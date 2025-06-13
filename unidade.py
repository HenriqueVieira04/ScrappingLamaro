class Unidade:

    # ----------------- Construtor ----------------- #
    def __init__(self, name, courses=[]):
        self.name = name
        self.courses = courses
    
    # ----------------- Getters ----------------- #

    def get_name(self):
        return self.name
    
    def get_courses(self):
        return self.courses
    
    # ----------------- Setters ----------------- #

    def set_name(self, value):
        self.name = value

    def set_courses(self, value):
        self.courses = value

    # ------------------ Funcs ------------------ #

    # função que retorna a chave do curso caso ele esteja na lista, caso não, none
    def CursoInUnit(self, nomeCurso):
        for chave, curso in self.courses:
            if nomeCurso == curso.name:
                return chave
    
        return None
    
    # metodo auxiliar ao __str__
    def format_college_course(self):
        strg = "Cursos do/a " + self.name + ":\n"
        for course in self.courses:
            strg = strg + course + "\n"

        return strg

    # __str__ para print
    def __str__(self):
        if not self.courses:
            return "Unidade sem cursos."
        
        strg = self.format_college_course()
        return str(strg)   

    # adiciona um curso na lista
    def addCurso(self, curso):
        if curso != None:
            self.courses.append(curso)

    # deleta um curso da lista
    def deleteCurso(self, nomeCurso):
        index = self.inUnit(nomeCurso)
        if (index != None):
            self.courses.pop(index)

    # retorna a quantidade de cursos da lista
    def qtdCourses(self):
        return len(self.courses)

    # adiciona uma lista de cursos de uma vez no objeto
    def addCourseList(self, listCourses):
        if listCourses != None:
            self.courses = listCourses