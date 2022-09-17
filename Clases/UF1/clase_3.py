"""
Clase 20 de septiembre 20200
"""
"""
If, else y elif
"""

num = 100
print("HACEMOS LAS COMPROBACIONES CON IF")
print("Primera comprobación.")
if num > 0:
    print("+0")
print("Segunda comprobación")
if num > 20:
    print("+20")
print("Tercera comprobación")
if num > 50:
    print("+50")
print("Cuarta comprobacion.")
if num < 100:
    print("-100")

print("Fin. El numero era el: " + str(num))

print("HACEMOS LAS COMPROBACIONES CON ELIF")
if num < 0:
    print("+0")
elif num > 20:
    print("+20")
elif num > 50:
    print("+50")
elif num < 100:
    print("-100")


# EJERCICIOS
"""EJERCICIO 1
_________________
Calcuraremos la letra del DNI
La letra del DNI se calcula, dividiendo el numero del DNI entre 23
el modulo de esta division sera un numero entre 0 y 22
Las letras son: TRWAGMYFPDXBNJZSQVHLCKE
Y las letras se relacionan del 0 al 22:
0 = T
1 = R
2 = W
etc...

SALIDA
La letra de tu DNI es: X. Por lo que tu DNI completo es: XXXXXXXX-X
"""


"""
EJERCICIO 2
-------------

Tramos de la renta:
Tramo 1 - Hasta 12.450 euros: 19% 
Tramo 2 - De 12.450 euros hasta 20.200 euros: 24% 
Tramo 3 - De 20.200 euros hasta 35.200 euros: 30% 
Tramo 4 - De 35.200 euros hasta 60.000 euros: 37% 
Tramo 5 - De 60.000 euros hasta 300.000 euros: 45% 
Tramo 6 - De rentas superiores a 300.000 euros: 47%

2.1- Crearemos un programa que:
    - Pida al usuario sus ingresos anuales
    - Le indique en que tramo de la renta se encuentra
SALIDA
El tramo según tu salario es el X

2.2- Mejoraremos el programa anterior (hacerlo a continuación del anterior) que:
    - Con los ingresos que ya hemos pedido anteriormente, calcule el total de lo que tiene que pagar.
OJO: Los tramos se acumulan

SALIDA
El tramo aplicable es el: X y has de pagar: X€
"""