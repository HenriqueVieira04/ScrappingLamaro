from bs4 import BeautifulSoup

with open("html/bcc.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

unit = soup.find('span', class_="unidade")

name_course = soup.find('span', class_="curso")

ideal_dur = soup.find('span', class_="duridlhab")

min_dur = soup.find('span', class_="durminhab")

max_dur = soup.find('span', class_="durmaxhab")

disciplinas = soup.find('div', id="gradeCurricular")
tabelas = disciplinas.find_all('table')
for tabela in tabelas:
    for corpo_tabela in tabela.find_all('tbody'):
        for linha in corpo_tabela.find_all('tr'):
            for dados in linha.find_all('td'):
                print(dados.contents)

