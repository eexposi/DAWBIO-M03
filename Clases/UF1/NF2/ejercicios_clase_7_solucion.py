""" EJERCICIO 1 ------------------------------------------------------------------------------------
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está
en el diccionario, pidiéndole que introduzca el símbolo si lo conoce. Finalmente mostrará toda la lista
en formato:

MONEDA <--> SÍMBOLO
-------------------
moneda 1 <--> símbolo 1
moneda 2 <--> símbolo 2
...
moneda nueva <--> símbolo nuevo
--------------------------------------------------------------------------------------------------- """

monedas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
moneda = input("Introduce una divisa: ")
if moneda in monedas:
    print(monedas[moneda])
else:
    simbolo = input("La divisa no está. Cómo se simboliza? ")
    monedas[moneda] = simbolo

print()
print("MONEDA <--> SIMBOLO")
print("-------------------")
for moneda, simbolo in monedas.items():
    print(moneda, simbolo, sep=' <--> ')

""" EJERCICIO 2 -----------------------------------------------------------------------------------
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe 
preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
Después se debe mostrar por pantalla la lista de la compra SIN EL PRECIO del artículo y el coste total, 
con el siguiente formato: 

LISTA DE LA COMPRA:
--------------------
Artículo 1
Artículo 2
Artículo ..
Artículo n
TOTAL   XXX €

Y finalmente, podemos pedirle el precio unitario de un artículo concreto, hasta que el usuario decida
terminar.                                                                                         """

cesta = {}

continuar = True
while continuar:
    item = input("Introduce un artículo: ")
    precio = float(input("Introduce el precio de " + item + ": "))
    cesta[item] = precio
    continuar = input("¿Quieres añadir artículos a la lista (Si/No)? ") == "Si"
coste = 0

print()
print("Lista de la compra:")
print("-------------------")
for item, precio in cesta.items():
    print(item)
    coste += precio
print("Coste total: ", coste)
print()

continuar = True
while continuar:
    item = input("Quieres saber el precio de algún artículo? Introduce artículo: ")
    if item in cesta:
        print(cesta[item])
    else:
        print("Este artículo no está en la cesta.")
    continuar = input("¿Quieres saber el precio del algún otro artículo (Si/No)? ") == "Si"
