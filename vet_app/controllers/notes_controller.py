from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.notes import Notes

import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository
import repositories.pet_repository as notes_repository

from datetime import datetime

notes_blueprint = Blueprint("notes", __name__)

# INDEX
@notes_blueprint.route("/notes")
def notes():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    notes = notes_repository.select_all()
    return render_template("notes/index.html", notes=notes, pets=pets, vets=vets)

# SHOW
@notes_blueprint.route("/notes/<id>")
def show(id):
    notes = notes_repository.select(id)
    return render_template("notes/show.html", notes=notes)

# NEW
@notes_blueprint.route("/notes/new")
def new_note():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("notes/new.html", pets=pets, vets=vets)

# SAVE
@notes_blueprint.route("/notes", methods=['POST'])
def create_notes():
    now = datetime.now()
    time = now.strftime("%m/%d/%Y, %H:%M:%S")

    notes = request.form['notes']
    date = time
    pet = pet_repository.select(request.form['pet.id'])
    vet = vet_repository.select(request.form['vet.id'])
    # vet_id = request.form['vet_id']
    new_note = Notes(notes, 
                  date,
                  pet,
                  vet) 
                  #vet_id)
    notes_repository.save(new_note)
    return redirect("/notes")

# EDIT
@notes_blueprint.route("/vets/<id>/edit")
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template('vets/edit.html', vet = vet)

# UPDATE
@notes_blueprint.route("/vets/<id>", methods=["POST"])
def update_vet(id):
    name = request.form["name"]
    address = request.form["address"]
    vet = Vet(name, address, id)
    vet_repository.update(vet)
    return redirect ("/vets")

# DELETE
@notes_blueprint.route("/vets/<id>/delete", methods=["POST"])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect("/vets")
    