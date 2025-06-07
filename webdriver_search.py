from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from soup_html import get_disciplinas_e_curso
import time
from Unidade import Unidade

class ScraperUSP:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        self.URL_INICIAL = "https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275"
        
        # Estruturas de dados como dicionários
        self.units = {} # Dado o nome da unidade -> guarda um objeto Unidade
        self.courses = {} # Dado o nome de um curso -> retorna um objeto Curso
        self.disciplinas = {} # Dado código da disciplinas -> retorna objeto Disciplina

    def initialize(self):
        """Inicializa o navegador e carrega a página inicial"""
        self.driver.get(self.URL_INICIAL)
        time.sleep(1)  # Espera inicial para carregamento completo

    def process_units(self):
        """Obtém todas as unidades disponíveis e processa"""
        # Pega o select das unidades e obtém as suas opções na forma de vetor
        select_unit = Select(self.driver.find_element(By.ID, "comboUnidade"))
        unit_options = select_unit.options[1:]  # Remove a primeira opção vazia
        
        # Itera pelas opções(unidades)
        for unit_option in unit_options:
            unit_name = unit_option.text
            unit_value = unit_option.get_attribute('value')
            self.units[unit_name] = Unidade(unit_name)
            print(f"Unidade encontrada: {unit_name}")
        
            """Processa uma unidade específica"""
            print(f"\nProcessando unidade: {unit_name}")
            
            try:
                # Seleciona a unidade
                Select(self.driver.find_element(By.ID, "comboUnidade")).select_by_value(unit_value)
                time.sleep(1)  # Pequena espera para atualização
                
                # Obtém cursos da unidade
                self.process_courses(unit_name)
                
            except Exception as e:
                print(f"Erro ao processar unidade {unit_name}: {str(e)}")


    def process_courses(self, unit_name):
        """Processa todos os cursos de uma unidade"""
        try:
            # Obtem seletor dos cursos e pega suas opçãoes(cursos)
            select_course = Select(self.driver.find_element(By.ID, "comboCurso"))
            course_options = select_course.options[1:]  # Remove opção vazia
            
            if not course_options:
                print("Nenhum curso encontrado para esta unidade")
                return

            # Salva um vetor de cursos dada sua unidade
            self.units[unit_name].courses = course_options            
            
            # Itera sobre os cursos
            for course_option in course_options:
                course_value = course_option.get_attribute('value')
                course_name = course_option.text
                
                # Processa o curso individualmente
                self.process_course(course_name, course_value)
                
                # Volta para a aba de busca
                self.driver.find_element(By.ID, "step1-tab").click()
                time.sleep(1)
                
        except Exception as e:
            print(f"Erro ao buscar cursos: {str(e)}")

    def process_course(self, course_name, course_value):
        """Processa um curso específico para obter grade curricular"""
        print(f"  Processando curso: {course_name}")
        
        try:
            # Seleciona o curso
            Select(self.driver.find_element(By.ID, "comboCurso")).select_by_value(course_value)
            
            # Clica em buscar
            self.driver.find_element(By.ID, "enviar").click()
            
            # Processa grade curricular
            self.process_curriculum(course_name)
            
        except Exception as e:
            print(f"Erro ao processar curso {course_name}: {str(e)}")

    def process_curriculum(self, course_name):
        """Obtém a grade curricular de um curso"""
        try:
            # Espera e clica na grade curricular
            grade_tab = self.wait.until(
                EC.element_to_be_clickable((By.ID, "step4-tab")))
            grade_tab.click()
            
            # Espera o conteúdo carregar
            time.sleep(3)
            
            # Salva HTML e processa
            html_content = self.driver.page_source
            with open(f"html/course.html", "w", encoding="utf-8") as file:
                file.write(html_content)
            
            # Extrai disciplinas e atualiza o dicionário de cursos
            course = get_disciplinas_e_curso("html/course.html", self.disciplinas)
            self.courses[course_name] = course
            print(course)

        except Exception as e:
            print(f"Erro ao obter grade curricular: {str(e)}")
            self.close_popups()

    def close_popups(self):
        """Fecha possíveis popups que aparecem"""
        try:
            close_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[3]/div/button")))
            close_btn.click()
        except:
            pass

    def run(self):
        """Executa o processo completo"""
        try:
            self.initialize()
            self.process_units()
                
        finally:
            self.driver.quit()
            print("Processo concluído")
            print("\nDados coletados:")
            print(f"Unidades: {len(self.units)}")
            print(f"Cursos: {len(self.courses)}")
            # Exemplo de como acessar os dados:
            # print(self.units['unit_code']['name'])  # Nome de uma unidade
            # print(self.courses['course_code']['curriculum'])  # Currículo de um curso
