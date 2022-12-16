#
# """
# TODO
# - Pedir la frase
# - Quitar "e"
# - Mostrar resultados
# """
#
# # Laura
# def quitar_letra(frase, letra):
#     result = ""
#     for i in frase:
#         if i != letra:
#             result += i
#     return result
#
# # Sergio
# # Pedir la frase
# frase = "pedir la frase"
# # Quitar la e
# resultado_frase = quitar_letra(frase, "e")
# # Mostrar frase sin e
# print(resultado_frase)

"----"
"""
- Pediremos al usuario numeros de forma indefinida hasta que
 ingrese el 999, y se iran guardando en una lista
 """

"""
TODO
- crear lista vacia
- Pedir numeros
- Guardar en lista
- Mostrar
"""

#
# # Ketsia
# def pedir_num():
#     lista = []
#     num = 0
#     while num != 999:
#         num = int(input("Introduce un numero: "))
#         lista.append(num)
#     return lista
#
#
# def mostrar_lista(lista):
#     print(lista)
#
# lista = pedir_num()
# mostrar_lista(lista)

"""EJERCICIO 1
- Solicitaremos al usuario un numero mayor que 1 y menor que 100.
 Este número serán los bloques.
- Si el numero no cumple estos requisitos, volveremos a solicitarlo.
- Haremos una piramide usando el número de bloques como base.


- Ejemplo de piramide para 6 bloques:
*
**
***
****
*****

NOTA: No se podrán utilizar funciones, listas o métodos no 
explicados en clase
"""

"""
TODO
- pedir numero
- mostramos la piramide

"""


def piramide(num):
    cont = num
    for i in range(num):
        cont -= 1
        print("*", end="")
        for j in range(cont):
            print("*", end="")
        print()


numero = int(input("Numero: "))

piramide(numero)
