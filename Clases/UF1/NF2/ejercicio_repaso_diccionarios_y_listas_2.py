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

opciones = {'1':'Añadir alumno','2':'Buscar alumno','3':'Añadir nota a alumno','4':'Mostrar la media de notas de alumno','5':'Borrar un alumno','0':'Salir'}
diccionario = {}

while True:
    print("Menú de opciones:")
    for n, opcion in opciones.items():
        print("  ",n, " - ",opcion)
    opt=int(input("Introduce opción: "))

    if opt==1:
        alumno=input("Indícame el nombre del alumno: ")             # Añadir alumno y nota
        if len(diccionario) == 0:
            nota=int(input("Introduce una nota para " + alumno + ": "))
            diccionario[alumno]=nota
            print(diccionario)
        else:
            if alumno in diccionario:
                print("El alumno ya está dado de alta.")
            else:
                nota=int(input("Introduce una nota para " + alumno + ": "))
                diccionario[alumno]=nota
                print(diccionario)
    elif opt == 2:
        print() # Buscar alumno y mostrar sus notas
    elif opt == 3:
        print() # Añadir nota a un alumno
    elif opt == 4:
        print() # Mostrar la media de notas de un alumno
    elif opt == 5:
        print() # Borrar alumno
    elif opt == 0:
        break
    else:
        print("Opción incorrecta! ")

