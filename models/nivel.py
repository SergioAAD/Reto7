from helpers.routes import *

class Nivel:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def insert_nivel(self):
        try:
            conn = Connection('reformatorio')
            conn.insert('nivel', {
                'nombre': self.nombre
            })
            print(f'Se registro el nivel')
        except Exception as e:
            print(e)

    def all_nivel(self):
        try:
            conn = Connection('reformatorio')
            data = conn.get_all('nivel')

            p = PrettyTable()
            print("-- LISTA DE CURSOS --".center(80))
            p.field_names = ["ID", "Nombre"]

            for value in data:
                p.add_row([value["_id"], value["nombre"]])
            print(p)

        except Exception as e:
            print(e)

    def update_nivel(self):
        try:
            conn = Connection('reformatorio')
            conn.update('nivel', {
                'nombre': {
                    '$lt': self.nombre
                }
            }, {
                'nombre': self.nombre
            })
            print(f'Se modifico el curso')
        except Exception as e:
            print(e)

    def delete_nivel(self):
        try:
            conn = Connection('reformatorio')
            conn.delete('nivel', {
                'nombre': {
                    '$gt': self.nombre
                }
            })
            print(f'Se elimino el curso.')
        except Exception as e:
            print(e)