from flask import Flask, render_template, request
# from controllers.vets_controllers import vets_blueprint
# from controllers.pets_controllers import pets_blueprint
# from controllers.owners_controllers import owners_blueprint

app = Flask(__name__)

#app.register_blueprint(vets_blueprint)
#app.register_blueprint(pets_blueprint)
#app.register_blueprint(owners_blueprint)

#@app.route('/')
#def home():
#   return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)