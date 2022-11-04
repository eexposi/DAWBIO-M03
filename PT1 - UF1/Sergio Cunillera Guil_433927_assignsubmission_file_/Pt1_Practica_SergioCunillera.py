print("\nPT1 - NF1 - DAWBIO1 - M03\n")
print("INSTRUCCIONES:")
print("- No se permitirán prints innecesarios ni dentro de condicionales ni iteraciones, salvo que sean necesarios")
print("- No se podrán crear nuevas listas")
print("- No se permite el uso de metodos o funciones que no se han expuesto en clase")
print("- Se entregará 1 archivo .py en el que se ejecutarán todos los ejercicios. Indicándose cuando se inicia")
print("cada uno de ellos.\n")

# Introduce el numero del ejercicio que quieras ejecutar: 1, 2, 3, 4
lista_ejercicios = []
ejercicio = 0
opcion = 0
while opcion < 1 or opcion > 2:
    print("\nOpcion 1: Seleccionar todos los ejericicios")
    print("Opcion 2: Seleccionar el ejercicio individual\n")
    opcion = int(input("Introduce una opcion de las 2: "))
    if opcion == 1:
        lista_ejercicios.append(1)
        lista_ejercicios.append(2)
        lista_ejercicios.append(3)
        lista_ejercicios.append(4)
    if opcion == 2:
        print("\nLista ejercicios = [1, 2, 3, 4]\n")
        ejercicio = int(input("Introduce el numero del ejercicio que quieras de la lista ejercicios: "))
        lista_ejercicios.append(ejercicio)

print("\n", "-" * 90)

if 1 in lista_ejercicios:
    print("\n\nEJERCICIO 1\n")
    print("Elaborar un programa que realice la conversión de cm. a pulgadas. Donde 1cm = 0.39737 pulgadas.\n")

    centimetros = int(input("Introduce una cantidad de centimetros: "))
    pulgadas = 0.39737
    print("El resultado de la conversión es:", pulgadas * centimetros, "pulgadas.\n")

    print("-" * 90)

if 2 in lista_ejercicios:
    print("\n\nEJERCICIO 2\n")
    print(
        "Obtener la edad de una persona en meses, si se introduce su edad en años y meses. Ejemplo: Introducimos 3 años 4 meses")
    print("debe mostrar: 40 meses.\n")

    años = int(input("Introduce una cantidad de años: "))
    meses = int(input("Introduce una cantidad de meses: "))
    resultado = (12 * años) + meses
    print("\n", resultado, "meses.\n")

    print("-" * 90)

if 3 in lista_ejercicios:
    print("\n\nEJERCICIO 3\n")
    print(
        "Los alumnos de 1º de DAWBIO realizaran un viaje a Port Aventura a final de curso, el precio de la entrada general es de 45€.")
    print("Al grupo se le aplicará un descuento dependiendo del número de alumnos:")
    print("    • Si alumnos > 50 --> 30%")
    print("    • Si alumnos entre 20  y 50 --> 20%")
    print("    • Si alumnos entre 10 y 20 € --> 10%")
    print("    • Si alumnos es <  10 € --> 0%")
    print("    • Profesor de programación --> entrada libre.")
    print("")
    print("Se realizará un descuento adicional del 15% a los alumnos menores de 18 años. La cantidad de alumnos")
    print("menores del grupo se ha de indicar para obtener el precio final.")
    print("")
    print(
        "El programa mostrará el importe total a pagar para los mayores de edad, el importe a pagar para los menores de edad y ")
    print("el importe total del grupo.\n")

    cantidad_alumnos = int(input("Introduce una cantidad de alumnos: "))
    grupo_alumnos = 0
    precio_mayores = 0
    precio_menores = 0
    while cantidad_alumnos != grupo_alumnos:
        grupo_alumnos += 1
        alumno = int(input("Introduce la edad de un alumno: "))
        if alumno > 50:
            precio_mayores += 45 - (45) * 0.30
        if alumno <= 50 and alumno >= 20:
            precio_mayores += 45 - (45) * 0.20
        if alumno < 20 and alumno >= 10:
            if alumno < 20 and alumno >= 18:
                precio_mayores += 45 - (45) * 0.10
            if alumno < 18 and alumno >= 10:
                precio_menores += 45 - (45) * 0.25
        if alumno < 10:
            precio_menores += 45 - (45) * 0.15
    precio_final = precio_mayores + precio_menores
    print("\nEl importe de los mayores de edad es:", precio_mayores)
    print("El importe de los menores de edad es:", precio_menores)
    print("El importe final del grupo es:", precio_final, "\n")

    print("-" * 90)

if 4 in lista_ejercicios:
    print("\n\nEJERCICIO 4\n")
    print("Dadas las listas:")
    print(
        "lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,")
    print(
        "        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,")
    print("        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]")
    print(
        "lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,")
    print(
        "        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,")
    print("        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]")
    print("")
    print("4.1 - Compararemos ambas listas, mostrando por pantalla cuál de las 2 es mas larga.")
    print("4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.")
    print(
        "4.3 - Recorreremos la lista 1 y compararemos cada elemento de la lista, con el que tenga la misma posición de la otra.")
    print("      Indicando que lista posee el elemento con un valor más pequeño.")
    print(
        "4.4 - Ordenaremos ambas listas de la misma forma y las mostraremos una de mayor a menor y la otra al revés de forma")
    print("      invertida.\n")

    lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0,
            2,
            0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5,
            3,
            5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
    lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7,
            2,
            5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9,
            10, 2,
            0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]

    print("-" * 90)

    print("\n4.1 - Compararemos ambas listas, mostrando por pantalla cuál de las 2 es mas larga.\n")

    if len(lst1) > len(lst2):
        print("La lista 1 es más grande que la lista 2\n")
    else:
        print("La lista 2 es más grande que la lista 1\n")

    print("-" * 90)

    print("\n\n4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.\n")

    # saber la media con las dos listas.
    resultado_lista1 = 0
    for r in range(0, len(lst1)):
        resultado_lista1 += lst1[r]
    print("La media de la lista 1 es:", resultado_lista1 // len(lst1))

    resultado_lista2 = 0
    for t in range(0, len(lst2)):
        resultado_lista2 += lst2[t]
    print("La media de la lista 2 es:", resultado_lista2 // len(lst2), "\n")

    print("-" * 90)

    print(
        "\n4.3 - Recorreremos la lista 1 y compararemos cada elemento de la lista, con el que tenga la misma posición de la otra.")
    print("Indicando que lista posee el elemento con un valor más pequeño.\n")

    # comparar valores de la lista 2 con la lista 1
    for t in range(0, len(lst1) - 1):
        if lst1[t] > lst2[t]:
            print("El valor:", lst1[t], "de la lista 1, es más grande que:", lst2[t], "de la lista 2")

    print("\n", "-" * 90)

    print(
        "\n\n4.4 - Ordenaremos ambas listas de la misma forma y las mostraremos una de mayor a menor y la otra al revés de forma invertida.")

    # Ordenar la lista 1
    for r in range(1, len(lst1)):
        for n in range(len(lst1) - r):
            if lst1[n] > lst1[n + 1]:
                aux = lst1[n]
                lst1[n] = lst1[n + 1]
                lst1[n + 1] = aux
    print("\nLista 1 ordenada de menor a mayor", "\n", lst1)

    # Ordenar la lista 2
    for r in range(1, len(lst2)):
        for n in range(len(lst2) - r):
            if lst2[n] > lst2[n - 1]:
                aux = lst2[n]
                lst2[n] = lst2[n - 1]
                lst2[n - 1] = aux
    a = len(lst2) - 1
    ax = lst2[a]
    lst2.pop(a)
    lst2.insert(0, ax)
    print("\nLista 2 ordenada de mayor a menor", "\n", lst2, "\n")

    print("-" * 90)
