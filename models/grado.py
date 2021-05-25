from helpers.routes import *

class Grado:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def insert_grado(self):
        try:
            conn = Connection('reformatorio')
            conn.insert('grado', {
                'nombre': self.nombre
            })
            print(f'Se registro el grado')
        except Exception as e:
            print(e)

    def all_grado(self):
        try:
            conn = Connection('reformatorio')
            data = conn.get_all('grado')

            p = PrettyTable()
            print("-- LISTA DE CURSOS --".center(80))
            p.field_names = ["ID", "Nombre"]

            for value in data:
                p.add_row([value["_id"], value["nombre"]])
            print(p)

        except Exception as e:
            print(e)

    def update_grado(self):
        try:
            conn = Connection('reformatorio')
            conn.update('grado', {
                'nombre': {
                    '$lt': self.nombre
                }
            }, {
                'nombre': self.nombre
            })
            print(f'Se modifico el curso')
        except Exception as e:
            print(e)

    def delete_grado(self):
        try:
            conn = Connection('reformatorio')
            conn.delete('grado', {
                'nombre': {
                    '$gt': self.nombre
                }
            })
            print(f'Se elimino el curso.')
        except Exception as e:
            print(e)