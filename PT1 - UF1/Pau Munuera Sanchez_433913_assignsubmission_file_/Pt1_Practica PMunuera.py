"""
PT1 - NF1 - DAWBIO1 - M03
INSTRUCCIONES:
- No se permitirán prints innecesarios ni dentro de condicionales ni iteraciones, salvo que sean necesarios
- No se podrán crear nuevas listas
- No se permite el uso de metodos o funciones que no se han expuesto en clase
- Se entregará 1 archivo .py en el que se ejecutarán todos los ejercicios. Indicándose cuando se inicia
cada uno de ellos.
"""

"""
EJERCICIO 1
Elaborar un programa que realice la conversión de cm. a pulgadas. Donde 1cm = 0.39737 pulgadas.
"""
print("Ejercicio 1 :")
n = int(input("Introduce un numero : "))
n2 = 0.39737
print(n,"cm son", n*n2, "pulgadas")

"""
EJERCICIO 2
Obtener la edad de una persona en meses, si se introduce su edad en años y meses. Ejemplo: Introducimos 3 años 4 meses
debe mostrar: 40 meses.
"""
print("\nEjercicio 2 :")
n = int(input("Intrduce tu edad : "))
n2 = int(input("introduce los meses pasados despues de tu ultimo aniversario : "))
print(" Tu edad es ",n*12+n2, "meses")

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
print("\nEjercicio 3")
alum_t=int(input("Introduce los alumnos que van al viaje : "))
alum_m=int(input("Introduce los alumnos menores de 18 : "))
n = 45
alum_18 = alum_t-alum_m
if alum_t > 50:
        precio = ((alum_t-alum_m)*n) * 0.3
elif alum_t < 50 and alum_t > 20:
        precio = ((alum_t-alum_m)*n) * 0.2
elif alum_t < 20 and alum_t > 10:
        precio = ((alum_t-alum_m)*n) * 0.1
elif alum_t < 10:
        precio = (alum_t-alum_m)*n
print(" El precio de los mayores  es " + str(precio) + "€")  
print(" El precio de los menores es ", (alum_m*45)*0.15, "€")
print(" El precio total es " ,precio + ((alum_m*45)*0.15), "€")
"""
EJERCICIO 4
Dadas las listas:
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]

4.1 - Compararemos ambas listas, mostrando por pantalla cuál de las 2 es mas larga.
4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.
4.3 - Recorreremos la lista 1 y compararemos cada elemento de la lista, con el que tenga la misma posición de la otra.
 Indicando que lista posee el elemento con un valor más pequeño.
4.4 - Ordenaremos ambas listas de la misma forma y las mostraremos una de mayor a menor y la otra al revés de forma
invertida.
"""
print("\nEjercicio 4.4")
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]
lista_ordenada1 = lst1[:]
cambios = True
while cambios:
        cambios = False
        for i in range(len(lista_ordenada1) - 1):
         if lista_ordenada1[i] > lista_ordenada1[i + 1]:
            cambios = True
            lista_ordenada1[i], lista_ordenada1[i + 1] = lista_ordenada1[i + 1], lista_ordenada1[i]
lista_ordenada2 = lst2[:]
cambios = True
while cambios:
        cambios = False
        for i in range(len(lista_ordenada2) - 1):
         if lista_ordenada2[i] < lista_ordenada2[i + 1]:
            cambios = True
            lista_ordenada2[i], lista_ordenada2[i + 1] = lista_ordenada2[i + 1], lista_ordenada2[i]
print("Lista ordenada1: " + str(lista_ordenada1))
print("Lista ordenada2: " + str(lista_ordenada2))

