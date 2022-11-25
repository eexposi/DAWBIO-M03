"""
PT1 - NF1 - DAWBIO1 - M03
"""
"""
EJERCICIO 1
Elaborar un programa que realice la conversión de cm. a pulgadas. 
Donde 1cm = 0.39737 pulgadas.
"""
# cm = int(input("Introduce los cm: "))
# print("En pulgadas son: " + str(cm * 0.39737))

"""
EJERCICIO 2
Obtener la edad de una persona en meses, si se introduce su edad en años y meses.
Ejemplo: Introducimos 3 años 4 meses debe mostrar: 40 meses.
"""
# anyos = 0
# meses = 0
# anyos = int(input("Indique los años: "))
# meses = int(input("Indique los meses: "))
# total_meses = (anyos * 12) + meses
# print("Tienes " + str(total_meses) + " meses de edad.")

"""
EJERCICIO 3
Los alumnos  de 1º de DAWBIO realizaran un viaje a Port Aventura  a final de curso, el precio de la entrada general es de 45€.
Al grupo se le aplicará un descuento dependiendo del número de alumnos :
    • Si alumnos > 50  30%
    • Si alumnos entre 20  y 50  20%
    • Si alumnos entre 10 y 20 €  10%
    • Si alumnos es <  10 €  0%
    • Profesor de programación -- entrada libre.

Se realizará un descuento adicional del 15% a los alumnos menores de 18 años
 la cantidad de alumnos
menores del grupo se ha de indicar para obtener el precio final.

El programa mostrará el importe total a pagar para los mayores de edad 
y el importe a pagar para los menores de edad y el importe total del grupo.

NOTA: No se permitirán prints dentro de if ni similares. Se realizarán 
los prints correspondientes al final del programa.
"""
# alumnos = int(input("Introduce la cantidad total de alumnos: "))
# menores = int(input("Introduce la cantidad de menores de edad: "))
# precio_entrada = 45
# precio_menores = (precio_entrada * 0.85)
# precio_con_descuento = 0

# if alumnos > 50:
#     precio_con_descuento = precio_entrada * 0.70
# elif 20 < alumnos <= 50:
#     precio_con_descuento = precio_entrada * 0.80
# elif 10 < alumnos <= 20:
#     precio_con_descuento = precio_entrada * 0.9
# else:
#     precio_con_descuento = precio_entrada

# coste_menores = menores * precio_menores
# coste_adultos = ((alumnos - menores) * precio_con_descuento)
# print("Los menores deberán pagar un total de: " + str(coste_menores))
# print("Los mayores de edad deberán pagar un total de: " + str(coste_adultos))
# print("El coste total es de: " + str(coste_adultos + coste_menores))

"""
EJERCICIO 4
Dadas las listas:
lst1 = [9, 2, 4, 5, 12
lst2 =

4.1 - Compararemos ambas listas, mostrando por pantalla cual de las 2 es mas larga.
4.2 - Realizaremos la media de cada una, indicando el resultado y cual tiene la media más grande.
4.3 - Compararemos cada elemento de la lista, con el que tenga la misma posición de la otra. Indicando que lista
    pose el elemento con un valor más pequeño. (vigilad que las listas no tienen el mismo tamaño)
4.5 - Ordenaremos ambas listas y las mostraremos de forma invertida.

"""
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]
# 4.1
print("4.1 ---- Compararemos ambas listas, mostrando por pantalla cual"
+" de las 2 es mas larga.")
long_lst1 = 0
suma_lst1 = 0
for i in lst1:
    long_lst1 += 1
    suma_lst1 += i
long_lst2 = 0
suma_lst2 = 0
for i in lst2:
    long_lst2 += 1
    suma_lst2 += i

print("Long1: " + str(long_lst1))
print("Long2: " + str(long_lst2))
print("4.2 - Realizaremos la media de cada una, indicando el resultado y cual tiene la media más grande.")
print("La media de la lst1 es: " + str(suma_lst1 / long_lst1))
print("La media de la lst2 es: " + str(suma_lst2 / long_lst2))

print(
    "4.3 - Compararemos cada elemento de la lista, con el que tenga la misma posición de la otra. Indicando que lista pose el elemento con un valor más pequeño. vigilad que las listas no tienen el mismo tamaño)")
for i in range(long_lst2):
    if lst1[i] < lst2[i]:
        print(
            "En el indice " + str(i) + " los valores son: " + str(lst1[i]) + " y " + str(lst2[i]) + " y el de la lst1 "
                                                                                                    "es mas pequeño")
    else:
        print(
            "En el indice " + str(i) + " los valores son: " + str(lst1[i]) + " y " + str(lst2[i]) + " y el de la lst2 "
                                                                                                    "es mas pequeño")

print("4.5 - Ordenaremos ambas listas y las mostraremos de forma invertida.")
hay_cambios = True
while hay_cambios == True:
    hay_cambios = False
    for i in range(long_lst1 - 1):
        if lst1[i] < lst1[i + 1]:
            lst1[i], lst1[i + 1] = lst1[i + 1], lst1[i]
            hay_cambios = True

hay_cambios = True
while hay_cambios == True:
    hay_cambios = False
    for i in range(long_lst2 - 1):
        if lst2[i] < lst2[i + 1]:
            lst2[i], lst2[i + 1] = lst2[i + 1], lst2[i]
            hay_cambios = True
print(lst1[:10])
print(lst2[long_lst2::-1])
