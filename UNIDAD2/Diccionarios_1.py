#Abajo a la variable se le asigna como valor un diccionario y dentro de este los datos que lleva 
Edades = {
    "Brayan": 25,
    "Luis": 30,
    "José": 22
}
#Imprime la edad de Luis
print("Edad de Luis:", Edades["Luis"]) 
#Imprime la edad y nombre de Pedro
Edades["Pedro"] = 28
print("\nDespués de añadir a Pedro:")
print(Edades)                               
#Imprime imprime la edad actualizado y nombre de Luis
Edades["Luis"] = 26
print("\nDespués de actualizar la edad de Luis:")
print(Edades)                              
#Elimina el dato de Jose para luego imprimir las edades
del Edades["José"]
print("\nDespués de eliminar a José:")
print(Edades)                               
#Imprime el diccionario, donde muestra el nombre, edad
print("\nRecorriendo el diccionario:")
for Nombre, Edad in Edades.items():         
    print(f"{Nombre} tiene {Edad} años")