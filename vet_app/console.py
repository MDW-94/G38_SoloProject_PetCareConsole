# import pdb

from models.pet import Pet
from models.vet import Vet
from models.notes import Notes
# from models.owner import Owner

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.notes_repository as notes_repository

from datetime import datetime

# pet_repository.delete_all()
# vet_repository.delete_all()

vet_1 = Vet("Shawlands Vet", "-Address Info Here-")
vet_2 = Vet("The Other Vet", "-Address Info Here-")
vet_repository.save(vet_1)
vet_repository.save(vet_2)

pet_1 = Pet("Harry", "to-be-datetime", "male", "dragon", "assign-contact_details-to-owner", "create timestamp, broken leg", vet_1)
pet_2 = Pet("Derek", "to-be-datetime", "male", "ostrich", "3578479456", "damaged nose", vet_1)
pet_repository.save(pet_1)
pet_repository.save(pet_2)

note_1 = Notes("Recovering from broken leg", "to-be-datetime", pet_1, vet_2)
note_2 = Notes("Still Recovering from broken leg but looking better than a second ago", "to-be_datetime", pet_1, vet_2)
notes_repository.save(note_1)
notes_repository.save(note_2)


# print(vet_repository.select(1).name)
# print(vet_repository.select(1).address)
# print(vet_repository.select(1).id)

# print(pet_repository.select(1).name)
# print(pet_repository.select(1).dob)
# print(pet_repository.select(1).gender)
# print(pet_repository.select(1).species)
# print(pet_repository.select(1).contact_details)
# print(pet_repository.select(1).treatment_notes)
# print(pet_repository.select(1).vet.id)
# print(pet_repository.select(1).admission_date)
# print(pet_repository.select(1).id)

# print(vet_repository.select_all())
# print(pet_repository.select_all())

# vet_repository.delete(1)
# pet_repository.delete(2)

# pet_2.name = "Test"
# pet_2.dob = "Test"
# pet_2.gender = "Test"
# pet_2.species = "Test"
# pet_2.contact_details = "Test"
# pet_2.treatment_notes = "Test"
# pet_2.admission_date = "Test"
# pet_2.vet.id = 1
# pet_repository.update(pet_2)

# vet_1.name = "Test"
# vet_1.address = "Test"
# vet_1.id = 7
# vet_repository.update(vet_1)


