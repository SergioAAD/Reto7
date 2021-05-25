from helpers.routes import *

conn = Connection('reformatorio')
records = conn.get_all('profesores', {}, {'nombre':1})
print(list(records))
p = PrettyTable()
print("-- LISTA DE PROFESORES --".center(50))
p.field_names = ["ID", "nombre", "Dni", "Edad", "Correo"]

for record in records:
     p.add_row([record[0], record[1], record[2], record[3], record[4]])
print(p)