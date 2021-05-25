from helpers.routes import *

class Mobile:
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio

class Reformatorio():
    def __init__(self):
        self.view_principal()

    def view_principal(self):
        while True:
            print(''' !!! BIENVENIDO A TU REFORMATORIO FAVORITO !!! 
            ¿Que deseas realizar?
                1) Ver Alumnos
                2) Ver Docentes
                3) Administrar Cursos
                4) Agregar Notas
                5) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.view_alumno()
            if opcion == "2":
                pass
                self.view_profesor()
            if opcion == "3":
                self.view_cursos()
            if opcion == "4":
                self.add_notas()
            else:
                self.salir()

    def view_alumno(self):
        while True:
            print('''
                Escoga una opción:
                1) Crear Nuevo Alumno
                2) Lista de Alumnos por Salón
                3) Modificar Alumno
                4) Eliminar Alumno
                5) Regresar
                6) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.data_insert_alumno()
            elif opcion == "2":
                # self.datos_salon()
                Alumno.all_alumnos("xx")
                sleep(1)
            elif opcion == "3":
                self.data_update_alumno()
            elif opcion == "4":
                self.data_delete_alumnos()
            elif opcion == "5":
                self.view_principal()
            else:
                self.salir()

    def data_insert_alumno(self):
        print(''' INGRESAR DATOS DEL ALUMNO:''')
        print(''' NOMBRES: ''')
        nombres = input("> ")
        print(''' CODIGO: ''')
        codigo_alumno = input("> ")
        print(''' EDAD: ''')
        edad = input("> ")
        print(''' CORREO: ''')
        correo = input("> ")
        print(''' CELULAR: ''')
        celular = input("> ")
        print(''' DNI: ''')
        dni = input("> ")
        print(''' SALON: ''')
        salon_id = input("> ")

        insert = Alumno('', nombres, codigo_alumno, edad, correo, celular, dni, salon_id)
        insert.insert_alumnos()
    
    def choose_alumno(self):
        Alumno.list_all_alumnos("xx")
        print('''ESCOGER ID DE ALUMNOS:''')

    def data_update_alumno(self):
        self.choose_alumno()
        id = input("> ")

        print(''' INGRESAR DATOS DEL ALUMNO:''')
        print(''' NOMBRES: ''')
        nombres = input("> ")
        print(''' CODIGO: ''')
        codigo_alumno = input("> ")
        print(''' EDAD: ''')
        edad = input("> ")
        print(''' CORREO: ''')
        correo = input("> ")
        print(''' CELULAR: ''')
        celular = input("> ")
        print(''' DNI: ''')
        dni = input("> ")
        print(''' SALON: ''')
        salon_id = input("> ")

        update = Alumno(id, nombres, codigo_alumno, edad, correo, celular, dni, salon_id)
        update.update_profesor()

    def data_delete_alumnos(self):
        self.choose_alumno()
        id = input("> ")
        
        delete = Alumno(id)
        delete.delete_alumnos()

        self.choose_cursos()
        id = input("> ")
        
        delete = Cursos(id, '')
        delete.delete_cursos()

    def view_profesor(self):
        while True:
            print('''
                Escoga una opción:
                1) Crear Nuevo Profesor
                2) Lista de Profesores
                3) Profesores por curso
                4) Modificar Profesor
                5) Eliminar Profesor
                6) Regresar
                7) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.data_insert_profesor()
            elif opcion == "2":
                # self.datos_salon()
                Profesor.all_profesores("xx")
                #sleep(1)
                pass
            elif opcion == "3":
                Profesor.list_prof_x_curso("xx")
            elif opcion == "4":
                self.data_update_profesor()
            elif opcion == "5":
                self.data_delete_profesor()
            elif opcion == "6":
                self.view_principal()
            else:
                self.salir()

    def data_insert_profesor(self):
        print(''' INGRESAR DATOS DEL PROFESOR:''')
        print(''' NOMBRES: ''')
        nombre = input("> ")
        print(''' DNI: ''')
        dni = input("> ")
        print(''' EDAD: ''')
        edad = input("> ")
        print(''' CORREO: ''')
        correo = input("> ")
        
        insert = Profesor('', nombre, dni, edad, correo)
        insert.insert_profesores()
    
    def choose_profesor(self):
        Profesor.list_all_profesores("xx")
        print('''ESCOGER ID DEL PROFESOR:''')

    def data_update_profesor(self):
        self.choose_profesor()
        id = input("> ")

        print(''' INGRESAR DATOS DEL PROPFESOR:''')
        print(''' NOMBRES: ''')
        nombre = input("> ")
        print(''' DNI: ''')
        dni = input("> ")       
        print(''' EDAD: ''')
        edad = input("> ")
        print(''' CORREO: ''')
        correo = input("> ")
        print(''' DNI: ''')
        dni = input("> ")

        update = Profesor(id, nombre, dni, edad, correo)
        update.update_profesor()

    def data_delete_profesor(self):
        self.choose_profesor()
        id = input("> ")
        
        delete = Profesor(id)
        delete.delete_profesores()

    def salir(self):
        print(''' \\\ CERRADO ///''')
        exit()



Reformatorio()