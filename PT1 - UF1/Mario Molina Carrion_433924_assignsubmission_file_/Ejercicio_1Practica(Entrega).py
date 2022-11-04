# EJERCICIO 1
# Elaborar un programa que realice la conversión de cm. a pulgadas. Donde 1cm = 0.39737 pulgadas.

num = int(input("Itroduzca la cantidad de cm que quiere pasa a pulgadas: "))
p = num * 0.39737
print("La cantidad obtenida de pulgadas son ", p, "pulgadas")

# EJERCICIO 2
# Obtener la edad de una persona en meses, si se introduce su edad en años y meses. Ejemplo: Introducimos 3 años 4 meses
# debe mostrar: 40 meses.

ano = int(input("Escriba su edad en años: "))
meses = int(input("Escriba cuantos meses han pasado desde que cumplió años por ultima vez: "))
n = ano * 12
print("la cantidad de meses que tiene usted es", n + meses, "meses")

# EJERCICIO 3
# Los alumnos de 1º de DAWBIO realizaran un viaje a Port Aventura a final de curso, el precio de la entrada general es de 45€.
# Al grupo se le aplicará un descuento dependiendo del número de alumnos:
#   • Si alumnos > 50 --> 30%
#   • Si alumnos entre 20  y 50 --> 20%
#   • Si alumnos entre 10 y 20 € --> 10%
#   • Si alumnos es <  10 € --> 0%
#   • Profesor de programación --> entrada libre.
# 
# Se realizará un descuento adicional del 15% a los alumnos menores de 18 años. La cantidad de alumnos
# menores del grupo se ha de indicar para obtener el precio final.
# El programa mostrará el importe total a pagar para los mayores de edad, el importe a pagar para los menores de edad y 
# el importe total del grupo.

Alumnos_mayores_de_Edad = int(input("Escriba la cantidad de alumnos mayores de Edad: "))
Alumnos_menores_de_Edad = int(input("Escriba la cantidad de Alumnos menores de Edad: "))
Mas_de_50 = 45 - 45 * 0.3
Entre_20y50 = 45 - 45 * 0.2
Entre_10y20 = 45 - 45 * 0.1
Menos_de_10 = 45
r = 0
while r < 1:
    if Alumnos_mayores_de_Edad + Alumnos_menores_de_Edad >= 50:
        Todos = Alumnos_mayores_de_Edad * Mas_de_50 + Alumnos_menores_de_Edad * Mas_de_50 * 0.15
        Alumnos_mayores_de_Edad = Alumnos_mayores_de_Edad * Mas_de_50
        Alumnos_menores_de_Edad = Alumnos_menores_de_Edad * Mas_de_50 * 0.15
        r = r + 1
    elif Alumnos_mayores_de_Edad + Alumnos_menores_de_Edad >= 20 < 50:
        Todos = Alumnos_mayores_de_Edad * Entre_20y50 + Alumnos_menores_de_Edad * Entre_20y50 * 0.15
        Alumnos_mayores_de_Edad = Alumnos_mayores_de_Edad * Entre_20y50
        Alumnos_menores_de_Edad = Alumnos_menores_de_Edad * Entre_20y50 * 0.15
        r = r + 1
    elif Alumnos_mayores_de_Edad + Alumnos_menores_de_Edad >= 10 < 20:
        Todos = Alumnos_mayores_de_Edad * Entre_10y20 + Alumnos_menores_de_Edad * Entre_10y20 * 0.15
        Alumnos_mayores_de_Edad = Alumnos_mayores_de_Edad * Entre_10y20
        Alumnos_menores_de_Edad = Alumnos_menores_de_Edad * Entre_10y20 * 0.15
        r = r + 1
    elif Alumnos_mayores_de_Edad + Alumnos_menores_de_Edad < 10:
        Todos = Alumnos_mayores_de_Edad * Menos_de_10 + Alumnos_menores_de_Edad * Menos_de_10 * 0.15
        Alumnos_mayores_de_Edad = Alumnos_mayores_de_Edad * Menos_de_10
        Alumnos_menores_de_Edad = Alumnos_menores_de_Edad * Menos_de_10 * 0.15
        r = r + 1
print("El precio de la entrada por alumno mayor de Edad será ", Alumnos_mayores_de_Edad, "€")
print("El precio de la entrada por alumno menor de Edad será ", Alumnos_menores_de_Edad, "€")
print("El precio de el grupo será", Todos, "€")

# EJERCICIO 4
# Dadas las listas:
# lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
#         0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
#         5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
# lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
#         5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
#         0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]
# 4.1 - Compararemos ambas listas, mostrando por pantalla cuál de las 2 es mas larga.
# 4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.
# 4.3 - Recorreremos la lista 1 y compararemos cada elemento de la lista, con el que tenga la misma posición de la otra.
#  Indicando que lista posee el elemento con un valor más pequeño.
# 4.4 - Ordenaremos ambas listas de la misma forma y las mostraremos una de mayor a menor y la otra al revés de forma
# invertida.

# Creamos lista original
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lista_ordenada = lst1[:]

# Ordenamos la lista
hay_cambios = True
while hay_cambios:
    hay_cambios = False
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] > lista_ordenada[i + 1]:
            hay_cambios = True
            lista_ordenada[i], lista_ordenada[i + 1] = lista_ordenada[i + 1], lista_ordenada[i]

# Calculamos el valor medio
punto_medio = len(lista_gauss) // 2

print("Lista 1 original: " + str(lst1))
print("Lista 1 ordenada: " + str(lista_ordenada))
print("Lista 1 gauss: " + str(lista_gauss))
print("El valor medio de la lista 1 es: " + str(lista_gauss[punto_medio]))

# Creamos lista original
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]
lista_ordenada2 = lst2[:]

# Ordenamos la lista
hay_cambios = True
while hay_cambios:
    hay_cambios = False
    for i in range(len(lista_ordenada2) - 1):
        if lista_ordenada2[i] > lista_ordenada2[i + 1]:
            hay_cambios = True
            lista_ordenada2[i], lista_ordenada2[i + 1] = lista_ordenada2[i + 1], lista_ordenada2[i]

# Calculamos el valor medio
punto_medio2 = len(lista_gauss) // 2

if punto_medio > punto_medio2:
    punto_medio = punto_medio
elif punto_medio < punto_medio2:
    punto_medio = punto_medio2

print("Lista 2 original: " + str(lst2))
print("Lista 2 ordenada: " + str(lista_ordenada))
print("Lista 2 gauss: " + str(lista_gauss))
print("El valor medio de la lista 2 es: " + str(lista_gauss[punto_medio2]))

if lista_gauss[punto_medio] > lista_gauss[punto_medio2]:
    lista_gauss[punto_medio] = lista_gauss[punto_medio]
elif lista_gauss[punto_medio] < lista_gauss[punto_medio2]:
    lista_gauss[punto_medio] = lista_gauss[punto_medio2]
elif lista_gauss[punto_medio] == lista_gauss[punto_medio2]:
    lista_gauss[punto_medio] = lista_gauss[punto_medio2]
print("El punto medio más grande es", lista_gauss[punto_medio])
