# import pdb
from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet

from datetime import datetime

import repositories.vet_repository as vet_repository

def save(pet):
    now = datetime.now() 
    time = now.strftime("%m/%d/%Y, %H:%M:%S")
    sql = "INSERT INTO pets (name, dob, gender, species, contact_details, treatment_notes, vet_id, admission_date) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s ) RETURNING *"
    values = [pet.name, 
              pet.dob, 
              pet.gender, 
              pet.species, 
              pet.contact_details, 
              pet.treatment_notes,
              pet.vet.id,
              time]
    results = run_sql( sql,values )
    # pdb.set_trace()
    id = results[0]['pet_id']
    admission_date = results[0]['admission_date']
    vet_id = results[0]['vet_id']
    pet.id = id
    pet.vet = vet_repository.select(vet_id)
    pet.admission_date = admission_date
    return pet

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE pet_id = %s"
    values = [id]
    results = run_sql(sql, values)

    pet_id = results[0]['pet_id']
    name = results[0]['name']
    dob = results[0]['dob']
    gender = results[0]['gender']
    species = results[0]['species']
    contact_details = results[0]['contact_details']
    treatment_notes = results[0]['treatment_notes']
    vet_id = results[0]['vet_id']
    vet = vet_repository.select(vet_id)
    admission_date = results[0]['admission_date']
    pet = Pet(name, dob, gender, species, contact_details, treatment_notes, vet, admission_date, pet_id)
   
    return pet

def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        pet = Pet(row['name'], 
                   row['dob'], 
                   row['gender'], 
                   row['species'], 
                   row['contact_details'], 
                   row['treatment_notes'], 
                   row['vet_id'], 
                   row['admission_date'], 
                   row['pet_id'])
        pets.append(pet)
    return pets

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM pets WHERE pet_id = %s"
    values = [id]
    run_sql(sql, values)

def update(pet):
    sql = "UPDATE pets SET (name, dob, gender, species, contact_details, treatment_notes, admission_date, vet_id) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE pet_id = %s"
    values = [pet.name, pet.dob, pet.gender, pet.species, pet.contact_details, pet.treatment_notes, pet.admission_date, pet.vet.id, pet.id]
    run_sql(sql, values)



# def update_treament_notes(pet):
#     sql = "UPDATE pets SET treatment_notes = %s WHERE id = %s"
#     values = [human.name, human.id]
#     run_sql(sql, values)

# def assign_vet():

# def update_details(pet):
#     sql = "UPDATE pets SET (name, dob, gender, species, contact_details, treatment_notes) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
#     values = [pet.name, pet.dob, pet.gender, pet.species, pet.contact_details, pet.treatment_notes, pet.admission_date]
#     run_sql(sql, values)

# separate functions for updating treatment notes?

# def update_treatment(id): #?return treatment_notes, store them in variable, then add that variable to a date time plus input
#     now = datetime.now() 
#     time = now.strftime("%m/%d/%Y, %H:%M:%S")
#     sql = "INSERT INTO treatment_notes VALUES (%s) WHERE pet_id = %s"
#     values =





