"""Ejercicios clase 20 sept 2022"""
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

dni = int(input("Introduce el DNI: "))
mod = dni % 23
letra = ""

if mod == 0:
    letra = "T"
elif mod == 1:
    letra = "R"
elif mod == 2:
    letra = "W"
elif mod == 3:
    letra = "A"
elif mod == 4:
    letra = "G"
elif mod == 5:
    letra = "M"
elif mod == 6:
    letra = "Y"
elif mod == 7:
    letra = "F"
elif mod == 8:
    letra = "P"
elif mod == 9:
    letra = "D"
elif mod == 10:
    letra = "X"
elif mod == 11:
    letra = "B"
elif mod == 12:
    letra = "N"
elif mod == 13:
    letra = "J"
elif mod == 14:
    letra = "Z"
elif mod == 15:
    letra = "S"
elif mod == 16:
    letra = "Q"
elif mod == 17:
    letra = "V"
elif mod == 18:
    letra = "H"
elif mod == 19:
    letra = "L"
elif mod == 20:
    letra = "C"
elif mod == 21:
    letra = "K"
elif mod == 22:
    letra = "E"

print("La letra de tu DNI es: " + letra + ". Por lo que tu DNI completo es: " + str(dni) + letra)

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
salario = int(input("Introduzca su salario: "))

print("EJERCICIO 2.1:")
tramo = ""
if salario <= 12450:
    tramo = "1"
elif 12450 < salario <= 20200:
    tramo = "2"
elif 20200 < salario <= 3520:
    tramo = "3"
elif 35200 < salario <= 60000:
    tramo = "4"
elif 60000 < salario <= 300000:
    tramo = "5"
else:
    tramo = "6"
print("El tramo según tu salario es el " + tramo)

print("\nEJERCICIO 2.2:")
if salario > 300000:
    # Tramo 6
    impuestos = (12450 * 0.19) + (7749 * 0.24) + (14999 * 0.30) + (24599 * 0.37) + (239999 * 0.45) + (salario - 300001) * 0.47
elif 300000 >= salario > 60000:
    # Tramo 5
    impuestos = (12450 * 0.19) + (7749 * 0.24) + (14999 * 0.30) + (24599 * 0.37) + (salario - 60001) * 0.45
elif 60000 >= salario > 35200:
    # Tramo 4
    impuestos = (12450 * 0.19) + (7749 * 0.24) + (14999 * 0.30) + (salario - 35201) * 0.37
elif 35200 >= salario > 20200:
    # Tramo 3
    impuestos = (12450 * 0.19) + (7749 * 0.24) + (salario - 20201) * 0.30
elif 20200 >= salario > 12450:
    # Tramo 2
    impuestos = 12450 * 0.19 + (salario - 12450) * 0.24
elif 12450 > salario >= 0:
    # Tramo 1
    impuestos = salario * 0.19

print("El tramo aplicable es el: " + str(tramo) + " y has de pagar: " + str(impuestos) + "€")
