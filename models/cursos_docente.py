from helpers.routes import *

class CursosDocente:
    def __init__(self, id, profesor_id, salon_id, cursos_id):
        self.id = id
        self.profesor_id = profesor_id
        self.salon_id = salon_id
        self.cursos_id = cursos_id
    
    def insert_cursos_docente(self):
        try:
            conn = Connection('reformatorio')
            conn.insert('cursos_docente', {
                'profesor_id': self.profesor_id,
                'salon_id': self.salon_id,
                'cursos_id': self.cursos_id
            })
            print(f'Se registro el curso del docente')
        except Exception as e:
            print(e)

    def all_cursos_docente(self):
        try:
            conn = Connection('reformatorio')
            data = conn.get_all('cursos_docente')

            p = PrettyTable()
            print("-- LISTA COMPLETA --".center(80))
            p.field_names = ["ID", "profesor_id", "salon_id", "cursos_id"]

            for value in data:
                p.add_row([value["_id"], value["profesor_id"], value["salon_id"], value["cursos_id"]])
            print(p)

        except Exception as e:
            print(e)

    def update_cursos_docente(self):
        try:
            conn = Connection('reformatorio')
            conn.update('cursos_docente', {
                'id': {
                    '$ne': self.id
                }
            }, {
                'profesor_id': self.profesor_id
            })
            print(f'Se modifico el curso')
        except Exception as e:
            print(e)

    def delete_cursos_docente(self):
        try:
            conn = Connection('reformatorio')
            conn.delete('cursos_docente', {
                'profesor_id': {
                    '$gt': self.profesor_id
                }
            })
            print(f'Se elimino el curso.')
        except Exception as e:
            print(e)
