from helpers.routes import *

class Salon:
    def __init__(self, id, grado_id, seccion_id, nivel_id):
        self.id = id
        self.grado_id = grado_id
        self.seccion_id = seccion_id
        self.nivel_id = nivel_id

    def insert_salon(self):
        try:
            conn = Connection('reformatorio')
            conn.insert('salon', {
                'grado_id': self.grado_id,
                'seccion_id': self.seccion_id,
                'nivel_id': self.nivel_id
            })
            print(f'Se registro el salon')
        except Exception as e:
            print(e)

    def all_salon(self):
        try:
            conn = Connection('reformatorio')
            data = conn.get_all('salon')

            p = PrettyTable()
            print("-- LISTA DE SALONES --".center(80))
            p.field_names = ["ID", "grado_id", "seccion_id", "nivel_id"]

            for value in data:
                p.add_row([value["_id"], value["grado_id"], value["seccion_id"], value["nivel_id"]])
            print(p)

        except Exception as e:
            print(e)

    def update_salon(self):
        try:
            conn = Connection('reformatorio')
            conn.update('salon', {
                'id': {
                    '$ne': self.id
                }
            }, {
                'grado_id': self.grado_id,
                'seccion_id': self.seccion_id,
                'nivel_id': self.nivel_id
            })
            print(f'Se modifico el salon')
        except Exception as e:
            print(e)

    def delete_salon(self):
        try:
            conn = Connection('reformatorio')
            conn.delete('salon', {
                'id': {
                    '$gt': self.id
                }
            })
            print(f'Se elimino el salon.')
        except Exception as e:
            print(e)