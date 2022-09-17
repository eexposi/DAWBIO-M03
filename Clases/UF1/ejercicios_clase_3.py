"""Ejercicios clase 20 sept 2022"""
"""
EJERCICIO 1
-------------

Tramos de la renta:
Tramo 1 - Hasta 12.450 euros: 19% 
Tramo 2 - De 12.450 euros hasta 20.200 euros: 24% 
Tramo 3 - De 20.200 euros hasta 35.200 euros: 30% 
Tramo 4 - De 35.200 euros hasta 60.000 euros: 37% 
Tramo 5 - De 60.000 euros hasta 300.000 euros: 45% 
Tramo 6 - De rentas superiores a 300.000 euros: 47%

1.1- Crearemos un programa que:
    - Pida al usuario sus ingresos anuales
    - Le indique en que tramo de la renta se encuentra

1.2- Mejoraremos el programa anterior (hacerlo a continuación del anterior) que:
    - Con los ingresos que ya hemos pedido anteriormente, calcule el total de lo que tiene que pagar.
OJO: Los tramos se acumulan
"""
salario = int(input("Introduzca su salario: "))

print("EJERCICIO 1.1:")
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

print("\nEJERCICIO 1.2:")
acumulado = 0
if 0 <= salario <= 12450:
    tramo = "1"
    acumulado += salario * 0.19
elif 12450 < salario <= 20200:
    tramo = "2"
    acumulado += ((salario - 12450) * 0.24) + (12450 * 0.19)
elif 20200 < salario <= 35200:
    tramo = "3"
    acumulado += ((salario - 20200) * 0.30) + (20200 * 0.24)
elif 35200 < salario <= 60000:
    tramo = "4"
    acumulado += ((salario - 35200) * 0.37) + (35200 * 0.30)
elif 60000 < salario <= 300000:
    tramo = "5"
    acumulado += ((salario - 60000) * 0.45) + (60000 * 0.37)
elif salario > 300000:
    tramo = "6"
    acumulado += ((salario - 300000) * 0.47) + (300000 * 0.45)
else:
    tramo = "ERROR"
    acumulado = "ERROR"
    print("No se encuentra dentro de los baremos")
print("El tramo aplicable es el: " + tramo + " y has de pagar: " + str(acumulado) + "€")
