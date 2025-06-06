class Unidade:
    def __init__(self, courses=[]):
        self.courses = courses
    
    def searchCourses(self):
        return self.courses

    def __str__(self):
        return '\n'.join(str(course) for course in self.courses)
