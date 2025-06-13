class Disciplina:
    def __init__(self, code, name, class_credits, work_credits, ch, ce, cp, atpa):
        self.code = code
        self.name = name
        self.class_credits = class_credits
        self.work_credits = work_credits
        self.ch = ch
        self.ce = ce
        self.cp = cp
        self.atpa = atpa
        self.inCourse = []

    # ----------------- Getters ----------------- #

    def get_code(self):
        return self.code
    
    def get_name(self):
        return self.name
    
    def get_class_credits(self):
        return self.class_credits
    
    def get_work_credits(self):
        return self.work_credits
    
    def get_ch(self):
        return self.ch
    
    def get_ce(self):
        return self.ce
    
    def get_cp(self):
        return self.cp
    
    def get_atpa(self):
        return self.atpa
    
    # ----------------- Setters ----------------- #

    def set_code(self, value):
        self.code = value

    def set_name(self, value):
        self.name = value

    def set_class_credits(self, value):
        self.class_credits = value

    def set_work_credits(self, value):
        self.work_credits = value

    def set_ch(self, value):
        self.ch = value

    def set_ce(self, value):
        self.ce = value

    def set_cp(self, value):
        self.cp = value

    def set_atpa(self, value):
        self.atpa = value

    # ----------------- Funcs ----------------- #

    
    def __str__(self): # definição do str para posterior uso do print
        cursos_formatados = "Nenhum curso associado."
        if self.inCourse: # conversão da lista de cursos onde pertence para uma string formatada
            cursos_formatados = "\n".join([f"    - {nome_curso}" for nome_curso in self.inCourse])
        
        return (
            f"Código: {self.code}\n"
            f"Nome: {self.name}\n"
            f"Créditos aula: {self.class_credits}\n"
            f"Créditos trabalho: {self.work_credits}\n"
            f"Carga horária (CH): {self.ch}\n"
            f"Carga teórica (CE): {self.ce}\n"
            f"Carga prática (CP): {self.cp}\n"
            f"ATPA: {self.atpa}\n"
            f"Pertencente aos cursos:\n{cursos_formatados}" # Usa a string formatada
        )

# função que verifica se uma disciplina esta presente no dicionario de disciplinas
def belongs_to_dict(cod_disciplina, disciplinas): 
    for chave, disciplina_obj in disciplinas.items():
        if disciplina_obj.code == cod_disciplina:
            return chave
    
    return None 

# função que adiciona disciplina no dicionario de disciplinas
def add_subject_dict(code, name, class_credits, work_credits, ch, ce, cp, atpa, disciplinas):
    newdisci =  Disciplina(code, name, class_credits, work_credits, ch, ce, cp, atpa)
    disciplinas[code] = newdisci
