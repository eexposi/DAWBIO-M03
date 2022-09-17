"""Clase 23 sept. 2022"""
""" ITERACIONES 


WHILE
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
