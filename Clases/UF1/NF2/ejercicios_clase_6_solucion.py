""" EJERCICIO 1 ----------------------------------------------------------------------"""
Lista = ["almacenar", 8, "a", [1, 2, 3], True, (0, 0, 1), 85.7]

# a)
Lista_comprobar = [85.7, 0, True, [True], [(0, 0, 1)], 85, "a", [1, 2, 3]]
for e in Lista_comprobar:
    if e in Lista:
        print("El elemento " + str(e) + " esta en la lista")
print()

# b)
print("La posicion del elemento (0,0,1) es " + str(Lista.index((0, 0, 1))))
print()

# c)
Lista.remove(Lista[len(Lista) - 1])  # Tambien puede hacerse """ del L[len(L)-1] """
print(Lista)
print()

# d)
print("El string 'a' aparece " + str(Lista.count("a")) + " vez/veces")
print()

""" EJERCICIO 2 ----------------------------------------------------------------------"""
# 2.1) Solicitar al usuario que introduzca números, los cuales se guardarán en una lista.
# Finalizar al introducir el número 0, el cual no debe guardarse.
print("2.1")
numeros = []
num = int(input("Introduce un numero: "))
while num != 0:
    numeros.append(num)
    num = int(input("Introduce un numero: "))
print()

# 2.2) A continuación, solicitar al usuario que introduzca un número y, si el número está en la lista,
# eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar (no existe)
print("2.2")
encontrado = False
while encontrado == False:
    eliminar = int(input("Introduce un numero a eliminar: "))
    if eliminar in numeros:
        encontrado = True
        numeros.remove(eliminar)
    else:
        print("El número introducido no esta en la lista.")
print()

# 2.3) Imprimir la SUMA de todos los números de la lista.
print("2.3")
suma = 0
for e in numeros:
    suma = suma + e
print("la SUMA total de los numeros es " + str(suma))
print()

# 2.4) Solicitar al usuario otro número y crear una lista con los elementos de la lista original
# que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
lista_limitada = []
limite = int(input("Filtramos numeros menores a: "))
for e in numeros:
    if e < limite:
        lista_limitada.append(e)

for e in lista_limitada:
    print(e)

# 2.5) Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta
# por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo,
# si la lista original es [4,7,12,83,7,7,12,4], la nueva lista contendrá: [(4,2), (7,3), (12,2), (83,1)]
nueva_lista = []
for e in numeros:
    if (e, numeros.count(e)) not in nueva_lista:
        nueva_lista.append((e, numeros.count(e)))  # OJO con los paréntesis, entender porqué
print(nueva_lista)

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
        print("Opción incorrecta