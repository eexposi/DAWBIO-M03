import random

""" EJERCICIO 1 ----------------------------------------------------------------------"""
# Mediante la siguiente matriz, generar un menú de opciones:

menu = [[1, "Opcion 1"], [2, "Opcion 2"], [3, "Opcion 3"], [4, "Salir"]]

for i in range(len(menu)):
    for j in range(len(menu[i])):
        print(menu[i][j], end="-")
    print()

""" EJERCICIO 1.2 ----------------------------------------------------------------------"""
# Añadir una opción más al menú, pidiendo los datos por pantalla:

num = input("numero: ")
opt = input("opción: ")
elemento4 = [num, opt]
menu.append(elemento4)

for i in range(len(menu)):
    for j in range(len(menu[i])):
        print(menu[i][j], end="-")
    print()

""" EJERCICIO 2 ----------------------------------------------------------------------"""
# --- Menú ---
# 0 - Salir
# 1 - Jugar         # Otras opciones deben dar error y volver a mostrar el menú

# Crear manualmente una matriz tipo:
#    O   O   O
#    O   O   O
#    O   O   O

# Si elegimos la opción 1, nos pedirá 2 números independientes, es decir, 2 input (fila y columna). No aceptaremos posiciones incorrectas, volviendo a pedir el dato.
# Si la (fila,columna) contiene una 'O' --> cambiaremos la 'O' por 'X' y mostraremos la matriz con la nueva 'X'
# Cuando todas las posiciones de la matriz tengan 'X' --> mensaje de "WINNER"

menu = [[0, "Salir"], [1, "Jugar"]]
matriz = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
winner = 0
opt = 5
while opt != 0:
    correcto = False
    correcto2 = False
    if winner < 9:
        for i in range(len(menu)):
            for j in range(len(menu[i])):
                print(menu[i][j], end="-")
            print()
        opt = int(input("Opción: "))

        if opt == 1:
            while correcto == False:
                fila = int(input("Indícame número de fila: "))
                if fila < 0 or fila > 2:
                    print("Error. Pásame una fila correcta: ")
                else:
                    correcto = True

            while correcto2 == False:
                columna = int(input("Indícame número de columna: "))
                if columna < 0 or columna > 2:
                    print("Error. Pásame una columna correcta: ")
                else:
                    correcto2 = True

            if matriz[fila][columna] == "O":
                matriz[fila][columna] = "X"
                winner += 1
            else:
                print("Aquí ya hay una 'X'")
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    print(matriz[i][j], end=" ")
                print()
        elif opt != 0:
            print("Opción incorrecta!")
    else:
        print("You are the winner!")
        break

""" EJERCICIO 2.2 --------------------------------------------------------------------"""
# Modifica el ejercicio 2.1 para que el sistema "juegue" de manera autónoma, es decir, sin pedirle
# valores de fila o columna al usuario.

menu = [[0, "Salir"], [1, "Jugar"]]
matriz = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
winner = 0
opt = 5
while opt != 0:
    correcto = False
    correcto2 = False
    if winner < 9:
        for i in range(len(menu)):
            for j in range(len(menu[i])):
                print(menu[i][j], end="-")
            print()
        input("Pulsa para continuar... ")

        while correcto == False:
            fila = random.randint(0, 2)
            correcto = True

        while correcto2 == False:
            columna = random.randint(0, 2)
            correcto2 = True

        if matriz[fila][columna] == "O":
            matriz[fila][columna] = "X"
            winner += 1
        else:
            print("Aquí ya hay una 'X'")
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                print(matriz[i][j], end=" ")
            print()
    else:
        print("You are the winner!")
        break

""" EJERCICIO 3 ----------------------------------------------------------------------"""
# Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas
# con la siguiente forma: (nombre, DNI, destino). Ejemplo:
# [("Javier Carrasco", 39727461, "Tarragona"), ("Eric Exposito", 47766297, "Paris")]

# Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen.
# Ejemplo: [("Tarragona","Espanya"), ("Paris","Francia")]

# Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
#     3.1) Agregar pasajeros a la lista de viajeros
#     3.2) Agregar ciudades a la lista de ciudades
#     3.3) Dado el DNI de un pasajero, ver a qué ciudad viaja
#     3.4) Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad
#     3.5) Dado el DNI de un pasajero, ver a qué país viaja
#     3.6) Dado un país, mostrar cuántos pasajeros viajan a ese país
#     3.7) Salir del programa

pasajeros = []
ciudades = []

while True:
    num_pasajeros = 0

    print()
    print("   1. Agregar pasajeros")
    print("   2. Agregar ciudades")
    print("   3. Buscar ciudad de destino mediante el DNI")
    print("   4. Cantidad de pasajeros que viajan a una ciudad")
    print("   5. Buscar pais de destino mediante el DNI")
    print("   6. Cantidad de pasajeros que viajan a un pais")
    print("   7. Salir del programa")
    menu = int(input("   Selecciona la opción: "))

    if menu == 1:
        print()
        print("AÑADIR PASAJEROS (X para salir): ")
        nombre = input("Introduce nombre: ")
        while nombre != "X":
            dni = input("Introduce DNI: ")
            destino = input("Introduce destino: ")
            pasajeros.append((nombre, dni, destino))
            nombre = input("Introduce nombre: ")

    elif menu == 2:
        print("AÑADIR CIUDADES (X para salir):")
        ciudad = input("Introduce ciudad: ")
        while ciudad != "X":
            pais = input("Introduce pais: ")
            ciudades.append((ciudad, pais))
            ciudad = input("Introduce ciudad: ")

    elif menu == 3:
        print("BUSCAR CIUDAD:")
        dni = input("Introduce el DNI del pasajero: ")
        for viaje in pasajeros:
            if viaje[1] == dni:
                print("La ciudad destino es " + viaje[2])

    elif menu == 4:
        print("CANTIDAD DE PASAJEROS A CIUDAD:")
        ciudad = input("Introduce la ciudad a buscar: ")
        for viaje in pasajeros:
            if viaje[2] == ciudad:
                num_pasajeros += 1
        print("Viajan " + str(num_pasajeros) + " pasajeros a " + ciudad)

    elif menu == 5:
        print("BUSCAR PAIS:")
        dni = input("Introduce el DNI del pasajero: ")
        for viaje in pasajeros:
            if viaje[1] == dni:
                for ciudad in ciudades:
                    if viaje[2] == ciudad[0]:
                        print("El pais de destino es " + ciudad[1])

    elif menu == 6:
        print("CANTIDAD DE PASAJEROS A PAIS:")
        pais_destino = input("Introduce el pais de destino: ")
        for pais in ciudades:
            if pais[1] == pais_destino:
                for viaje in pasajeros:
                    if pais[0] == viaje[2]:
                        num_pasajeros += 1
        print("Viajan " + str(num_pasajeros) + " pasajeros a " + pais_destino)

    elif menu == 7:
        print("¡ADIOS!")
        break

    else:
        print("Opción incorrecta.")
