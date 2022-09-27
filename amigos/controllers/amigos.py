from flask import render_template
from amigos import app

# importar la clase de Amigos de la carpeta models del archivo amigo.py
from amigos.models.amigo import Amigos


#OPERACION READ(LEER)
@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    friends = Amigos.get_all()
    print(friends)
    return render_template("index.html", todos_amigos=friends)

@app.route("/<int:id>")
def un_usuario(id):
    data = {
        "identificador":id
    }
    amigo = Amigos.get_un_amigo(data)
    print(amigo)
    return amigo