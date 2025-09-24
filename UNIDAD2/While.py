def mostrar_menu() -> None:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1) Saludar")
    print("2) Calcular la suma de dos números")
    print("3) Mostrar la tabla de multiplicar del 5")
    print("0) Salir")
    

def opcion_saludar() -> None:
    Nombre = input("¿Cómo te llamas? ").strip()
    print(f"¡Hola, {Nombre}! Bienvenido/a.")


def opcion_suma() -> None:
    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(f"La suma es: {a + b}")
    except ValueError:
        print(" Debes introducir valores numéricos.")

#Esta de aqui impirme una lista con la tabla del 5
def opcion_tabla() -> None:
    Numero = 5
    print(f"\nTabla del {Numero}:")
    for i in range(1, 11):
        print(f"{Numero} × {i} = {Numero * i}")
4
"""#La variable continuar es la condifcion que se debe de cumplir, El if hace que si se elige la opcion 1, se ejecutara la opcion 1, 
elfi funciona como un sino y 
sirve como alternativa para que se ejecuten opciones alternas, else funciona como una cancelacion,
"""
# ---------- Bucle principal ----------
Continuar = True              
while Continuar:
    mostrar_menu()             
    Eleccion = input("Elige una opción: ").strip()

    if Eleccion == "1":
        opcion_saludar()
    elif Eleccion == "2":
        opcion_suma()
    elif Eleccion == "3":
        opcion_tabla()
    elif Eleccion == "0":
        print("\n ¡Hasta luego!")
        Continuar = False
    else:
        print(" Opción no válida, intenta de nuevo.")

print("Programa terminado.")