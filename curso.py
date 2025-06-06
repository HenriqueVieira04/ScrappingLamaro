class Curso:
    def __init__(self, name, unit, ideal_duration, min_duration, max_duration, mandatory_subjects, free_elective_subjects, elective_optional_subjects):
        self.name = name
        self.unit = unit
        self.ideal_duration = ideal_duration
        self.min_duration = min_duration
        self.max_duration = max_duration
        self.mandatory_subjects = mandatory_subjects
        self.free_elective_subjects = free_elective_subjects
        self.elective_optional_subjects = elective_optional_subjects

    # ----------------- Getters ----------------- #

    def get_code(self):
        return self.code
    
    def get_name(self):
        return self.name
    
    def get_unit(self):
        return self.unit
    
    def get_ideal_duration(self):
        return self.ideal_duration
    
    def get_min_duration(self):
         return self.min_duration

    def get_max_duration(self):
        return self.max_duration
    
    def get_mandatory_subjects(self):
        return self.mandatory_subjects
    
    def get_free_elective_subjects(self):
        return self.free_elective_subjects
    
    def get_elective_optional_subjects(self):
        return self.elective_optional_subjects
    
    # ----------------- Setters ----------------- #

    def set_code(self, value):
        self.code = value
    
    def set_name(self, value):
        self.name = value
    
    def set_unit(self, value):
        self.unit = value
    
    def set_ideal_duration(self, value):
        self.ideal_duration = value
    
    def set_min_duration(self, value):
        self.min_duration = value

    def set_max_duration(self, value):
        self.max_duration = value
    
    def set_mandatory_subjects(self, value):
        self.mandatory_subjects = value
    
    def set_free_elective_subjects(self, value):
        self.free_elective_subjects = value
    
    def set_elective_optional_subjects(self, value):
        self.elective_optional_subjects = value

    # ----------------- Funcs ----------------- #

    def __str__(self):
        return (
            f"Nome: {self.name}\n"
            f"Unidade: {self.unit}\n"
            f"Duração ideal: {self.ideal_duration}\n"
            f"Duração mínima: {self.min_duration}\n"
            f"Duração máxima: {self.max_duration}\n"
            f"Disciplinas obrigatórias: {self.mandatory_subjects}\n"
            f"Disciplinas eletivas livres: {self.free_elective_subjects}\n"
            f"Disciplinas optativas eletivas: {self.elective_optional_subjects}\n"
        )