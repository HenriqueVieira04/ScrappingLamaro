from bs4 import BeautifulSoup
from disciplina import Disciplina
from curso import Curso

def get_disciplinas_e_curso(path):
    """
        Função que realiza a busca dos dados necessários em um arquivo .html

        Parâmetros: 
            path: Caminho do arquivo
        
        Retorno:
            curso: Objeto do tipo Curso 
            disciplinas_obrigatorias: Array de objetos do tipo Disciplina (disciplinas obrigatórias) 
            disciplinas_livres: Array de objetos do tipo Disciplina (disciplinas livres) 
            disciplinas_eletivas: Array de objetos do tipo Disciplina (disciplinas eletivas) 
    """

    # Abertura do arquivo html
    with open(path, 'r', encoding='utf-8') as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    unidade = soup.find('span', class_="unidade").contents[0]
    nome_curso = soup.find('span', class_="curso").contents[0]

    # Duração do curso
    ideal_dur = soup.find('span', class_="duridlhab").contents[0]
    min_dur = soup.find('span', class_="durminhab").contents[0]
    max_dur = soup.find('span', class_="durmaxhab").contents[0]

    # Onde estão os tipos e tabelas de disciplinas
    tipos_disciplinas = soup.find_all('td', attrs={
        'style': 'padding: 5px; font-weight: bold;',
        'colspan': '8'
    })

    # Busca das disciplinas
    disciplinas = soup.find('div', id="gradeCurricular")
    tabelas_disciplinas = disciplinas.find_all('table')

    # Inicializa os arrays das disciplinas
    disciplinas_obrigatorias = []
    disciplinas_livres = []
    disciplinas_eletivas = []

    # Associa cada tipo de disciplina à sua tabela correspondente
    for tipo, tabela in zip(tipos_disciplinas, tabelas_disciplinas):
        nome_tipo = tipo.text.strip()
        linhas = tabela.find_all('tr', style="height: 20px;")

        # Cria um array de objetos do tipo Disciplina com todas as disciplinas encontradas
        lista_disciplinas = [
            # Encontra todas as células (<td>) dentro de uma linha de tabela
            # Para cada célula da linha, pega o texto com td.text e remove os espaços extras
            # O conteúdo da lista será passado como argumentos individuais para o construtor da classe Disciplina
            Disciplina(*[td.text.strip() for td in linha.find_all('td')])
            for linha in linhas
        ]

        if nome_tipo == "Disciplinas Obrigatórias":
            disciplinas_obrigatorias = lista_disciplinas
        elif nome_tipo == "Disciplinas Optativas Livres":
            disciplinas_livres = lista_disciplinas
        elif nome_tipo == "Disciplinas Optativas Eletivas":
            disciplinas_eletivas = lista_disciplinas

    curso = Curso(nome_curso, unidade, ideal_dur, min_dur, max_dur, disciplinas_obrigatorias, disciplinas_livres, disciplinas_eletivas)
    
    print(curso)

    return curso