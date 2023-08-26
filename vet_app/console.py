# import pdb

from models.pet import Pet
from models.vet import Vet
# from models.owner import Owner

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

from datetime import datetime

# pet_repository.delete_all()

pet_1 = Pet("Harry", "2023-05-03", "male", "dragon", "014197245", "broken leg")
pet_2 = Pet("Derek", "2010-02-13", "male", "ostrich", "3578479456", "damaged nose")
pet_repository.save(pet_1)
pet_repository.save(pet_2)

vet_1 = Vet("Shawlands Vet", "-Address Info Here-")
vet_repository.save(vet_1)

# print(pet_repository.select(2))
# print("------------")
# print(pet_repository.select_all())

# print(datetime.now())

# now = datetime.now() 
# time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(time)

