from db.run_sql import run_sql
from models.notes import Notes
from models.pet import Pet
from models.vet import Vet
import pdb

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

from datetime import datetime

def save(notes):
    now = datetime.now()
    time = now.strftime("%m/%d/%Y, %H:%M:%S")
    sql = "INSERT INTO notes (treatment_notes, date_time, pet_id, vet_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [notes.notes, notes.date, notes.pet.id, notes.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    notes.id = id
    return print(notes)


def select_all():
    # pdb.set_trace()
    notes = []
    sql = "SELECT * FROM notes"
    results = run_sql(sql)
    for result in results:
        pet = pet_repository.select(result["pet_id"])
        vet = vet_repository.select(result["vet_id"])
        note = Notes(result['treatment_notes'],result['date_time'],pet, vet, result["id"])
        notes.append(note)
    return notes


def select(id):
    biting = None 
    sql = "SELECT * FROM notes WHERE id = %s"
    values = [id]

    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        pet = pet_repository.select(result["pet_id"])
        vet = vet_repository.select(result["vet_id"])
        notes = Notes(pet, vet, result["id"])
    return notes


def delete_all():
    sql = "DELETE FROM notes"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM notes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# def update(notes):
#     sql = "UPDATE notes SET (treatment_notes, pet_id, vet_id) = (%s, %s, %s) WHERE id = %s"
#     values = [notes.human.id, biting.zombie.id, biting.id]
#     run_sql(sql, values)