# importar la función que devolverá una instancia de una conexión
from unittest import result
from amigos.config.mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos


class Amigos:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.ocupacion = data['ocupacion']
        self.creado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']
# ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM amigos;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('amigos_db').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        friends = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for friend in results:
            friends.append(cls(friend))
        return friends
    
    @classmethod
    def insertar_amigos(cls, data):
        consulta = "INSERT INTO......."
        resultados = connectToMySQL('amigos_db').query_db(consulta, data)
    
    @classmethod
    def get_un_amigo(cls, data):
        consulta = "SELECT * FROM amigos WHERE id=%(identificador)s;"
        resultados = connectToMySQL('amigos_db').query_db(consulta, data )
        return resultados

