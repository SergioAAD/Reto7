from helpers.routes import *

conn = Connection('reformatorio')
records = conn.get_all('profesores')
print(list(records))
p = PrettyTable()
print("-- LISTA DE PROFESORES --".center(50))
p.field_names = ["ID", "nombre", "Dni", "Edad", "Correo"]

for record in records:
    p.add_row([record["_id"], record["nombre"], record["dni"], record["edad"], record["correo"]])
print(p)

