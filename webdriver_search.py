from selenium import webdriver
import time
from soup_html import get_disciplinas_e_curso
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

URL_INICIAL = "https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275"
driver.get(URL_INICIAL)

time.sleep(1)
select_unit = Select(driver.find_element(By.ID, "comboUnidade"))

# Webelements list 
unit_options = select_unit.options
del unit_options[0] # Delete empty option

# Vetor para as unidades, cursos, grades_curriculares possuindo valor e nome.
units_value_name = []
courses_value_name = []
course_grade_curricular = []

# Guarda as unidades e seus valores e imprime as opções de unidades e index da posição.
for index, unit_option in enumerate(unit_options):
    units_value_name.append([unit_option.get_attribute('value'), unit_option.text])
    print(f"{index}: {unit_option.text}") 


# Botões fixos
btn_buscar = driver.find_element(By.ID, "enviar")
a_buscar = driver.find_element(By.ID, "step1-tab")

# Percorrer unidades
for unit_value, unit_name in units_value_name:
    # print("---------------- " + unidade_nome + " ----------------")
    try:
        # Seleciona a unidade
        select_unit.select_by_value(unit_value)
        time.sleep(1)

        try:
            select_course = Select(driver.find_element(By.ID, "comboCurso"))
        except:
            print(f"[AVISO] Nenhum curso para a unidade {unit_name}")
            continue

        # Faz um vetor com todas as opções do select
        course_options = select_course.options
        del course_options[0]
        
        # Percorre todos os cursos
        for index, course_option in enumerate(course_options):
            course_value = course_option.get_attribute('value')
            course_name = course_option.text
            courses_value_name.append([courses_value_name, course_name])
            try:
                select_course.select_by_value(course_value)

                # Click "Buscar"
                btn_buscar.click()
                
                try:                    
                    # Espera explícita para o botão "Grade Curricular" ficar clicável
                    a_grade_curricular = wait.until(EC.element_to_be_clickable((By.ID, "step4-tab")))
                        
                    a_grade_curricular.click()
                    time.sleep(2)
                    
                    # Obter o HTML completo da página
                    html_content = driver.page_source
                    
                    # Salvar em um arquivo
                    with open("html/pagina.html", "w", encoding="utf-8") as file:
                        file.write(html_content)
                        
                    course_grade_curricular.append(get_disciplinas_e_curso("html/pagina.html"))
                            
                except:
                    # Clica no botão "Grade Curricular"   
                    # btn_fechar = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/button") 
                    btn_fechar = wait.until(EC.element_to_be_clickable((By.XPATH, 
                                                                    "/html/body/div[7]/div[3]/div/button")))
     
                    btn_fechar.click()
                
            except Exception as erro:
                print(f"[ERRO] {unit_name} - {course_name}: {erro}")

            
            # Click "Buscar"
            a_buscar.click()
            time.sleep(1)
            
            
    except Exception as erro:
        print(f"[ERRO NA UNIDADE] {unit_name}: {erro}")
        exit(1)

driver.quit()
