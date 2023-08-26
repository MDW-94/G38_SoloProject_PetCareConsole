# import pdb

from models.pet import Pet
from models.vet import Vet
# from models.owner import Owner

import repositories.pet_repository as pet_repository

pet_1 = Pet("Harry", "2023-05-03", "male", "dragon", "014197245", "broken leg") #CURRENT_TIMESTAMP as string input?
pet_repository.save(pet_1)