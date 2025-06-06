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
        self.min_duration

    def get_max_duration(self):
        return self.max_duration
    
    def get_mandatory_subjects(self):
        return self.mandatory_subjects
    
    def get_free_elective_subjects(self):
        return self.free_elective_subjects
    
    def get_elective_optional_subjects(self):
        return self.elective_optional_subjects
    
    def __str__(self):
        return (
            f"Curso: {self.name}\n"
            f"Unidade: {self.unit}\n"
            f"Duração ideal: {self.ideal_duration} semestres\n"
            f"Duração mínima: {self.min_duration} semestres\n"
            f"Duração máxima: {self.max_duration} semestres\n"
            f"Disciplinas obrigatórias: {len(self.mandatory_subjects)}\n"
            f"Disciplinas eletivas livres: {len(self.free_elective_subjects)}\n"
            f"Disciplinas optativas eletivas: {len(self.elective_optional_subjects)}"
        )

            