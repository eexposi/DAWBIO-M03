# EJERCICIO 1
# Elaborar un programa que realice la conversión de cm. a pulgadas. Donde 1cm = 0.39737 pulgadas.

numero = float(input("Introduce un numero: "))
conversion = numero * 0.39737
print("La conversion de " + str(numero) + "cm a pulgadas es: " + str(conversion) + " pulgadas")

# EJERCICIO 2
# Obtener la edad de una persona en meses, si se introduce su edad en años y meses. Ejemplo: Introducimos 3 años 4 meses
# debe mostrar: 40 meses.

edad = int(input("Introduce tu edad: "))
meses = int(input("Introduce meses cumplidos: "))
calculo = (edad * 12) + meses
print(calculo)

# EJERCICIO 3
# Los alumnos de 1º de DAWBIO realizaran un viaje a Port Aventura a final de curso, el precio de la entrada general es de 45€.
# Al grupo se le aplicará un descuento dependiendo del número de alumnos:
#     • Si alumnos > 50 --> 30%
#     • Si alumnos entre 20  y 50 --> 20%
#     • Si alumnos entre 10 y 20 € --> 10%
#     • Si alumnos es <  10 € --> 0%
#     • Profesor de programación --> entrada libre.

# Se realizará un descuento adicional del 15% a los alumnos menores de 18 años. La cantidad de alumnos
# menores del grupo se ha de indicar para obtener el precio final.

# El programa mostrará el importe total a pagar para los mayores de edad, el importe a pagar para los menores de edad y 
# el importe total del grupo.

numero_de_alumnos = int(input("Introduce número de alumos: "))
mayores_de_edad = int(input("Introduce el numero de alumnos mayores de edad: "))

menores_de_edad = numero_de_alumnos - mayores_de_edad

for i in range(menores_de_edad + 1):
    descuento_menores_de_edad = 45 * 15 // 100
    precio_menores = menores_de_edad * descuento_menores_de_edad

for i in range(numero_de_alumnos + 1):
    if i > 50:
        descuento1 = 45 * 30 // 100
        precio_mas_50_alumnos = 45 - descuento1
        print("Importe total del grupo: " + str((precio_mas_50_alumnos * numero_de_alumnos) - precio_menores) + "€")
        print("Importa total mayores de edad: " + str(precio_mas_50_alumnos * mayores_de_edad) + "€")
        print("Importe total menores de edad: " + str((precio_mas_50_alumnos - descuento_menores_de_edad) * menores_de_edad) + "€")
        break
    elif i > 20 and i < 50:
        descuento2 = 45 * 20 // 100
        precio_entre_20_50_alumnos = 45 - descuento2
        print("Importe total del grupo: " + str(precio_entre_20_50_alumnos * numero_de_alumnos - precio_menores) + "€")
        print("Importa total mayores de edad: " + str(precio_entre_20_50_alumnos * mayores_de_edad) + "€")
        print("Importe total menores de edad: " + str((precio_entre_20_50_alumnos - descuento_menores_de_edad) * menores_de_edad) + "€")
        break
    elif i > 10 and i < 20:
        descuento3 = 45 * 10 // 100
        precio_entre_10_20_alumnos = 45 - descuento3
        print("Importe total del grupo: " + str(precio_entre_10_20_alumnos * numero_de_alumnos - precio_menores) + "€")
        print("Importa total mayores de edad: " + str(precio_entre_10_20_alumnos * mayores_de_edad) + "€")
        print("Importe total menores de edad: " + str((precio_entre_10_20_alumnos - descuento_menores_de_edad) * menores_de_edad) + "€")
        break
    elif i < 10:
        precio_menos_10_alumnos = 45
        print("Importe total del grupo: " + str((precio_menos_10_alumnos * numero_de_alumnos) - precio_menores) + "€")
        print("Importa total mayores de edad: " + str(precio_menos_10_alumnos * mayores_de_edad) + "€")
        print("Importe total menores de edad: " + str((precio_menos_10_alumnos - descuento_menores_de_edad) * menores_de_edad) + "€")
        break

# EJERCICIO 4
# Dadas las listas:
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]

# 4.1 - Compararemos ambas listas, mostrando por pantalla cuál de las 2 es mas larga.

cont_lst1 = 0
for i in lst1:
    cont_lst1 += 1

cont_lst2 = 0
for i in lst2:
    cont_lst2 += 1

if cont_lst1 > cont_lst2:
    print("La primera lista es más grande que la segunda lista")
else: 
    print("La segunda lista es más grande que la primera lista")

# 4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.

cont_media_lst1 = 0
for i in lst1:
    cont_media_lst1 += i

cont_media_lst2 = 0
for i in lst2:
    cont_media_lst2 += i

print("La media de la primera lista es: " + str(cont_media_lst1))
print("La media de la segunda lista es: " + str(cont_media_lst2))

if cont_media_lst1 > cont_media_lst2:
    print("La media de la primera lista es más grande que la media de la segunda lista")
else:
    print("La media de la segunda lista es más grande que la media de la primera lista")

# 4.3 - Recorreremos la lista 1 y compararemos cada elemento de la lista, con el que tenga la misma posición de la otra.
#  Indicando que lista posee el elemento con un valor más pequeño.

for i in range(0, cont_lst2):
    if lst1[i] > lst2[i]:
        print("En la posicion " + str(i) + " el valor más pequeño esta en la lista 2")
    elif lst1[i] < lst2[i]:
        print("En la posicion " + str(i) + " el valor mas pequeño esta en la lista 1")
    elif lst1[i] == lst2[i]:
        print("En la posicion " + str(i) + " el valor es igual en las dos listas")

# 4.4 - Ordenaremos ambas listas de la misma forma y las mostraremos una de mayor a menor y la otra al revés de forma
# invertida.
lista_mayor_menor = lst1[:]
hay_cambios = True
while hay_cambios:
    hay_cambios = False
    for i in range(len(lista_mayor_menor)-1):
        if lista_mayor_menor[i] < lista_mayor_menor[i+1]:
            hay_cambios = True
            lista_mayor_menor[i], lista_mayor_menor[i+1] = lista_mayor_menor[i+1], lista_mayor_menor[i]

lista_mayor_menor2 = lst2[:]
hay_cambios = True
while hay_cambios:
    hay_cambios = False
    for i in range(len(lista_mayor_menor2)-1):
        if lista_mayor_menor2[i] < lista_mayor_menor2[i+1]:
            hay_cambios = True
            lista_mayor_menor2[i], lista_mayor_menor2[i+1] = lista_mayor_menor2[i+1], lista_mayor_menor2[i]

