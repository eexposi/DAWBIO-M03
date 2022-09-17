"""Clase 23 sept. 2022"""
""" ITERACIONES 


WHILE

Nos sirve para iterar siempre que se cumpla una condición. Mientras...
"""
i = -1
while i != 0:
    i = int(input("Numero: "))
print("El numero es " + str(i) + ". Acabamos el programa")

# Podemos condicionarlo tambien con boolean
salir = False
while salir == False:
    i = int(input("Numero: "))
    if i == 0:
        salir = True
# Podemos ir contando
i = 0
while i < 20000:
    print(str(i))
    i += 1

"""EJERCICIO 1
___________________
Printaremos por pantalla un menu con 5 opciones.
0 - Salir
1 - Opcion 1
etc.

Le pediremos al usuario que elija una de las opciones. Cuando elija una de las opciones le printaremos por pantalla:
Genial, has elegido la opcion X. 
Y volvera a mostrarnos el menu
El programa acabara cuando elija la opcion 0.

"""

"""FOR
Es la iteración más utilizada.
Nos permite recorrer un rango o los elementos de una variable

Recordemos que se empieza siempre por el 0
"""

for i in range(10):
    print(str(i))
print()
"""Podemos indicarle desde que numero queremos que empiece, aunque siempre terminara en uno menos 
del que hemos indicado"""
for i in range(10, 20):
    print(str(i))

"""Nos permite recorrer elementos"""
texto = "Hola soy una frase y me van a recorrer caracter a caracter"
for i in texto:
    print("- " + str(i) + " - ")
    if i == "a":
        print("Hay una a en el texto")
else:
    print("fin del for")

"""Recordemos que podemos acceder a los elementos de una string de forma individual string[0], string[1], etc..
Y que si ponemos los numeros negativos, sera a la inversa. Siendo el -1 el ultimo, el -2 el penultimo, etc."""
frase = "Hola"
for i in range(0, 4):
    print(frase[i], end="")
print()
frase = "Hola"
for j in range(1, 5):
    print(frase[-j], end="")

"""
EJERCICIO 2

2.1.-
Pediremos una frase al usuario y le devolveremos el numero de caracteres totales de la frase.

2.2.-
Con la misma frase, eliminaremos todas las vocales, guardando la frase en una variable nueva y mostrando ambas.

2.3.- 
La misma grase, la mostraremos a la inversa:
Ejemplo: Hola - aloH

2.4.- 
Substituiremos todas las "o" por "e".
Mostraremos el resultado

"""

"""
Iteraciones con listas

Una lista es un tipo de variable, solo que cada uno de sus elementos puede ser de cualquier tipo de variable, incluso otra lista
Se recorren tal como hemos recorrido los string
lista[0], etc
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lista:
    print(str(i))

lista = ["a", "b", "c", "d"]
for i in lista:
    print(str(i))

lista[0] = "z"
print(lista)

"""Para añadir un nuevo elemento a la lista:
"""
lista.append("e")
print(lista)

lista.insert(0, "a")

lista.remove("a")
print(lista)

lista.pop(0)

"""Ejercicio conjunto:
Pediremos una serie de numeros al usuario, continuados.
Añadiremos cada numero como un int a una lista
Mostraremos cada numero separado por guiones
"""
# numeros = input("Lista de numeros: ")
# lista_numeros =[]
# for e in numeros:
#     lista_numeros.append(int(e))
# print(lista_numeros)

"""EJERCICIO 3
- Pediremos al usuario una serie de numeros y los guardaremos en una lista
- Crearemos una nueva lista donde guardaremos la serie a la inversa
- De la primera lista, obtendremos el numero mas grande
- De la segunda lista, obtendremos el numero más pequeño.

SALIDA
Lista original:
Lista inversa:
Numero mñas pequeño: 
Numero más grande:
"""
