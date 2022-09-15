"""
EJERCICIO 1
Pediremos al usuario:
    - Nombre
    - Apellido
    - Edad
    - Grupo
    - Asignatura
Mostraremos por pantalla con un print() la información completa, indicando que es cada elemento
Crearemos una variable en la que concatenaremos la informacion e indicaciones de cada elemento. Mostrandola
______________________________
"""
# PEDIMOS LA INFORMACION  AL USUARIO
# nombre: str = input("Indique su nombre: ")
# apellido: str = input("Indique su apellido: ")
# edad: int = int(input("Indique su edad: "))
# grupo: str = input("Indique su grupo: ")
# asignatura: str = input("Indique su asignatura: ")
#
# print("Mostramos la informacion en un print:")
# print("Me llamo " + nombre + " " + apellido + ", tengo " + str(edad) + " años. Estoy cursando "
#       + asignatura + " en el grupo" + grupo + ".")
# resultado = "Me llamo " + nombre + " " + apellido + ", tengo " + str(edad) + " años. Estoy cursando " \
#             + asignatura + " en el grupo" + grupo + "."
# print("Mostramos la informacion desde la variable")
# print(resultado)

"""
EJERCICIO 2
Pediremos al usuario 2 numeros con input()
Realizaremos las operaciones: +, -, *, /, % y guardaremos el resultado en variables
Printaremos el resultado y la operacion de cada una de ellas
______________________________
"""

# Pedimos la información
n1: int = int(input("Numero 1: "))
n2: int = int(input("Numero 2: "))

suma: int = n1 + n2
resta: int = n1 - n2
division: int = n1 / n2
multi: int = n1 * n2
modulo: int = n1 % n2

print("El resultado de la suma de " + str(n1) + " y de " + str(n2) + " es de: " + str(suma))
print("El resultado de la resta de " + str(n1) + " y de " + str(n2) + " es de: " + str(resta))
print("El resultado de la division de " + str(n1) + " y de " + str(n2) + " es de: " + str(division))
print("El resultado de la multiplicacion de " + str(n1) + " y de " + str(n2) + " es de: " + str(multi))
print("El resultado del modulo de " + str(n1) + " y de " + str(n2) + " es de: " + str(modulo))
