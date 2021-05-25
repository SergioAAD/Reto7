from helpers.routes import *

class Alumno:
    def __init__(self, id="", nombres="", codigo_alumno="", edad="", correo="", celular="", dni="", salon_id=""):
        self.id = id
        self.nombres = nombres
        self.codigo_alumno = codigo_alumno
        self.edad = edad
        self.correo = correo
        self.celular = celular
        self.dni = dni
        self.salon_id = salon_id

    def create_table(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS alumnos(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombres character varying(50) NOT NULL,
                    codigo_alumno integer NOT NULL,
                    edad character varying(2) NOT NULL,
                    correo character varying(35) NOT NULL,
                    celular character varying(9) NOT NULL,
                    dni character varying(8) NOT NULL,
                    salon_id integer NOT NULL,
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)

    def all_alumnos(self):
        try:
            conn = Connection('reformatorio')
            data = conn.get_all('alumnos')

            p = PrettyTable()
            print("-- LISTA DE ALUMNOS --".center(80))
            p.field_names = ["ID", "Nombres", "Código", "Edad", "Correo", "Celular", "Dni", "Salon_id"]

            for alumnos_alls in data:
                p.add_row([alumnos_alls["_id"], alumnos_alls["nombres"], alumnos_alls["codigo_alumno"], alumnos_alls["edad"], alumnos_alls["correo"], alumnos_alls["celular"], alumnos_alls["dni"], alumnos_alls["salon_id"]])
            print(p)
        except Exception as e:
            print(e)
    
    def list_all_alumnos(self):
        try:
            conn = Connection('reformatorio')
            data = conn.get_all('alumnos')

            p = PrettyTable()
            print("-- LISTA DE ALUMNOS --".center(80))
            p.field_names = ["ID", "Nombres"]

            for alumnos_alls in data:
                p.add_row([alumnos_alls["_id"], alumnos_alls["nombres"]])
            print(p)

        except Exception as e:
            print(e)

    def insert_alumnos(self):
        try:
            conn = Connection('reformatorio')
            conn.insert('alumnos', {
                'nombres': self.nombres,
                'codigo_alumno': self.codigo_alumno,
                'edad': self.edad,
                'correo': self.correo,
                'celular': self.celular,
                'dni': self.dni,
                'salon_id': self.salon_id
            })
            print(f'Se registro el alumno')
        except Exception as e:
            print(e)

    def update_alumnos(self):
        try:
            conn = Connection('alumnos')
            conn.update({
                'id': self.id
            }, {
                'nombres': self.nombres,
                'codigo_alumno': self.codigo_alumno,
                'edad': self.edad,
                'correo': self.correo,
                'celular': self.celular,
                'dni': self.dni,
                'salon_id': self.salon_id
            })
            print(f'Se modifico el usuario: {self.nombres} con DNI: {self.dni}')
        except Exception as e:
            print(e)
    
    def delete_alumnos(self):
        try:
            conn = Connection('reformatorio')
            conn.delete('alumnos', {
                'nombres': {
                    '$gt': self.nombres
                }
            })
            print(f'Se elimino el usuario.')
        except Exception as e:
            print(e)
