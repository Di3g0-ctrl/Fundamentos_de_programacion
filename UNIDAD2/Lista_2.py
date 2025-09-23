#Se crea una lista llamda lista_compras
lista_compras = []

print("🛒 Lista de Compras 🛒")

#Agregar producto
producto1 = input(" Agregar el primer producto: ")
lista_compras.append(producto1)

#Agregar producto
producto2 = input(" Agregar el segundo producto: ")
lista_compras.append(producto2)

producto3 = input(" Agregar el tercer producto: ")
lista_compras.append(producto3)

print("\n Tu lista de compras es: ")
for producto in lista_compras:
    print(f"- {producto}")

print("\n ¡Lista creada con exito!")