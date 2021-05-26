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
                5) Agregar Grado
                6) Agregar Nivel
                7) Agregar Periodo
                8) Salir\n
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
            if opcion == "5":
                self.view_grado()
            if opcion == "6":
                self.view_nivel()
            if opcion == "7":
                self.view_periodo()
            else:
                self.salir()

# ALUMNO

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
        print('''ESCRIBIR NOMBRE DE ALUMNO PAR ELIMINAR:''')

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
        update.update_alumnos()

    def data_delete_alumnos(self):
        self.choose_alumno()
        nombres = input("> ")
        
        delete = Alumno(nombres)
        delete.delete_alumnos()

        self.choose_cursos()
        id = input("> ")
        
        delete = Cursos(id, '')
        delete.delete_cursos()

# PROFESOR

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

# CURSOS

    def choose_cursos(self):
        Cursos.all_cursos("xx")
        print('''ESCRIBIR EL ID DEL CURSO A MODIFICAR:''')
    
    def view_cursos(self):
        while True:
            print('''
                Escoga una opción:
                1) Crear Nuevo
                2) Agregar Profesores por curso
                3) Modificar Curso
                4) Eliminar Curso
                5) Regresar
                6) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.add_cursos()
            elif opcion == "2":
                self.data_cursos_profesor()
            elif opcion == "3":
                self.data_update_cursos()
            elif opcion == "4":
                self.data_delete_cursos()
            elif opcion == "5":
                self.view_principal()
            else:
                self.salir()

    def add_cursos(self):
        print(''' INGRESAR NUEVO CURSO:''')
        nombre = input("> ")
        
        insert = Cursos('', nombre)
        insert.insert_cursos()    

    def data_update_cursos(self):
        self.choose_cursos()
        id = input("> ")

        print(''' INGRESAR EL NUEVO NOMBRE DEL CURSO:''')
        nombre = input("> ")

        update = Cursos(id, nombre)
        update.update_cursos()

    def data_delete_cursos(self):
        self.choose_cursos()
        id = input("> ")
        
        delete = Cursos(id, '')
        delete.delete_cursos()

# GRADO

    def choose_grado(self):
        Grado.all_grado("xx")
        print('''ESCRIBIR EL ID DEL GRADO A MODIFICAR:''')
    
    def view_grado(self):
        while True:
            print('''
                Escoga una opción:
                1) Crear Nuevo
                2) Modificar Curso
                3) Eliminar Curso
                4) Regresar
                5) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.add_grado()
            elif opcion == "2":
                self.data_update_grado()
            elif opcion == "3":
                self.data_delete_grado()
            elif opcion == "4":
                self.view_principal()
            else:
                self.salir()

    def add_grado(self):
        print(''' INGRESAR NUEVO GRADO:''')
        nombre = input("> ")
        
        insert = Grado('', nombre)
        insert.insert_grado()    

    def data_update_grado(self):
        self.choose_grado()
        id = input("> ")

        print(''' INGRESAR EL NUEVO NOMBRE DEL GRADO:''')
        nombre = input("> ")

        update = Grado(id, nombre)
        update.update_grado()

    def data_delete_grado(self):
        self.choose_grado()
        id = input("> ")
        
        delete = Grado(id, '')
        delete.delete_grado()

# NIVEL

    def choose_nivel(self):
        Nivel.all_nivel("xx")
        print('''ESCRIBIR EL ID DEL NIVEL A MODIFICAR:''')
    
    def view_nivel(self):
        while True:
            print('''
                Escoga una opción:
                1) Crear Nuevo
                2) Modificar Curso
                3) Eliminar Curso
                4) Regresar
                5) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.add_nivel()
            elif opcion == "2":
                self.data_update_nivel()
            elif opcion == "3":
                self.data_delete_nivel()
            elif opcion == "4":
                self.view_principal()
            else:
                self.salir()

    def add_nivel(self):
        print(''' INGRESAR NUEVO nivel:''')
        nombre = input("> ")
        
        insert = Nivel('', nombre)
        insert.insert_nivel()    

    def data_update_nivel(self):
        self.choose_nivel()
        id = input("> ")

        print(''' INGRESAR EL NUEVO NOMBRE DEL nivel:''')
        nombre = input("> ")

        update = Nivel(id, nombre)
        update.update_nivel()

    def data_delete_nivel(self):
        self.choose_nivel()
        id = input("> ")
        
        delete = Nivel(id, '')
        delete.delete_nivel()


    def salir(self):
        print(''' \\\ CERRADO ///''')
        exit()

# PERIODO

    def choose_periodo(self):
        Periodo.all_periodo("xx")
        print('''ESCRIBIR EL ID DEL PERIODO A MODIFICAR:''')
    
    def view_periodo(self):
        while True:
            print('''
                Escoga una opción:
                1) Crear Nuevo
                2) Modificar Curso
                3) Eliminar Curso
                4) Regresar
                5) Salir\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.add_periodo()
            elif opcion == "2":
                self.data_update_periodo()
            elif opcion == "3":
                self.data_delete_periodo()
            elif opcion == "4":
                self.view_principal()
            else:
                self.salir()

    def add_periodo(self):
        print(''' INGRESAR NUEVO PERIODO:''')
        nombre = input("> ")

        print(''' INGRESAR AÑO:''')
        ano = input("> ")
        
        insert = Periodo('', nombre, ano)
        insert.insert_periodo()    

    def data_update_periodo(self):
        self.choose_periodo()
        id = input("> ")

        print(''' INGRESAR EL NUEVO NOMBRE DEL PERIODO:''')
        nombre = input("> ")

        print(''' INGRESAR AÑO:''')
        ano = input("> ")

        update = Periodo(id, nombre, ano)
        update.update_periodo()

    def data_delete_periodo(self):
        self.choose_periodo()
        id = input("> ")
        
        delete = Periodo(id, '', )
        delete.delete_periodo()


    def salir(self):
        print(''' \\\ CERRADO ///''')
        exit()


Reformatorio()