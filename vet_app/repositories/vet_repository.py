# import pdb
from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet

from datetime import datetime

def save(vet):
    sql = "INSERT INTO vets(name, address) VALUES ( %s, %s ) RETURNING *"
    values = [vet.name, 
              vet.address]
    results = run_sql( sql, values )

    vet.id = results[0]['vet_id']
    # vet.current_pets = results[0]['current_pets_id']
    return vet

def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['name'], row['address'], row['vet_id'])
        vets.append(vet)
    return vets

def select(id):
    sql = "SELECT * FROM vets WHERE vet_id = %s"
    values = [id]
    results = run_sql(sql,values)

    vet_id = results[0]['vet_id']
    name = results[0]['name']
    address = results[0]['address']
    vet = Vet(name,address,vet_id)
    return vet


def delete(id):
    sql = "DELETE FROM vets WHERE vet_id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

