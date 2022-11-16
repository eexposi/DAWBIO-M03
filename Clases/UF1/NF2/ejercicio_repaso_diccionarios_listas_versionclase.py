""" EJERCICIO DE REPASO DE DICCIONARIOS ----------------------------------------------------------------

Mediante el uso de diccionario/s, vamos a gestionar los datos de alumnos y sus notas.
IMPORTANTE: para cada alumno, el sistema debe permitir almacenar un número indeterminado de notas.
diccionario = {"Nombre": [nota1, nota2, ...], "Nombre2": [nota1, nota2, ...], ...}
El programa va a permitir:
    - Añadir alumno: si el alumno no existe, se añadirá el nombre y la primera nota (0..10 con decimales).
      Si ya existe, mostrar mensaje de error y volver a preguntar el nombre de nuevo alumno.
    - Buscar alumno: mostrará las notas del alumno introducido por teclado. Si no existe, mostrar mensaje
      de error y volver a preguntar.
    - Añadir nota: para un alumno introducido por teclado, añadirá una nueva nota.
    - Mostrar media de notas: para un alumno introducido por teclado, mostrará la media de sus notas.
    - Borrar estudiante: borrará al alumno indicado de nuestra base de datos. Si no existe, mostrar mensaje
      de error y volver a preguntar el nombre del alumno a borrar.

NOTA: si nos hemos confundido de opción, introduciremos una "X" cuando nos pida el nombre del alumno. El sistema
volverá al menú principal. El menú se generará con lista o diccionario, no un print por opción.

        Menú de opciones:
            1 - Añadir alumno
            2 - Buscar alumno
            3 - Añadir nota a alumno
            4 - Mostrar la media de notas de alumno
            5 - Borrar un alumno
            0 - Salir
        Introduce opción:
--------------------------------------------------------------------------------------------------- """

menu = ["Salir", "Añadir alumno", "Buscar alumno", "Añadir nota a alumno",
        "Mostrar la media de notas de alumno", "Borrar alumno", "Mostrar toda la información"]

"""
diccionario = {"Nombre": [nota1, nota2, ...], "Nombre2": [nota1, nota2, ...], ...}
"""
diccionario = {}
diccionario = {"Eric": [1, 2, 3], "Javi": [10, 5, 5]}

while True:
    print("---MENU---")
    for i in range(len(menu)):
        print(i, menu[i], sep=" - ")
    seleccion = input("Seleccione la opción: ")

    if seleccion == "0":
        print("Adiós")
        break
    elif seleccion == "1":
        # Añadir alumno
        print("Has seleccionado la opción 1")
        while True:
            nombre_alumno = input("Indica el nombre del alumno a añadir: ")
            if nombre_alumno in diccionario:
                # Mensaje de error y volver a pedir el nombre
                print("El alumno ya existe. Vuelve a intentarlo.")
            else:
                # Añadir usuario y nota
                nota = int(input("Indícame la nota: "))
                diccionario[nombre_alumno] = [nota]
                break
    # print(diccionario)
    elif seleccion == "2":
        # Buscar alumno
        print("Has seleccionado la opción 2")
        while True:
            nombre_alumno = input("Indica el nombre del alumno a buscar: ")
            if nombre_alumno not in diccionario:
                print("El alumno no existe. Vuelve a intentarlo.")
            else:
                """print("Has seleccionado el alumno " + nombre_alumno)
                for i in range(len(diccionario[nombre_alumno])):
                    print(diccionario[nombre_alumno][i])"""
                # print(diccionario[nombre_alumno])
                for e in diccionario[nombre_alumno]:
                    print(e)
                break
    elif seleccion == "3":
        # Añadir nota a alumno
        print("Has seleccionado la opción 3")
        while True:
            nombre_alumno = input("Indica el nombre del alumno a buscar: ")
            if nombre_alumno not in diccionario:
                print("El alumno no existe. Vuelve a intentarlo.")
            else:
                nota = input("Indícame la nota: ")
                diccionario[nombre_alumno].append(nota)
                break
    elif seleccion == "4":
        # Mostrar la media de notas de alumno
        print("Has seleccionado la opción 4")
        while True:
            nombre_alumno = input("Indica el nombre del alumno a buscar: ")
            if nombre_alumno not in diccionario:
                print("El alumno no existe. Vuelve a intentarlo.")
            else:
                media = 0
                for i in diccionario[nombre_alumno]:
                    media += int(i)
                print("La media es: ", media / (len(diccionario[nombre_alumno])))
                break
    elif seleccion == "5":
        # Borrar alumno
        while True:
            nombre_alumno = input("Indica el nombre del alumno a buscar: ")
            if nombre_alumno not in diccionario:
                print("El alumno no existe. Vuelve a intentarlo.")
            else:
                print("Borramos al alumno: ", nombre_alumno)
                del diccionario[nombre_alumno]
                print("Borrado")
                break
    elif seleccion == "6":
        for i in diccionario:
            print("Alumno: ", i)
            print("------------")
            # print(diccionario[i])
            for e in diccionario[i]:
                print(e)
            # for clave in diccionario:
            # print(clave, diccionario[clave])
            print()

        """
        Alumno
        7
        5
        3
        4

        Alumno 2
        2
        4
        5
        2
        """
    else:
        print("Opción incorrecta.")
