from flask import render_template
from amigos import app

# importar la clase de Amigos de la carpeta models del archivo amigo.py
from amigos.models.amigo import Amigos


@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    friends = Amigos.get_all()
    print(friends)
    return render_template("index.html")