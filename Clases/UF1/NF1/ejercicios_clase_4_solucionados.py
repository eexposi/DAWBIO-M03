"""Ejercicios clase 23 sept. 2022"""
"""EJERCICIO 1
___________________
Printaremos por pantalla un menu con 3 opciones.
0 - Salir
1 - Opcion 1
etc.

Le pediremos al usuario que elija una de las opciones. Cuando elija una de las opciones le printaremos por pantalla:
Genial, has elegido la opcion X. 
Y volvera a mostrarnos el menu
El programa acabara cuando elija la opcion 0.

"""

opc0 = "0 - Salir"
opc1 = "1 - Opcion 1"
opc2 = "2 - Opcion 2"

while True:
    print(opc0)
    print(opc1)
    print(opc2)
    resposta = int(input("Elija su opcion: "))
    if resposta == 0:
        print("Adios")
        break
    elif resposta == 1:
        print("Genial, has elegido la opcion 1")
    elif resposta == 2:
        print("Genial, has elegido la opcion 2")
    else:
        print("No has elegido ninguna opcion correcta.")

"""
EJERCICIO 2

2.1.-
Pediremos una frase al usuario y le devolveremos el numero de caracteres totales de la frase.

2.2.-
Con la misma frase, eliminaremos todas las vocales, guardando la frase en una variable nueva y mostrando ambas.

2.3.- 
La misma frase, la mostraremos a la inversa:
Ejemplo: Hola - aloH

"""
frase = input("Indica una frase: ")

print("EJERCICIO 2.1")
tamany = 0
for e in frase:
    tamany += 1
print("La frase - " + frase + " - tiene " + str(tamany) + " caracteres")

print("EJERCICIO 2.2")
frase_sin_vocales = ""
for e in frase:
    if e != "a" and e != "e" and e != "i" and e != "o" and e != "u":  # Tener en cuenta tema mayuusculas
        frase_sin_vocales += e
print("La frase sin vocales es: " + frase_sin_vocales)

print("EJERCICIO 2.3")
contador = tamany
nueva_frase = ""
for i in range(tamany):
    nueva_frase += frase[contador - 1]
    contador -= 1
print(nueva_frase)

"""EJERCICIO 3
- Pediremos al usuario numeros de forma indefinida hasta que ingrese el 999, y se iran guardando en una lista
- Crearemos una nueva lista donde guardaremos la serie a la inversa
- De la primera lista, obtendremos el numero mas grande
- De la segunda lista, obtendremos el numero más pequeño.

SALIDA
Lista original:
Lista inversa:
Numero mñas pequeño: 
Numero más grande:
"""
serie = 0
lista_original = []
orden = 0
numero_salida = -999
while serie != numero_salida:
    serie = int(input("Numero " + str(orden) + " de la lista (" + str(numero_salida) + " para salir): "))
    if serie != numero_salida:
        lista_original.append(serie)
    orden += 1

# Calculamos el tamaño de la lista
long = 0
for e in lista_original:
    long += 1

# Creamos la nueva lista
contador = long
lista_inversa = []
for e in range(long):
    lista_inversa.append(lista_original[contador - 1])
    contador -= 1

# Sobre la lista original, buscamos el numero más grande
numero_mas_grande = lista_original[0]
for e in lista_original:
    if e > numero_mas_grande:
        numero_mas_grande = e

# Sobre la lista inversa, buscamos el numero mas pequeño
numero_mas_peque = lista_inversa[0]
for e in lista_inversa:
    if e < numero_mas_peque:
        numero_mas_peque = e

print("Lista original: ", lista_original)
print("Lista inversa: ", lista_inversa)
print("Numero más grande: ", numero_mas_grande)
print("Numero más pequeño: ", numero_mas_peque)
