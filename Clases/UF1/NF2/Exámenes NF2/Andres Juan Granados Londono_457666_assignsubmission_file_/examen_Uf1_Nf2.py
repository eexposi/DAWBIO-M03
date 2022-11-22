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
#divide 23
"""

letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K",
          "E"]
diccionario = {}
while True:
    nombre = input("Dime tu nombre: ")
    dni = int(input("dime tu dni: "))
    diccionario["nombre"] = nombre
    diccionario["dni"] = [dni]
    operacion = dni % 23
    print(operacion)
    if operacion == 0:
        diccionario["dni"].append(letras[0])
    elif operacion == 1:
        diccionario["dni"].append(letras[1])
    elif operacion == 2:
        diccionario["dni"].append(letras[2])
    elif operacion == 3:
        diccionario["dni"].append(letras[3])
    elif operacion == 4:
        diccionario["dni"].append(letras[4])
    elif operacion == 5:
        diccionario["dni"].append(letras[5])
    elif operacion == 6:
        diccionario["dni"].append(letras[6])
    elif operacion == 7:
        diccionario["dni"].append(letras[7])
    elif operacion == 8:
        diccionario["dni"].append(letras[8])
    elif operacion == 9:
        diccionario["dni"].append(letras[9])
    elif operacion == 10:
        diccionario["dni"].append(letras[10])
    elif operacion == 11:
        diccionario["dni"].append(letras[11])
    elif operacion == 12:
        diccionario["dni"].append(letras[12])
    elif operacion == 13:
        diccionario["dni"].append(letras[13])
    elif operacion == 14:
        diccionario["dni"].append(letras[14])
    elif operacion == 15:
        diccionario["dni"].append(letras[15])
    elif operacion == 16:
        diccionario["dni"].append(letras[16])
    elif operacion == 17:
        diccionario["dni"].append(letras[16])

    elif operacion == 18:
        diccionario["dni"].append(letras[16])

    elif operacion == 19:
        diccionario["dni"].append(letras[16])
    elif operacion == 20:
        diccionario["dni"].append(letras[16])

    elif operacion == 21:
        diccionario["dni"].append(letras[16])
    elif operacion == 22:
        diccionario["dni"].append(letras[16])
        print(diccionario)
    break

print("Usuarios")
print("--------")
print(diccionario["nombre"], diccionario["dni"][:])

"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 números.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
"""
valor = ""
while valor != "X":
    try:
        valor = int(input("introduce un numero: "))
        if valor == "X":

            valor = "X"

        elif valor < 0:
            raise Exception
        valor2 = int(input("introduce otro numero: "))
        if valor < 0:
            raise Exception
        total = float(valor / valor2)

        print("la divicion de estos dos numero es: ", total)


    except ZeroDivisionError:
        print("No puedes dividir entre cero")
    except ValueError:
        print("El numero introducido es invalido ")
    except Exception as error:
        print("no se usan numero negativos")
    except:
        print("no se que ha pasado")

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

menu = {1: 'jugar', 0: 'salir'}
tablero = [["A"], ["A"], ["A"], ["A"]]
for x in range(len(menu)):
    print(x, menu[x], sep="-")
opcion = int(input("escoge una opcion: "))

if opcion == 1:
    while True:
        tiro1 = random.randint(1, 4)
        tablero[tiro1][0] = "X"
        for x in range(len(tablero)):
            print(x, tablero[x])
            break
