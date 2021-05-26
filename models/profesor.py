from helpers.routes import *

class Profesor:
    def __init__(self,id, nombre, dni, edad, correo):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.correo = correo

    def all_profesores(self):
        try:
            conn = Connection('reformatorio')
            data = conn.get_all('profesores')
            
            p = PrettyTable()
            print("-- LISTA DE PROFESORES --".center(50))
            p.field_names = ["ID", "Nombres", "Dni", "Edad", "Correo"]

            for record in data:
                p.add_row([record["_id"], record["nombre"], record["dni"], record["edad"], record["correo"]])
            print(p)
        except Exception as e:
            print(e)

    def list_all_profesores(self):
        try:
            conn = Connection('reformatorio')
            data = conn.get_all('profesores')
            
            p = PrettyTable()
            print("-- LISTA DE PROFESORES --".center(50))
            p.field_names = ["ID", "Nombres"]

            for record in data:
                p.add_row([record["_id"], record["nombre"]])
            print(p)

        except Exception as e:
            print(e)
    
    def list_prof_x_curso(self):
        try:
            conn = Connection('profesor')
            records = conn.select_inner()
            p = PrettyTable()
            print("-- PROFESORES / CURSOS --".center(40))
            p.field_names = ["DNI", "Nombres del Profesor", "Curso"]

            for record in records:
                p.add_row([record[0], record[1], record[2]])
            print(p)

        except Exception as e:
            print(e)

    def insert_profesores(self):
        try:
            conn = Connection('reformatorio')
            conn.insert('profesores', {
                'nombre': self.nombre,
                'dni': self.dni,
                'edad': self.edad,
                'correo': self.correo
            })
            print(f'Se registro el profesor: {self.nombre} con el dni {self.dni}, edad: {self.edad} y correo {self.correo}')
        except Exception as e:
            print(e)
   
    def update_profesor(self):
        try:
            conn = Connection('reformatorio')
            conn.update('profesores', {
                'id': {
                    '$ne': self.id
                }
            }, {
                'nombre': self.nombre,
                'dni': self.dni,
                'edad': self.edad,
                'correo': self.correo
            })
            print(f'Se modifico el alumno')
        except Exception as e:
            print(e)
    
    def delete_profesores(self):
        try:
            conn = Connection('profesor')
            conn.delete({
                'id': self.id
            })
            print(f'Se elimino el usuario.')
        except Exception as e:
            print(e)
