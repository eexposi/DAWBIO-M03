"""
EJERCICIO 4
Dadas las listas:
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
 0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3, 5, 9, 8,
  0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]

lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
 5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2, 0, 10,
  7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 10, 8, 1, 7, 2, 0]


4.1 - Compararemos ambas listas, mostrando por pantalla cual de las 2 es mas larga.
4.2 - Realizaremos la media de cada una, indicando el resultado y cual tiene la media más grande.
4.3 - Recorreremos la lista 1 y compararemos cada elemento de la lista, con el que tenga la misma posición de la otra.
 Indicando que lista pose el elemento con un valor más pequeño.
4.5 - Ordenaremos ambas listas y mostraremos los 10 primeros numeros.

"""
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8,
        0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10,
        7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]
# 4.1
print("4.1 ---- Compararemos ambas listas, mostrando por pantalla cual de las 2 es mas larga.")
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
    "4.3 - Compararemos cada elemento de la lista, con el que tenga la misma posición de la otra. Indicando que lista "
    "pose el elemento con un valor más pequeño. (vigilad que las listas no tienen el mismo tamaño)")
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
print(lst2[10::-1])
