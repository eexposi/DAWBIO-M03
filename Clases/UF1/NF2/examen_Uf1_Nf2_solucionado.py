"""EXAMEN NF2"""
""" 
EXAMEN NF2 - MATRICES, DICCIONARIOS Y CONTROL DE ERRORES --------------------------------------------

-----------------------------------------------------------
EJERCICIO 1  ----------------------------------------------
-----------------------------------------------------------
- Pedir al usuario su nombre y su DNI sin letra.
- Crear un diccionario con la key : nombre y el value : DNI con la letra.
- Mostrar todos los datos en forma de tabla.

                    Usuarios
                    ---------
                    Nombre --> XXXXXXXX-X

Las letras son: TRWAGMYFPDXBNJZSQVHLCKE
Y las letras se relacionan del 0 al 22:
0 = T
1 = R
2 = W
etc...

"""
LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"
dicc = {}
todo_correcto = False
while todo_correcto == False:
    try:
        nombre = input("Indicame tu nombre: ")
        dni_sinletra = input("Indica el DNI sin letra: ")
        if len(nombre) < 1:
            raise Exception("El nombre es incorrecto.")
        elif dni_sinletra[len(dni_sinletra) - 1].isalpha():
            raise Exception("Has puesto la letra, inútil")
        elif len(dni_sinletra) != 8:
            raise Exception("El DNI tiene una longitud incorrecta. Vigila que no hayas puesto la letra.")
        else:
            print("Los datos introducidos son correctos.")
            todo_correcto = True
    except Exception as error:
        print(error)

if todo_correcto == True:
    todo_correcto = False
    try:
        letra = LETRAS[int(dni_sinletra) % 23]
        dni_completo = dni_sinletra + letra
        dicc[nombre] = dni_completo
        todo_correcto = True
    except Exception as error:
        print(error)

if todo_correcto == True:
    try:
        print("  Usuarios")
        print("  --------")
        for key in dicc:
            print(key, dicc[key], sep=" ---- ")
    except Exception as error:
        print(error)

"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 números.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
"""

try:
    while True:
        n1 = int(input("Número 1: "))
        if n1 == "X":
            break
        else:
            n2 = int(input("Número 2: "))
            print("El resultado es ", str(n1 / n2))
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("invalid literal for int() with base 10")
except Exception as e:
    print(e)

"""
-----------------------------------------------------------
EJERCICIO 3: HUNDIR LA FLOTA ------------------------------
-----------------------------------------------------------
El código va a crear un tablero de 4x4 y va a colocar 2 barcos en él. El código debe permitir, fácilmente, cambiar
la posición de los barcos antes de lanzar el programa.

# Antes de empezar a jugar:
- Creamos un tablero de 4x4 vacío ('A')
- Colocamos 2 barcos (posición con 'B'), uno de 2 celdas y otro de 3 celdas (horizontal o vertical pero que no solapen)

# Al iniciar el programa...
- Mostrar el menú de juego (diccionario o lista) y tablero inicial con los barcos:
        1 - Jugar
        0 - Salir
- En random, hacemos tiradas:
    - devolver posición de la tirada
    - devolver agua (cambiar la casilla vacía 'A' por 'X') o tocado (cambiar la casilla de barco 'B' por 'T')
    - devolver estado del tablero
    - Esperar 'ENTER' para siguiente tirada
- Al completar 6 tiradas, deberemos devolver un mensaje según si hemos conseguido hundir todos los barcos o no


EJEMPLO DEL 1ER TURNO ----------------------------------------------------
-  Mostramos el tablero al empezar el juego:
           0 1 2 3
         0 A B B A
         1 A A A B
         2 A A A B
         3 A A A B

- Vemos las posiciones del disparo:
    Se dispara en la posicion x: 0 y: 1
    Tocado!

- Mostramos el tablero con las modificaciones:
           0 1 2 3
         0 A T B A
         1 A A A B
         2 A A A B
         3 A A A B
- Esperamos al siguiente turno:   "Pulsa ENTER para continuar..."

--------------------------------------------------------------------------------------------------- """
import random

while True:
    menu = ["Salir", "Jugar"]
    tablero = [["A", "A", "A", "A"], ["A", "A", "A", "A"], ["A", "A", "A", "A"], ["A", "A", "A", "A"]]
    barcos = 5
    tiradas = 6

    barco1 = [[0, 0], [1, 0]]
    barco2 = [[2, 1], [2, 2], [2, 3]]

    for i in range(len(barco1)):
        tablero[barco1[i][0]][barco1[i][1]] = "B"
    for i in range(len(barco2)):
        tablero[barco2[i][0]][barco2[i][1]] = "B"

    print("\nTablero inicial: ")
    for columna in range(len(tablero)):
        for fila in range(len(tablero[i])):
            print(tablero[columna][fila], end=" ")
        print()

    print(" Menú:")
    for i in range(len(menu)):
        print(i, menu[i], sep="-")
    try:
        opcion = int(input("Selecciona opción: "))

        if opcion == 0:
            print("Has salido de la partida.")
            break

        elif opcion == 1:
            while tiradas > 0 and barcos > 0:
                x = random.randint(0, 3)
                y = random.randint(0, 3)
                print("Posición de tirada: x=", x, "y=", y)
                if tablero[x][y] == "A":
                    print("Agua")
                    tablero[x][y] = "X"
                    tiradas -= 1
                elif tablero[x][y] == "B":
                    print("Tocado!")
                    tablero[x][y] = "T"
                    tiradas -= 1
                    barcos -= 1
                elif tablero[x][y] == "X" or tablero[x][y] == "T":
                    print("Repite tirada")

                print()
                for columna in range(len(tablero)):
                    for fila in range(len(tablero[i])):
                        print(tablero[columna][fila], end=" ")
                    print()
                input("Pulsa una tecla para volver a tirar...")

            if barcos == 0:
                print("Has ganado!")
            if tiradas == 0 and barcos > 0:
                print("La partida ha finalizado!")
        else:
            raise Exception("¡La opción no es correcta!")
    except Exception as e:
        print("¡La opción no es correcta!")
