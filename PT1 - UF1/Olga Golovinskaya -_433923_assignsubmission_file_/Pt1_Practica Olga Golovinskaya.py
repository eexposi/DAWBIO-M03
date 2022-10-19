'''EJERCICIO 1
Elaborar un programa que realice la conversión de cm. a pulgadas. Donde 1cm = 0.39737 pulgadas.

a = int (input("Entra cm"))
if a < 0: 
    print("El numero introducido no es válido")
else:   
    print("Los", a, "en pulgadas (rodendeado) son", round(a/0.39737))

EJERCICIO 2
Obtener la edad de una persona en meses, si se introduce su edad en años y meses. Ejemplo: Introducimos 3 años 4 meses
debe mostrar: 40 meses.

a = int (input("Entra los años de tu edad"))
b = int (input("Entra los meses de tu edad"))
if a < 0 or b < 0:
    print("Uno de los numeros introducido no es válido")
else:
    print("Tu edad en meses son", a*12 + b)


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

menores = int(input("Entra la cantidad de alumnos menores de 18 años"))
preciomenores = 45*menores*0.85

mayores = int(input("Entra la cantidad de alumnos mayores de 18 años"))

if mayores > 50:
    preciomayores = 45 * mayores * 0.7
elif 20 <= mayores < 50:
    preciomayores = 45 * mayores * 0.8
elif 10 <= mayores < 20:
    preciomayores = 45 * mayores * 0.9
elif mayores < 10:
    preciomayores = 45 * mayores

if menores > 0:
    print("Precio de entradas para los menores de edad",preciomenores,"€")
print("Precio de entradas para los mayores de edad",preciomayores,"€")
print("Importe total es", preciomayores+preciomenores,"€")


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

'''
lista1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lista2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]
#4.1 - Compararemos ambas listas, mostrando por pantalla cuál de las 2 es mas larga.
contador1 = 0
for i in lista1:
    contador1 += 1
print("El numero de elementos de lista1 es",contador1)
contador2 = 0
for i in lista2:
    contador2 += 1
print("El numero de elementos de lista2 es",contador2)
if contador1> contador2:
    print("La lista 1 es mas larga")
else:
    print("La lista 2 es mas larga")
#4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.

suma1,suma2 = 0,0
for i in lista1:
    suma1 += i
media1 = suma1 / contador1

for i in lista2:
    suma2 += i
media2 = suma2 / contador2
print("La media de la lista 1 es", media1)
print("La media de la lista 2 es", media2)
if media1> media2:
    print("La media de la lista 1 es mas grande")
else:
    print("La media de la lista 2 es mas grande")

#4.3 - Recorreremos la lista 1 y compararemos cada elemento de la lista, con el que tenga la misma posición de la otra.
#Indicando que lista posee el elemento con un valor más pequeño.

small1 = lista1[0]
for i in range(len(lista1)):
    if lista1[i] < small1:
        small1 = lista1[i]
print("El valor más pequeño de la lista 1 es ",small1)

small2 = lista2[0]
for i in range(len(lista2)):
    if lista2[i] < small2:
        small2 = lista2[i]
print("El valor más pequeño de la lista 2 es ",small2)

if small1 < small2:
    print("La lista 1 tiene el valor más pequeño que la lista 2")
if small1 > small2:
    print("La lista 2 tiene el valor más pequeño que la lista 1")
else:
    print("El valor más pequeño de ambas listas es igual")
#4.4 - Ordenaremos ambas listas de la misma forma y las mostraremos una de mayor a menor y la otra al revés de forma
#invertida.
lista_ordenada1 = lista1[:]
a = True
while a:
    a = False
    for i in range(len(lista_ordenada1) - 1):
        if lista_ordenada1[i] < lista_ordenada1[i + 1]:
            a = True
            lista_ordenada1[i], lista_ordenada1[i + 1] = lista_ordenada1[i + 1], lista_ordenada1[i]
print("La lista1 ordenada de mayor a menor  es ",lista_ordenada1)


lista_ordenada2 = lista2[:]
a = True
while a:
    a = False
    for i in range(len(lista_ordenada2) - 1):
        if lista_ordenada2[i] < lista_ordenada2[i + 1]:
            a = True
            lista_ordenada2[i], lista_ordenada2[i + 1] = lista_ordenada2[i + 1], lista_ordenada2[i]
print("La lista2 ordenada de mayor a menor y de la forma invertida ",lista_ordenada2[::-1])


