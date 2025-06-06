from webdriver_busca import disciplinas

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

    

    def __str__(self):
        return (
            f"Código: {self.code}\n"
            f"Nome: {self.name}\n"
            f"Créditos aula: {self.class_credits}\n"
            f"Créditos trabalho: {self.work_credits}\n"
            f"Carga horária (CH): {self.ch}\n"
            f"Carga teórica (CE): {self.ce}\n"
            f"Carga prática (CP): {self.cp}\n"
            f"ATPA: {self.atpa}\n"
        )
