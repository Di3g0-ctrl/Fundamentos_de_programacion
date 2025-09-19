#Van a crear una lista vacia con su nombre y van a agregar 5 elementos con input:
#(Nombre, preparatoria, lugar de residencia, edad, carrera)

Lista_DatoA = []

print(" Datos ")

Dato1 = input(" Escribe tu nombre: ")
Lista_DatoA.append(Dato1)

Dato2 = input(" Escribe el nombre de tu preparatoria: ")
Lista_DatoA.append(Dato2)

Dato3 = input(" Escribe tu lugar de residencia: ")
Lista_DatoA.append(Dato3)

Dato4 = input(" Escribe tu edad: ")
Lista_DatoA.append(Dato4)

Dato5 = input(" Escribe el nombre de tu carrera: ")
Lista_DatoA.append(Dato5)

print("\n Tu lista de compras es: ")
for Dato in Lista_DatoA:
	print(f"- {Dato}")

print("\n Tus datos cargaron correctamente")