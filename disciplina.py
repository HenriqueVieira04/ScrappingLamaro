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
