from db.run_sql import run_sql
from models.notes import Note
from models.pet import Pet
from models.vet import Vet

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

from datetime import datetime

def save(notes):
    now = datetime.now()
    time = now.strftime("%m/%d/%Y, %H:%M:%S")
    sql = "INSERT INTO notes (treatment_notes, date_time, pet_id, vet_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [notes.treatment, time, notes.pet.id, notes.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    notes.id = id
    return print(notes)


def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    results = run_sql(sql)
    for result in results:
        human = human_repository.select(result["human_id"])
        zombie = zombie_repository.select(result["zombie_id"])
        biting = Biting(human, zombie, result["id"])
        bitings.append(biting)
    return bitings


def select(id):
    biting = None 
    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]

    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        human = human_repository.select(result["human_id"])
        zombie = zombie_repository.select(result["zombie_id"])
        biting = Biting(human, zombie, result["id"])
    return biting


def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bitings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(biting):
    sql = "UPDATE bitings SET (human_id, zombie_id) = (%s, %s) WHERE id = %s"
    values = [biting.human.id, biting.zombie.id, biting.id]
    run_sql(sql, values)