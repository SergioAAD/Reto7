from helpers.routes import *

class Seccion:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def insert_seccion(self):
        try:
            conn = Connection('reformatorio')
            conn.insert('seccion', {
                'nombre': self.nombre
            })
            print(f'Se registro el seccion')
        except Exception as e:
            print(e)

    def all_seccion(self):
        try:
            conn = Connection('reformatorio')
            data = conn.get_all('seccion')

            p = PrettyTable()
            print("-- LISTA DE seccionS --".center(80))
            p.field_names = ["ID", "Nombre"]

            for value in data:
                p.add_row([value["_id"], value["nombre"]])
            print(p)

        except Exception as e:
            print(e)

    def update_seccion(self):
        try:
            conn = Connection('reformatorio')
            conn.update('seccion', {
                'id': {
                    '$ne': self.id
                }
            }, {
                'nombre': self.nombre
            })
            print(f'Se modifico la seccion')
        except Exception as e:
            print(e)

    def delete_seccion(self):
        try:
            conn = Connection('reformatorio')
            conn.delete('seccion', {
                'nombre': {
                    '$gt': self.nombre
                }
            })
            print(f'Se elimino la seccion.')
        except Exception as e:
            print(e)