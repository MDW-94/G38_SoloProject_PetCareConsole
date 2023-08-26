# import pdb
from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet

from datetime import datetime

def save(pet):
    now = datetime.now() 
    time = now.strftime("%m/%d/%Y, %H:%M:%S")
    sql = "INSERT INTO pets (name, dob, gender, species, contact_details, treatment_notes, admission_date) VALUES ( %s, %s, %s, %s, %s, %s, %s) RETURNING id, admission_date"
    values = [pet.name, 
              pet.dob, 
              pet.gender, 
              pet.species, 
              pet.contact_details, 
              pet.treatment_notes,
              time]
    results = run_sql( sql,values )
    # pdb.set_trace()
    id = results[0]['id']
    admission_date = results[0]['admission_date']
    pet.id = id
    pet.admission_date = admission_date
    return pet

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    pet = results
    # if results:
    #     result = results[0]
    #     pet = Pet(result['name'], 
    #               result['dob'], 
    #               result['gender'], 
    #               results['species'],
    #               results['contact_details'],
    #               results['treatment_notes'],
    #               results['admission_date'],
    #               results['id'])
    return pet


def update_details(id):
    sql = "UPDATE pets SET ... WHERE id = %s"


def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)



