# import pdb

from models.pet import Pet
from models.vet import Vet
# from models.owner import Owner

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

from datetime import datetime

# pet_repository.delete_all()
vet_1 = Vet("Shawlands Vet", "-Address Info Here-")
vet_repository.save(vet_1)

pet_1 = Pet("Harry", "2023-05-03", "male", "dragon", "014197245", "broken leg", vet_1)
pet_2 = Pet("Derek", "2010-02-13", "male", "ostrich", "3578479456", "damaged nose", vet_1)
pet_repository.save(pet_1)
pet_repository.save(pet_2)

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

print(vet_repository.select_all())
print(pet_repository.select_all())



# print(pet_repository.select(2))
# print("------------")
# print(pet_repository.select_all())

# print(datetime.now())

# now = datetime.now() 
# time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(time)

