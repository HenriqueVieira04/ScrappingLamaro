class Unidade:
    def __init__(self, courses=[]):
        self.courses = courses
    
    def inUnit(self, nomeCurso):
        for chave, curso in self.courses:
            if nomeCurso == curso.name:
                return chave
    
        return -1
        
    def __str__(self):
        if not self.courses:
            return "Unidade sem cursos."
        return "\n".join(str(curso) for curso in self.courses)

    def addCurso(self, curso):
        if curso != None:
            self.courses.append(curso)

    def deleteCurso(self, nomeCurso):
        index = self.inUnit(nomeCurso)
        if (index != -1):
            self.courses.pop(index)

    def qtdCourses(self):
        return len(self.courses)


