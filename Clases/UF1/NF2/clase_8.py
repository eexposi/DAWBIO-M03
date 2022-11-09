""" CLASE 8 (08/11/22) - GESTIÓN DE ERRORES ----------------------------------------------------------------------
# Errores en los datos  VS  Errores en el código (sintaxis)
----------------------------------------------------------------------------------------------------"""

# CUANDO EL DATO NO ES CORRECTO:
# value = int(input('Ingresa un número natural: '))
# print("El recíproco de", value, "es", 1 / value)

# SI INTRODUCIMOS UN VALOR NO INT...
""" Traceback (most recent call last):
  File "code.py", line 1, in 
    value = int(input('Ingresa un número natural: '))
ValueError: invalid literal for int() with base 10: ''          <-- ValueError
"""
# SI INTRODUCIMOS EL VALOR 0...
""" Traceback (most recent call last):
  File "main.py", line 2, in <module>
    print("El recíproco de", value, "es", 1/value)
ZeroDivisionError: division by zero                             <-- ZeroDivisionError
"""

# PODEMOS INTENTAR EVITAR EL ERROR, PERO PYTHON NO RECOMIENDA TRABAJAR ASÍ...
# salida = False
# while salida == False:
#     value = int(input('Ingresa un número natural: '))
#     if type(value) is int:
#         print("El recíproco de", value, "es", 1 / value)
#         salida = True
#     else:
#         print("El valor introducido no es INT.")

# ES MEJOR MANEJAR UN ERROR CUANDO OCURRE QUE TRATAR DE EVITARLO

# try:
#     # Es un lugar donde
#     # tu puedes hacer algo
#     # sin pedir permiso.
#
# except:
# # Es un espacio dedicado
# # exclusivamente para pedir perdón.

# -------- OPCIÓN GENERAL
# try:
#     value = input('Ingresa un número natural: ')
#     print('El recíproco de', value, 'es', 1 / int(value))
# except:
#     print('No se que hacer con', value)
#
# # -------- OPCIÓN ESPECÍFICA SEGÚN EL TIPO DE ERROR
# try:
#     value = input('Ingresa un número natural: ')
#     print('El recíproco de', value, 'es', 1 / int(value))
# except ValueError:
#     print('No se que hacer con', value)
# except ZeroDivisionError:
#     print('La división entre cero no está permitida en nuestro Universo.')
#
# except Exception as e:
#     # ... PRINTA EL MENSAJE DE ERROR ... #
#     print(e)
#
# except:  # <-- POR DEFECTO, siempre el último except
# print('Ha sucedido algo extraño, ¡lo siento!')

""" TIPOS DE ERROR:
ZeroDivisionError: cuando el divisor de una operación es 0 (/, // y %).
ValueError: cuando una función tipo int() o float() recibe un tipo de valor no esperado.
TypeError: no se puede usar un tipo de valor según el contexto, p.e. usar un float como índice.
AttributeError: uso de atributo incorrecto.
    lista.append(2) --> OK
    lista.depend(2) --> no OK
SyntaxError: cuando se escribe mal el código pero el intérprete "se lo traga",
             hasta que se ejecuta y peta.
"""

# Cuando creamos un código, más importante es TESTEAR buscando los posibles errores que confirmar que funciona
# para los valores esperados. Probemos este código:

# temperature = float(input('Ingresa la temperatura actual:'))
# if temperature > 0:
#     print("Por encima de cero")
# elif temperature < 0:
#     prin("Por debajo de cero")
# else:
#     print("Cero")
#
#     # LENGUAJE INTERPRETADO          vs           # LENGUAJE COMPILADO

""" DEPURACIÓN POR IMPRESIÓN: uso de banderillas, marcas de paso """

# EJERCICIOS CLASE 8
# Para todos los ejercicios, controlar todos los posibles errores vía TRY-EXCEPT.


"""
EJERCICIO 1
Elaborar un programa que realice la conversión de cm. a pulgadas. Donde 1cm = 0.39737 pulgadas.
"""

"""
EJERCICIO 2
Obtener la edad de una persona en meses, si se introduce su edad en años y meses. Ejemplo: Introducimos 3 años 4 meses
debe mostrar: 40 meses.
"""

"""
EJERCICIO 3
Los alumnos de 1º de DAWBIO realizaran un viaje a Port Aventura a final de curso, el precio de la entrada general es de 45€.
Al grupo se le aplicará un descuento dependiendo del número de alumnos:
    • Si alumnos > 50 --> 30%
    • Si alumnos entre 20  y 50 --> 20%
    • Si alumnos entre 10 y 20 € --> 10%
    • Si alumnos es <  10 € --> 0%
    • Profesor de programación --> entrada libre.

Se realizará un descuento adicional del 15% a los alumnos menores de 18 años. La cantidad de alumnos
menores del grupo se ha de indicar para obtener el precio final.

El programa mostrará el importe total a pagar para los mayores de edad, el importe a pagar para los menores de edad y 
el importe total del grupo.
"""

"""
EJERCICIO 4
Dadas las listas:
alumno1 = random de 10 notas
alumno2 = random de 10 notas
alumno3 = random de 10 notas

4.1 - Crea una lista de diccionarios:
           alumno1 = {"nombre":"Pepe", "Pt1":5, "Pt2":3,...}
4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.
4.3 - Compararemos las notas de cada alumno indicando, en cada práctica, cuál tiene la nota + alta.
4.4 - Mostraremos sus notas en formato tabla:

    Alumno1 "nombre"
    ----------------
    Pt1 -- 2
    Pt2 -- 6
    ...
    Pt10 -- 8
"""
import random

# 4,1
alumno1 = {"nombre": "1"}
for i in range(1, 11):
    alumno1["Pt" + str(i)] = random.randint(0, 9)

# Creamos alumno 2
alumno2 = {"nombre": "2"}
for i in range(1, 11):
    alumno2["Pt" + str(i)] = random.randint(0, 9)

# Creamos alumno 3
alumno3 = {"nombre": "3"}
for i in range(1, 11):
    alumno3["Pt" + str(i)] = random.randint(0, 9)

# 4,2
for e in alumno1:
    media1 = alumno1[e]
for e in alumno2:
    media2 = alumno2[e]
for e in alumno3:
    media3 = alumno3[e]

print("La media del alumno ", alumno1["nombre"], " es de ", media1)
print("La media del alumno ", alumno2["nombre"], " es de ", media2)
print("La media del alumno ", alumno3["nombre"], " es de ", media3)
medias = []
medias.append(media1)
medias.append(media2)
medias.append(media3)
medias.sort()
print("La media más grande es:", medias[len(medias) - 1])
# 4.3

for i in range(1, 11):
    key = "Pt" + str(i)
    if alumno1[key] > alumno2[key] > alumno3[key]:
        print("La nota del alumno ", alumno1["nombre"], " es mayor. Notas: ", alumno1[key], alumno2[key], alumno3[key])
    elif alumno3[key] < alumno2[key] > alumno1[key]:
        print("La nota del alumno ", alumno2["nombre"], " es mayor. Notas: ", alumno1[key], alumno2[key], alumno3[key])
    elif alumno2[key] < alumno3[key] > alumno1[key]:
        print("La nota del alumno ", alumno3["nombre"], " es mayor. Notas: ", alumno1[key], alumno2[key], alumno3[key])

# 4.4
print("Alumno ", alumno1["nombre"])
print("-------------")
for e in alumno1:
    if e != "nombre":
        print(e, "--", alumno1[e])

print("Alumno ", alumno2["nombre"])
print("-------------")
for e in alumno2:
    if e != "nombre":
        print(e, "--", alumno2[e])

print("Alumno ", alumno3["nombre"])
print("-------------")
for e in alumno3:
    if e != "nombre":
        print(e, "--", alumno3[e])
