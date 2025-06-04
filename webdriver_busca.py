from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import os

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
URL_INICIAL = "https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275"
driver.get(URL_INICIAL)

select_unit = Select(wait.until(EC.presence_of_element_located((By.ID, "comboUnidade"))))
# select_unit = driver.find_elements(By.ID, "comboUnidade")
# for elem in select_unit:
#     print(elem.text)

# os.makedirs("grades_html", exist_ok=True)

# Pega todos os valores das unidades de uma vez
unit_options = [
    (opt.get_attribute("value"), opt.text.strip())
    for opt in select_unit.options[1:]  # Ignora a primeira ("Selecione")
]

for unit_value, unidade_nome in unit_options:
#     print("---------------- " + unidade_nome + " ----------------")
    try:
        # Seleciona a unidade
        select_unit.select_by_value(unit_value)
        time.sleep(3)

        try:
            select_course = Select(driver.find_element(By.ID, "comboCurso"))
        except:
            print(f"[AVISO] Nenhum curso para a unidade {unidade_nome}")
            continue

        course_options = [
            (opt.get_attribute("value"), opt.text.strip())
            for opt in select_course.options[1:]
        ]

        for curso_value, curso_nome in course_options:
            try:
                select_course.select_by_value(curso_value)
                time.sleep(3)

                # Clica em "Buscar"
                btn_buscar = wait.until(EC.element_to_be_clickable((By.ID, "enviar")))
                btn_buscar.click()

                # Espera o botão "Grade Curricular" aparecer
                wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='step4-tab']")))

                # Clica em "Grade Curricular"
                btn_grade = wait.until(EC.element_to_be_clickable((By.ID, "step4-tab")))
                btn_grade.click()
                time.sleep(3)
            except Exception as e:
                print(f"[ERRO] {unidade_nome} - {curso_nome}: {e}")

            # Volta para a página inicial 
            btn_busca = wait.until(EC.element_to_be_clickable((By.ID, "step1-tab")))
            btn_busca.click()

    except Exception as e:
        print(f"[ERRO NA UNIDADE] {unidade_nome}: {e}")
        exit(1)

driver.quit()
