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

Name = input("Entra su nombre: ")
DNI = int(input("Introduce su DNI sin la letra: "))
letter = (DNI % 23)
if letter == 0:
    X = "T"
elif letter == 1:
    X = "R"
elif letter == 2:
    X = "W"
elif letter == 3:
    X = "A"
elif letter == 4:
    X = "G"
elif letter == 5:
    X = "M"
elif letter == 6:
    X = "Y"
elif letter == 7:
    X = "F"
elif letter == 8:
    X = "P"
elif letter == 9:
    X = "D"
elif letter == 10:
    X = "X"
elif letter == 11:
    X = "B"
elif letter == 12:
    X = "N"
elif letter == 13:
    X = "J"
elif letter == 14:
    X = "Z"
elif letter == 15:
    X = "S"
elif letter == 16:
    X = "Q"
elif letter == 17:
    X = "V"
elif letter == 18:
    X = "H"
elif letter == 19:
    X = "L"
elif letter == 20:
    X = "C"
elif letter == 21:
    X = "K"
elif letter == 22:
    X = "E"
else:
    print("El numero del DNI no es correcta.")

DNI_completo = str(DNI) + "-" + X
dictionary = {}
dictionary[Name] = DNI_completo
print("Usuarios")
print("---------")
print(Name, dictionary[Name], sep='--->')
print()

"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 números.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
"""
while True:

    try:
        num1 = int(input("Entra el primero numero: "))
        num2 = int(input("Entra el segundo numero: "))
        division = num1 / num2
        print(division)

    except ValueError:
        print("El numero en algunos de dos input no es un numero correcta.", num1 == "X")

    except SyntaxError:
        print("El sintax en el input no es correcta.")

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

tablero = []

print("Menu")
print("-------")
print("1 - Jugar")
print("2 - Salir")
option = input("Choose an option: ")
