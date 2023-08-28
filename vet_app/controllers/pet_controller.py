from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_al()
    return render_template("pets/index.html", pets=pets)

@pets_blueprint.route("/pets/<id>")
def show(id):
    pet = pet_repository.select(id)
    return render_template("pets/show.html", pet=pet)

# @pets_blueprint.route("/pets", methods=['POST'])
# def save_pet():
#     name = request.form['name']
#     dob = request.form['dob']
#     gender = request.form['gender']
#     species = request.form['species']
#     contact_details = request.form['contact_details']
#     treatment_notes = request.form['treatment_notes']
#     vet = request.form['vet_id']
#     admission_date = request.form['admission_date']
#     pet_id = request.form['pet_id']


    
