# Clase 14: Repaso de métodos + try/except - 16/12/22
#
"""
	No se permitirán prints innecesarios ni dentro de condicionales ni iteraciones, salvo que sean necesarios
	No se permite el uso de métodos o funciones que no se han expuesto en clase
	Se entregarán tanto archivos como ejercicios tenga la prueba
	No se evaluará código comentado
	La entrega fuera de plazo equivaldrá a un 0
	No se valorarán métodos/funciones de + 10 líneas.
	El programa principal podrá tener también un máximo de 10 líneas. Con excepción de encadenamientos de elif,
	que no contarán para este limite
	Controlar los errores que se puedan producir FUERA de los métodos/funciones. El programa NO puede fallar.
	Todos los métodos deberán estar comentados como se expuso en clase:


def ejemplo(str):
'''
Esta función no hace nada
:param str: es un string que conforma una palabra para nada
:return: el 1, porque funciona
'''
print("esto no hace nada")
return 1

"""

""" EJERCICIO DNI  -----------------------------------------------------------------------------------------------------
- Pedir al usuario su nombre y su DNI sin letra.
- Mostrar todos los datos en forma de tabla.
- Que el programa nos pida cuantos DNI queremos añadir
-
                    Usuarios
                    ---------
                    Nombre --> XXXXXXXX-X

Las letras son: TRWAGMYFPDXBNJZSQVHLCKE
Y las letras se relacionan del 0 al 22:
0 = T
1 = R
2 = W
etc...
---------------------------------------------------------------------------------------------------------------------"""

""" EJERCICIO DICCIONARIOS ---------------------------------------------------------------------------------------------
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
---------------------------------------------------------------------------------------------------------------------"""
