# Actividad 1

try:
    letras_dni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L",
                  "C", "K", "E"]

    diccionario = {}

    nombre = input("Nombre: ")
    dni = int(input("DNI: "))

    calculo_letra = dni % 23

    diccionario[nombre] = dni, letras_dni[calculo_letra]

    print("USUARIOS")

    for i in diccionario:
        print(i, "-->", end=" ")
        for j in diccionario[i]:
            print(j, end="")
except ValueError:
    print("El valor introducido no es correcto")

# Actividad 2

try:
    while True:
        n1 = int(input("Número 1: "))
        if n1 == 0:
            break
        else:
            n2 = int(input("Número 2: "))
            division = n1 / n2
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("invalid literal for int() with base 10")

# Actividad 3

import random

juego = [
    ["A", "B", "B", "A"],
    ["A", "A", "A", "B"],
    ["A", "A", "A", "B"],
    ["A", "A", "A", "B"],
]

menu = [
    ["Salir"],
    ["Jugar"]
]

cont = 0
barcos = 0
try:
    for i in range(len(menu)):
        for j in range(len(menu[i])):
            print(i + 1, menu[i][j], sep="-")
        print()

    opcion = int(input("Introduce una opción valida: "))

    if opcion == 1:
        print("Programa terminado")

    elif opcion == 2:
        while True:
            x = random.randint(0, 3)
            y = random.randint(0, 3)

            if juego[x][y] == "X" or juego[x][y] == "T":
                continue
            else:
                if juego[x][y] == "A":
                    juego[x][y] = "X"
                    cont += 1
                elif juego[x][y] == "B":
                    juego[x][y] = "T"
                    cont += 1
                    barcos += 1
                    print("Tocado")
                    print()

                for i in range(len(juego)):
                    for j in range(len(juego[i])):
                        print(juego[i][j], end="")
                    print()

                print("Se dispara en la posicion X: " + str(x) + "y Y: " + str(y))
                print()

                continuar = input("Pulsa ENTER para continuar...")
                print()

                if cont == 6:
                    print("Juego finalizado")
                    print()
                    break

        if barcos == 6:
            print("Has hundido todos los barcos")
        else:
            print("No has hundido todos los barcos")
except ValueError:
    print("El valor introducido no es correcto")
