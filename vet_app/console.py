# import pdb

from models.pet import Pet
from models.vet import Vet
# from models.owner import Owner

import repositories.pet_repository as pet_repository

pet_repository.delete_all()

pet_1 = Pet("Harry", "2023-05-03", "male", "dragon", "014197245", "broken leg")
pet_repository.save(pet_1)

