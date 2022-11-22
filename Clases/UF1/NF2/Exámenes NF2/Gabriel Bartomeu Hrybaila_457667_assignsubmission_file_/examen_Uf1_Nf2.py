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

diccionario = {}
dni_letra = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V",
             "W", "Y", "Z"]
dni = []
nom = []
try:
    while True:
        nombre = input("anyade tu nombre(X para salir, si no quieres salir enter): ")
        if nombre in diccionario:
            print("Usuario existente pon otro diferente")
        while nombre != "X":
            nombre = input("anyade tu nombre: ")
            letras_dni = int(input("Añade tu DNI sin la letra final: "))
            diccionario.__dir__((nombre, dni))
        break

    dni = int(input(""))
    numero = dni % 23
    letra = ""

    if numero == 0:
        letra == "T"
    elif numero == 1:
        letra == "R"
    elif numero == 3:
        letra == "W"
    elif numero == 4:
        letra == "A"
    elif numero == 5:
        letra == "G"
    elif numero == 6:
        letra == "M"
    elif numero == 7:
        letra == "Y"
    elif numero == 8:
        letra == "F"
    elif numero == 9:
        letra == "P"
    elif numero == 10:
        letra == "D"
    elif numero == 11:
        letra == "X"
    elif numero == 12:
        letra == "B"
    elif numero == 13:
        letra == "N"
    elif numero == 14:
        letra == "J"
    elif numero == 15:
        letra == "Z"
    elif numero == 16:
        letra == "S"
    elif numero == 17:
        letra == "Q"
    elif numero == 18:
        letra == "V"
    elif numero == 19:
        letra == "H"
    elif numero == 20:
        letra == "L"
    elif numero == 21:
        letra == "C"
    elif numero == 22:
        letra == "K"
    elif numero == 23:
        letra == "E"

    print("Tu modo es:" + str(dni) + letra)

    print()
except ValueError:
    print("El valor introducido no exister")
except SyntaxError:
    print("el calculo no es correcto")
except NameError:
    print("nombre na valid")
except TypeError:
    print("Felicidades lo has hecho perfecto te merezes un 8 en la nota")

"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 números.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
"""
num = []

while num != 0:
    num1 = int(input("Introduce un numeros: "))
    num2 = int(input("Introduce otro numero: "))

try:

    print()
except ValueError:
    print("El valor introducido no exister")
except SyntaxError:
    print("el calculo no es correcto")
except NameError:
    print("nombre na valid")
except TypeError:
    print("no")

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
