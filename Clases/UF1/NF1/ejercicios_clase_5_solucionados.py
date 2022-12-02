"""EJERCICIOS Clase 27 de spetiembre 2022"""

"""EJERCICIO 3
- Pediremos al usuario numeros de forma indefinida hasta que
 ingrese el 999, y se iran guardando en una lista
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
"""
EJERCICIO 5
-------------

NOTA: Se comparan los 2 primeros numeros y se ordenan.
Luego se comprueban los numeros 2 y 3 y se ordenan.
Sucesivamente hasta que no hayan mas cambios

Haremos un calculo de la campana de Gauss.
- Con la lista dada, ordenaremos los valores de menor a mayor
- Crearemos una nueva lista sin el primer y ultimo resultado
    Usar [:]
- Indicaremos cual es el valor medio (el que se encuentra en
la mitad, no la media).
- Mostraremos todos los valores por debajo como Suspendidos
y por encima como aprobados.

lista_original = [0, 1, 3, 7, 9, 4, 5, 5, 5, 6, 9, 10, 10, 0, 3, 4, 5, 6]

SALIDA
Lista original
lista ordenada
Lista sin los numeros inicial/final
Valor medio
Valor mas repetido
Lista de aprobados y suspendidos
"""
# Creamos lista original
lista_original = [0, 1, 3, 7, 9, 4, 5, 5, 5, 6, 9, 10, 10, 0, 3, 4, 6]
lista_ordenada = lista_original[:]

# Ordenamos la lista
hay_cambios = True
while hay_cambios:
    hay_cambios = False
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] > lista_ordenada[i + 1]:
            hay_cambios = True
            lista_ordenada[i], lista_ordenada[i + 1] = lista_ordenada[i + 1], lista_ordenada[i]

# Creamos la lista filtrada sin el primer/ultimo
lista_gauss = lista_ordenada[1:len(lista_ordenada) - 1]

# Calculamos el valor medio
punto_medio = len(lista_gauss) // 2

# Creamos la lista de los supensos
lista_suspensos = lista_gauss[0:(punto_medio - 1)]
# Creamos la lista de los aprobados
lista_aprobados = lista_gauss[punto_medio:len(lista_gauss)]

print("Lista original: " + str(lista_original))
print("Lista ordenada: " + str(lista_ordenada))
print("Lista gauss: " + str(lista_gauss))
print("El valor medio es: " + str(lista_gauss[punto_medio]))
print("Los suspensos son: ", lista_suspensos)
print("Los aprobados son: ", lista_aprobados)
