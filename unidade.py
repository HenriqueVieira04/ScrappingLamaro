class Unidade:
    def __init__(self, name, courses=[]):
        self.name = name
        self.courses = courses
    
    def CursoInUnit(self, nomeCurso):
        for chave, curso in self.courses:
            if nomeCurso == curso.name:
                return chave
    
        return None
    
    def format_college_course(self):
        strg = "Cursos do/a " + self.name + ":\n"
        for course in self.courses:
            strg = strg + course.name + "\n"

        return strg

    def __str__(self):
        if not self.courses:
            return "Unidade sem cursos."
        
        strg = self.format_college_course()
        return str(strg)   

    def addCurso(self, curso):
        if curso != None:
            self.courses.append(curso)

    def deleteCurso(self, nomeCurso):
        index = self.inUnit(nomeCurso)
        if (index != None):
            self.courses.pop(index)

    def qtdCourses(self):
        return len(self.courses)

    def addCourseList(self, listCourses):
        if listCourses != None:
            self.courses = listCourses