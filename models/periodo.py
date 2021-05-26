from helpers.routes import *

class Periodo:
    def __init__(self, id, nombre, ano):
        self.id = id
        self.nombre = nombre
        self.ano = ano

    def insert_periodo(self):
        try:
            conn = Connection('reformatorio')
            conn.insert('periodo', {
                'nombre': self.nombre,
                'ano': self.ano
            })
            print(f'Se registro el periodo')
        except Exception as e:
            print(e)

    def all_periodo(self):
        try:
            conn = Connection('reformatorio')
            data = conn.get_all('periodo')

            p = PrettyTable()
            print("-- LISTA DE PERIODO --".center(80))
            p.field_names = ["ID", "Nombre", "Año"]

            for value in data:
                p.add_row([value["_id"], value["nombre"], value["ano"]])
            print(p)

        except Exception as e:
            print(e)

    def update_periodo(self):
        try:
            conn = Connection('reformatorio')
            conn.update('periodo', {
                'id': {
                    '$ne': self.id
                }
            }, {
                'nombre': self.nombre,
                'ano': self.ano
            })
            print(f'Se modifico el periodo')
        except Exception as e:
            print(e)

    def delete_periodo(self):
        try:
            conn = Connection('reformatorio')
            conn.delete('periodo', {
                'nombre': {
                    '$gt': self.nombre
                }
            })
            print(f'Se elimino el periodo.')
        except Exception as e:
            print(e)