from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pets_blueprint = Blueprint("pets", __name__)

# INDEX
@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets=pets)

# SHOW
@pets_blueprint.route("/pets/<id>")
def show(id):
    pet = pet_repository.select(id)
    return render_template("pets/show.html", pet=pet)

# NEW
@pets_blueprint.route("/pets/new")
def add_pet():
    return render_template("pets/new.html")

# SAVE
@pets_blueprint.route("/pets", methods=['POST'])
def create_pet():
    name = request.form['name']
    dob = request.form['dob']
    gender = request.form['gender']
    species = request.form['species']
    contact_details = request.form['contact_details']
    treatment_notes = request.form['treatment_notes']
    vet = request.form['vet_id']
    admission_date = request.form['admission_date']
    pet_id = request.form['pet_id']
    new_pet = Pet(name, 
                  dob, 
                  gender, 
                  species, 
                  contact_details, 
                  treatment_notes,
                  vet,
                  admission_date,
                  pet_id,)
    pet_repository.save(new_pet)
    return redirect("/pets")

# EDIT
@pets_blueprint.route("/pets/<id>/edit")
def edit_pet(id):
    pet = pet_repository.select(id)
    return render_template('pets/edit.html', pet = pet)

# UPDATE
@pets_blueprint.route("/pets/<id>", methods=["POST"])
def update_pet(id):
    name = request.form["name"]
    dob = request.form["name"]
    gender = request.form["name"]
    species = request.form["name"]
    contact_details = request.form["name"]
    treatment_notes = request.form["name"]
    vet = request.form["name"] #vet.id?
    admission_date = request.form["name"]
    pet = Pet(name, dob, gender, species, contact_details, treatment_notes, vet, admission_date, id)
    pet_repository.update(pet)
    return redirect ("/pets")

# DELETE
@pets_blueprint.route("/pets/<id>/delete", methods=["POST"])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect("/pets")
    
