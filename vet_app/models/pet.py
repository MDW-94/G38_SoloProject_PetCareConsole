from datetime import datetime

class Pet:

    def __init__(self, 
                 name, 
                 dob, 
                 gender, 
                 species, 
                 contact_details, 
                 treatment_notes, 
                 vet, 
                 admission_date=None, 
                 id=None):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.species = species
        self.contact_details = contact_details
        self.treatment_notes = treatment_notes
        self.vet = vet
        self.admission_date = admission_date
        self.id = id