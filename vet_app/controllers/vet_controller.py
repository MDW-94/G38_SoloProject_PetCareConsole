from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vet import Vet
import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository

vets_blueprint = Blueprint("vets", __name__)

# INDEX
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets=vets)

# SHOW
@vets_blueprint.route("/vets/<id>")
def show(id):
    vet = vet_repository.select(id)
    return render_template("vets/show.html", vet=vet)

# NEW
@vets_blueprint.route("/vets/new")
def new_vet():
    return render_template("vets/new.html")

# SAVE
@vets_blueprint.route("/vets", methods=['POST'])
def create_vet():
    name = request.form['name']
    address = request.form['address']
    # vet_id = request.form['vet_id']
    new_vet = Vet(name, 
                  address) 
                  #vet_id)
    vet_repository.save(new_vet)
    return redirect("/vets")

# EDIT
@vets_blueprint.route("/vets/<id>/edit")
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template('vets/edit.html', vet = vet)

# UPDATE
@vets_blueprint.route("/vets/<id>", methods=["POST"])
def update_vet(id):
    name = request.form["name"]
    address = request.form["address"]
    vet = Vet(name, address, id)
    vet_repository.update(vet)
    return redirect ("/vets")

# DELETE
@vets_blueprint.route("/vets/<id>/delete", methods=["POST"])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect("/vets")
    