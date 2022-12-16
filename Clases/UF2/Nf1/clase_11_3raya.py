"""
TODO
- Menu (jugar, salir)
- Printar tablero
- Elegir X o O
- Tirada IA
- Fin juego
"""
import random

MENU = ["Salir", "Jugar"]
marca = "X"
tablero = [[" - ", " - ", " - "],
           [" - ", " - ", " - "],
           [" - ", " - ", " - "]
           ]


def get_seleccion(MENU):
    """
    Muestra el menu y devuelve la opcion seleccionada.
    :param MENU: Lista con las opciones del menu
    :return: opcion escogida por el usuario
    """
    for i in range(len(MENU)):
        print(i, MENU[i], sep=" - ")
    seleccion = int(input("Seleccione una opción: "))
    return seleccion


def decir_adios():
    print("Adios")


def mostrar_tablero(tablero):
    """
    Muestra el tablero de juego
    :param tablero: matriz, donde esta el tablero
    """
    print("-------TABLERO--------")
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end="")
        print()
    print()


def tirada_random(rango):
    """
    Genera un numero aleatorio
    :param rango: numero maximo del random, del 0 al rango
    :return: numero aleatorio dentro del rango
    """
    numero = random.randint(0, rango)
    return numero


def add_tirada(tablero, X, Y, marca):
    """
    modifica el valor de la posicion de la tirada
    :param tablero: tablero de juego
    :param X: posicion x de la tirada
    :param Y: posicion y de la tirada
    :param marca: marca que muestra la posicion
    :return: tablero modificado
    """
    tablero[X][Y] = " " + marca + " "
    return tablero


def check_fin(num_tiradas):
    """
    Comprobara si hemos acabado el juego
    :param num_tiradas: tiradas actuales
    :return: si es fin o no.
    """
    if num_tiradas >= 5:
        fin = True
    else:
        fin = False
    return fin


def jugar(tablero, marca):
    fin_juego = False
    num_tiradas = 0
    while fin_juego == False:
        rango = len(tablero) - 1
        mostrar_tablero(tablero)
        tiradaX = tirada_random(rango)
        tiradaY = tirada_random(rango)
        tablero = add_tirada(tablero, tiradaX, tiradaY, marca)
        fin_juego = check_fin(num_tiradas)
        num_tiradas += 1


def seleccionar_marca():
    """
    Selecciona la marca de juego
    :return: la marca
    """
    mar = input("Seleccionar la marca: (X o O)")
    return mar


opcion = get_seleccion(MENU)
if opcion == 0:
    decir_adios()
elif opcion == 1:
    marca = seleccionar_marca()
    jugar(tablero, marca)
else:
    print("Te has equivocado")
