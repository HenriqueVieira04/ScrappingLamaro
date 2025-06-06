from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from soup_html import get_disciplinas_e_curso
import time

class ScraperUSP:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        self.URL_INICIAL = "https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275"
        
        # Estruturas de dados
        self.units = []
        self.courses = []
        self.curriculums = []

    def initialize(self):
        """Inicializa o navegador e carrega a página inicial"""
        self.driver.get(self.URL_INICIAL)
        time.sleep(1)  # Espera inicial para carregamento completo

    def get_units(self):
        """Obtém todas as unidades disponíveis"""
        select_unit = Select(self.driver.find_element(By.ID, "comboUnidade"))
        unit_options = select_unit.options[1:]  # Remove a primeira opção vazia
        
        for unit_option in unit_options:
            self.units.append({
                'value': unit_option.get_attribute('value'),
                'name': unit_option.text
            })
            print(f"Unidade encontrada: {unit_option.text}")

    def process_unit(self, unit):
        """Processa uma unidade específica"""
        print(f"\nProcessando unidade: {unit['name']}")
        
        try:
            # Seleciona a unidade
            Select(self.driver.find_element(By.ID, "comboUnidade")).select_by_value(unit['value'])
            time.sleep(1)  # Pequena espera para atualização
            
            # Obtém cursos da unidade
            self.process_courses()
            
        except Exception as e:
            print(f"Erro ao processar unidade {unit['name']}: {str(e)}")
            return False
        return True

    def process_courses(self):
        """Processa todos os cursos de uma unidade"""
        try:
            select_course = Select(self.driver.find_element(By.ID, "comboCurso"))
            course_options = select_course.options[1:]  # Remove opção vazia
            
            if not course_options:
                print("Nenhum curso encontrado para esta unidade")
                return
            
            for course_option in course_options:
                course = {
                    'value': course_option.get_attribute('value'),
                    'name': course_option.text
                }
                self.courses.append(course)
                
                # Processa o curso individualmente
                self.process_course(course)
                
                # Volta para a aba de busca
                self.driver.find_element(By.ID, "step1-tab").click()
                time.sleep(1)
                
        except Exception as e:
            print(f"Erro ao buscar cursos: {str(e)}")

    def process_course(self, course):
        """Processa um curso específico para obter grade curricular"""
        print(f"  Processando curso: {course['name']}")
        
        try:
            # Seleciona o curso
            Select(self.driver.find_element(By.ID, "comboCurso")).select_by_value(course['value'])
            
            # Clica em buscar
            self.driver.find_element(By.ID, "enviar").click()
            
            # Processa grade curricular
            self.process_curriculum(course)
            
        except Exception as e:
            print(f"Erro ao processar curso {course['name']}: {str(e)}")

    def process_curriculum(self, course):
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
            with open(f"html/{course['name']}.html", "w", encoding="utf-8") as file:
                file.write(html_content)
            
            # Extrai disciplinas
            course = get_disciplinas_e_curso(f"html/{course['name']}.html")
            self.courses.append(course)
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
            self.get_units()
            
            for unit in self.units:
                self.process_unit(unit)
                
        finally:
            self.driver.quit()
            print("Processo concluído")

# Execução principal
if __name__ == "__main__":
    scraper = ScraperUSP()
    scraper.run()