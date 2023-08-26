# import pdb
from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet

def save(pet):
    sql = "INSERT INTO pets (name, dob, gender, species, contact_details, treatment_notes, admission_date) VALUES ( %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) RETURNING id, admission_date"
    values = [pet.name, 
              pet.dob, 
              pet.gender, 
              pet.species, 
              pet.contact_details, 
              pet.treatment_notes]
    results = run_sql( sql,values )
    # pdb.set_trace()
    id = results[0]['id']
    admission_date = results[0]['admission_date']
    pet.id = id
    pet.admission_date = admission_date
    return pet