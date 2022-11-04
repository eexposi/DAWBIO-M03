"""
PT1 - NF1 - DAWBIO1 - M03
INSTRUCCIONES:
- No se permitirán prints innecesarios ni dentro de condicionales ni iteraciones, salvo que sean necesarios
- No se podrán crear nuevas listas
- No se permite el uso de metodos o funciones que no se han expuesto en clase
- Se entregará 1 archivo .py en el que se ejecutarán todos los ejercicios. Indicándose cuando se inicia
cada uno de ellos.



EJERCICIO 1
Elaborar un programa que realice la conversión de cm. a pulgadas. Donde 1cm = 0.39737 pulgadas.
"""

cm = int(input("Introduce la medida en cm: "))
pulgadas = cm * 0.39737
print(str(cm) + " cm son " + str(pulgadas) + " pulgadas.")
"""

EJERCICIO 2
Obtener la edad de una persona en meses, si se introduce su edad en años y meses. Ejemplo: Introducimos 3 años 4 meses
debe mostrar: 40 meses.
"""

any = int(input("Dime cuántos años tienes: "))
mes = int(input("Dime cuántos meses tienes: "))
total_meses = (any * 12) + mes
print("Tienes " + str(total_meses) + " meses.")

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

num_alumnos = int(input("Número de alumnos: "))
num_menores = int(input("Dime cuantós alumnos son menores de edad: "))
descuento = ""
entrada = 45

if num_alumnos > 50:
    descuento = entrada - (entrada * 0.3)
elif num_alumnos >= 20 and num_alumnos <= 50:
    descuento = entrada - (entrada * 0.20)
elif num_alumnos >= 10 and num_alumnos <= 20:
    descuento = entrada - (entrada * 0.10)
elif num_alumnos < 10:
    descuento = entrada
print("Los alumnos mayores de 18 años tienen que pagar: " + str(descuento) + " euros cada uno.")

descuento2 = descuento - (entrada * 0.15)

print("Hay " + str(num_menores) + " alumnes menores de edad. Los alumnos menores de edad tienen que pagar: " + str(
    descuento2) + " euros cada uno.")

total = (descuento * (num_alumnos - num_menores)) + (descuento2 * num_menores)
print("El grupo tiene que pagar en total: " + str(total) + " euros.")

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
"""

lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]
long = 0
for i in lst1:
    long += 1
print("La list1 tiene: " + str(long) + " elementos.")
long2 = 0
for e in lst2:
    long2 += 1
print("La lista2 tiene: " + str(long2) + " elementos.")
if long > long2:
    print("La list1 es más larga que la list2.")
else:
    print("La list2 es más larga que la list1")
"""      

4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.


        

4.3 - Recorreremos la lista 1 y compararemos cada elemento de la lista, con el que tenga la misma posición de la otra.
 Indicando que lista posee el elemento con un valor más pequeño.
"""
contador = long
for i in range(long):

    if lst1[0] < lst2[0]:
        print("La list1 tiene el elemento más pequeño")

    elif lst1[0] == lst2[0]:
        print("Los elementos son iguales.")

    else:
        print("La list2 tiene el elemento más pequeño.")

"""
4.4 - Ordenaremos ambas listas de la misma forma y las mostraremos una de mayor a menor y la otra al revés de forma
invertida.
"""

lst1_ordenada = lst1[:]
cambios = True
while cambios:
    cambios = False
    for i in range(len(lst1_ordenada) - 1):
        if lst1_ordenada[i] > lst1_ordenada[i + 1]:
            cambios = True
            lst1_ordenada[i], lst1_ordenada[i + 1] = lst1_ordenada[i + 1], lst1_ordenada[i]

lst2_ordenada = lst2[:]
cambios = True
while cambios:
    cambios = False
    for e in range(len(lst2_ordenada) - 1):
        if lst2_ordenada[e] > lst2_ordenada[e + 1]:
            cambios = True
            lst2_ordenada[e], lst2_ordenada[e + 1] = lst2_ordenada[e + 1], lst2_ordenada[e]

contador = long2
lst2_inversa = []
for i in range(long2):
    lst2_inversa.append(lst2_ordenada[contador - 1])
    contador -= 1

print(lst1_ordenada)
print(lst2_inversa)
