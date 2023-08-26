# import pdb
from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet

from datetime import datetime

def save(vet):
    sql = "INSERT INTO vets(name, address) VALUES ( %s, %s ) RETURNING vet_id, current_pets_id"
    values = [vet.name, 
              vet.address]
    results = run_sql( sql, values )
    vet.id = results[0]['vet_id']
    vet.current_pets = results[0]['current_pets_id']
    return vet