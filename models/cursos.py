from helpers.routes import *

class Cursos:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    
    def insert_cursos(self):
        try:
            conn = Connection('reformatorio')
            conn.insert('cursos', {
                'nombre': self.nombre
            })
            print(f'Se registro el curso')
        except Exception as e:
            print(e)

    def all_cursos(self):
        try:
            conn = Connection('reformatorio')
            data = conn.get_all('cursos')

            p = PrettyTable()
            print("-- LISTA DE CURSOS --".center(80))
            p.field_names = ["ID", "Nombre"]

            for value in data:
                p.add_row([value["_id"], value["nombre"]])
            print(p)

        except Exception as e:
            print(e)

    def update_cursos(self):
        try:
            conn = Connection('reformatorio')
            conn.update('cursos', {
                'id': {
                    '$ne': self.id
                }
            }, {
                'nombre': self.nombre
            })
            print(f'Se modifico el curso')
        except Exception as e:
            print(e)

    def delete_cursos(self):
        try:
            conn = Connection('reformatorio')
            conn.delete('cursos', {
                'nombre': {
                    '$gt': self.nombre
                }
            })
            print(f'Se elimino el curso.')
        except Exception as e:
            print(e)
