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
print("EJERCICIO 1")
letra1 = input("Dime tu la primera letra de tu dni")
letra2 = input("Dime tu la segunda letra de tu dni")
letra3 = input("Dime tu la tercera letra de tu dni")
letra4 = input("Dime tu la cuarta letra de tu dni")
letra5 = input("Dime tu la quinta letra de tu dni")
letra6 = input("Dime tu la sexta letra de tu dni")
letra7 = input("Dime tu la septima letra de tu dni")
letra8 = input("Dime tu la optava letra de tu dni")
if letra1 == "T":
    print("0")
    if letra1 == "R":
        letra1_2 = print("1")
if letra1 == "W":
    letra1_3 = print("2")
if letra1 == "A":
    letra1_4 = print("3")
if letra1 == "G":
    etra1_5 = print("4")
if letra1 == "M":
    letra1_6 = print("5")
if letra1 == "Y":
    letra1_7 = print("6")
if letra1 == "F":
    letra1_8 = print("7")
if letra1 == "P":
    letra1_9 = print("8")
if letra1 == "D":
    letra1_9 = print("9")
if letra1 == "X":
    letra1_10 = print("10")
if letra1 == "B":
    letra1_11 = print("11")
if letra1 == "N":
    letra1_12 = print("12")
if letra1 == "J":
    letra1_13 = print("13")
if letra1 == "Z":
    letra1_14 = print("15")
if letra1 == "S":
    letra1_15 = print("16")
if letra1 == "Q":
    letra1_16 = print("17")
if letra1 == "V":
    letra1_17 = print("18")
if letra1 == "H":
    letra1_18 = print("19")
if letra1 == "L":
    letra1_19 = print("20")
if letra1 == "C":
    letra1_20 = print("21")
if letra1 == "K":
    letra1_21 = print("22")
if letra1 == "E":
    letra1_22 = print("22")

"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 números.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
"""
print("EJERCICIO 2: CALCULADORA DE DIVISIÓN")
while True:
    try:
        dividir1 = (input("Introduce un numero para dividirlo por otro  "))
        if dividir1 == "X":
            print("Salir")
            break
        elif dividir1 != "X":
            dividir2 = (input("Indrucede otro numero para dividirlo por "))
        resultado = int(dividir1) / int(dividir2)
        print(resultado)
    except ZeroDivisionError:
        print("Estas intentado dividir por 0,intentelo de nuevo.")

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
print("EJERCICIO 3: HUNDIR LA FLOTA")
menu = ["jugar", "salir"]
m = [[" ", 0, 1, 2, 3], [0, "A", "A", "A", "A"], [1, "A", "A", "A", "A"],
     [2, "A", "A", "A", "A"][3, "A", "A", "A", "A"]]
anyadir = "B"
while True:
    print("---Menu---")
    for i in range(len(menu)):
        print(i, menu[i], sep=("-"))
    selecion = input("Seleciona una opcion del menu")
    if selecion == "0":
        print("Salir")
        break
    if selecion == "1":
        barco1 = input("Donde en que fila quires ñadir un el varco 1  ")
        barco1_2 = input("En que posicion  orizontal quieres añadir el varco")
        m[barco1][barco1_2]
        print(m)
