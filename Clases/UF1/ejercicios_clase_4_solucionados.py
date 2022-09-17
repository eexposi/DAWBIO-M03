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
salir = False

while salir != True:
    print(opc0)
    print(opc1)
    print(opc2)
    resposta = int(input("Elija su opcion: "))
    if resposta == 0:
        salir = True
        print("Adios")
    elif resposta == 1:
        print("Genial, has elegido la opcion 1")
    elif resposta == 2:
        print("Genial, has elegido la opcion 2")
    else:
        print("No has elegido ninguna opcion correcta.")
