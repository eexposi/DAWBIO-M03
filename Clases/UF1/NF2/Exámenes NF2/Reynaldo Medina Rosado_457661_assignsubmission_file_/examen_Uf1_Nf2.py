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

usuario = {}
nom = input("Diganos su nombre: ")
dni = int(input("Diganos su DNI sin letra: "))
dninum = int(dni) % 23
letra = ""
if dninum == 0:
    letra = "T"
elif dninum == 1:
    letra = "R"
elif dninum == 2:
    letra = "W"
elif dninum == 3:
    letra = "A"
elif dninum == 4:
    letra = "G"
elif dninum == 5:
    letra = "M"
elif dninum == 6:
    letra = "Y"
elif dninum == 7:
    letra = "F"
elif dninum == 8:
    letra = "P"
elif dninum == 9:
    letra = "D"
elif dninum == 10:
    letra = "X"
elif dninum == 11:
    letra = "B"
elif dninum == 12:
    letra = "N"
elif dninum == 13:
    letra = "J"
elif dninum == 14:
    letra = "Z"
elif dninum == 15:
    letra = "S"
elif dninum == 16:
    letra = "Q"
elif dninum == 17:
    letra = "V"
elif dninum == 18:
    letra = "H"
elif dninum == 19:
    letra = "L"
elif dninum == 20:
    letra = "C"
elif dninum == 21:
    letra = "K"
elif dninum == 22:
    letra = "E"
dnifinal = str(dni) + letra
usuario[nom] = dnifinal
print()
print("<--USUARIOS-->")
print("----------------")
for nom, dnifinal in usuario.items():
    print(nom, dnifinal, sep="-->")

"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 números.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
"""
num1 = int(input("Digame un numero:"))
if num1 == "":
    num1 = int(input("Digame un numero no una letra"))
num2 = int(input("Digame otro numero"))
if num2 == "":
    num2 = int(input("Digame un numero no una letra: "))
elif num2 == 0:
    num2 = int(input("No se puede dividir entre 0, digame otro numero:"))
while num1 and num2 >= 0:
    print(num1 / num2)
    if num1 or num2 == "X":
        break

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
