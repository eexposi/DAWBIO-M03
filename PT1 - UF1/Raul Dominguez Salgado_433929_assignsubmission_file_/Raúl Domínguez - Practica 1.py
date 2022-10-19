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


# Inicio del programa del ejercicio 1
"""
diagonal = float(input("Introduce cuanto mide la diagonal del televisor en centimetros\n"))
print("La diagonal mide",diagonal*.39737,"pulgadas")
"""

"""
EJERCICIO 2
Obtener la edad de una persona en meses, si se introduce su edad en años y meses. Ejemplo: Introducimos 3 años 4 meses
debe mostrar: 40 meses.
"""


# Inicio del programa del ejercicio 2
"""
años = int(input("Introduce cuantos años tienes...\n"))
meses = int(input("Así mismo, iIntroduce cuantos meseshan pasado desde tu último aniversario...\n"))

print(str(años*12 + meses) + " meses")
"""

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


# Inicio del programa de ejercicio 3

"""
PRECIO_ENTRADA = 45
DESC_MENORES = PRECIO_ENTRADA*.15


mayores = int(input("Indica el número de alumnos mayores de edad...\n"))
menores = int(input("Así mismo, indica el número de alumnos menores de 18...\n"))

alumnos_totales = mayores + menores

if alumnos_totales > 50:
        desc = .3
elif alumnos_totales > 20:
        desc = .2
elif alumnos_totales >= 10:
        desc = .1
elif alumnos_totales < 10:
        desc = 0

precio_mayores = mayores*(PRECIO_ENTRADA - (PRECIO_ENTRADA*desc))
precio_menores = menores*(PRECIO_ENTRADA - (PRECIO_ENTRADA*desc) - DESC_MENORES)

print("El precio a pagar del grupo entero es ", precio_mayores + precio_menores)

"""

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


# Inicio del programa del ejercicio 4

lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]






###################################### Ejercicio 4.1 #######################################
"""
#Comparamos la longitud de cada lista
if len(lst1) > len(lst2):
        print("-La lista 1 es más larga que la lista 2\n")
elif len(lst1) < len(lst2):
        print("-La lista 2 es más larga que la lista 1\n")
elif len(lst1) == len(lst2):
        print("-Las dos listas son igual de largas\n")
"""







###################################### Ejercicio 4.2 #######################################
"""
media_lst1 = 0
media_lst2 = 0

#Recorremos cada lista encontrado la suma de todos los valores.
for x in range(len(lst1)):
        media_lst1 += lst1[x]
for x in range(len(lst2)):
        media_lst2 += lst2[x]

#Dividimos la suma de valores entre la longitud de cada lista.
media_lst1 = media_lst1/len(lst1)
media_lst2 = media_lst2/len(lst2)

#Devolvemos los resultados
print("-La media de la lista 1 es", media_lst1, "y la media de la lista 2 es", media_lst2)

#Y definimos que lista es más larga
if media_lst1 < media_lst2:
        print("-De manera que la segunda lista tiene una media más grande.\n")
elif media_lst1 > media_lst2:
        print("-De manera que la primera lista tiene una media más grande.\n")
elif media_lst1 == media_lst2:
        print("-De manera que las dos listas tienen la misma media.\n")




"""


################################### Ejercicio 4.3 #######################################
"""
#Determinamos el número de vueltas con la longitud de la lista mas corta
if len(lst1) > len(lst2):
        vueltas = len(lst2)
elif len(lst1) < len(lst2):
        vueltas = len(lst1)
elif len(lst1) == len(lst2):
        vueltas = len(lst2)


iterador = 0
while iterador < vueltas:        
        if lst1[iterador] > lst2[iterador]:
                print("En la " + str(iterador) +  "ª posición la lista 1 tiene un número más grande")
        elif lst1[iterador] < lst2[iterador]:
                print("En la " + str(iterador) +  "ª posición la lista 2 tiene un número más grande")
        elif lst1[iterador] == lst2[iterador]:
                print("En la " + str(iterador) +  "ª posición las dos istas tienen el mismo número")

        #Avanzamos a la siguiente vuelta
        iterador += 1
        iterador += 1

"""



################################### Ejercicio 4.4 #######################################
"""
# Ordeamos ambas listas
hay_cambios = True
while hay_cambios:
    hay_cambios = False
    for i in range(len(lst1) - 1):
        if lst1[i] > lst1[i + 1]:
            hay_cambios = True
            lst1[i], lst1[i + 1] = lst1[i + 1], lst1[i]
hay_cambios = True
while hay_cambios:
    hay_cambios = False
    for i in range(len(lst2) - 1):
        if lst2[i] > lst2[i + 1]:
            hay_cambios = True
            lst2[i], lst2[i + 1] = lst2[i + 1], lst2[i]

# Invertimos la primera
lst_aux = []
contador = len(lst2)
for x in lst2:
      lst_aux.append(lst2[contador - 1])
      contador -= 1
lst2 = lst_aux

# Imprimimos ambas listas
print(lst1)
print(lst2)


"""
