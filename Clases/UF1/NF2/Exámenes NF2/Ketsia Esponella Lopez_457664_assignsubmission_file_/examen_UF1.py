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
try:
    usuarios = {}
    letra = ""
    nombre = input("Introduce tu nombre: ")
    if nombre not in usuarios:
        dni = int(input("Introduce tu DNI. Sin la letra: "))
        usuarios[nombre] = dni
        letra = dni % 23
        if letra == 0:
            letra = "T"
        elif letra == 1:
            letra = "R"
        elif letra == 2:
            letra = "w"
        elif letra == 3:
            letra = "A"
        elif letra == 4:
            letra = "G"
        elif letra == 5:
            letra = "M"
        elif letra == 6:
            letra = "Y"
        elif letra == 7:
            letra = "F"
        elif letra == 8:
            letra = "P"
        elif letra == 9:
            letra = "D"
        elif letra == 10:
            letra = "X"
        elif letra == 11:
            letra = "B"
        elif letra == 12:
            letra = "N"
        elif letra == 13:
            letra = "J"
        elif letra == 14:
            letra = "Z"
        elif letra == 15:
            letra = "S"
        elif letra == 16:
            letra = "Q"
        elif letra == 17:
            letra = "V"
        elif letra == 18:
            letra = "H"
        elif letra == 19:
            letra = "L"
        elif letra == 20:
            letra = "C"
        elif letra == 21:
            letra = "K"
        elif letra == 22:
            letra = "E"
        else:
            print("El n??mero no es correcto")
    print("Usuarios")
    print("---------")
    print(nombre, usuarios[nombre], letra)
except ValueError:
    print("Valor introducido incorrecto")
except (SyntaxError, NameError):
    print("Error en el c??digo")
except:
    print("Algo ha ido mal.")
"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISI??N ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 n??meros.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la divisi??n entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
"""
n1 = ""
n2 = 0
while n1 != "X":
    try:
        n1 = input("Introduce un n??mero. (Si no quieres continuar introduce una X): ")
        if n1 != "X":

            n1 = float(input("Introduce un n??mero: "))
            n2 = float(input("Introduce otro n??mero: "))
            if n2 > n1:
                print("El segundo n??mero tiene que ser menor al primer n??mero introducido")
            else:
                resultado = n1 / n2
            print("El resultado de la divisi??n entre: " + str(n1) + " y " + str(n2) + " es: " + str(resultado))
        print("aaaa")

    except ZeroDivisionError:
        print("No se puede dividir un n??mero por 0")
    except (SyntaxError, NameError):
        print("Error en el c??digo")
    except ValueError:
        print("El valor introducido no es correcto")
    except:
        print("Algo ha ido mal")
        """
-----------------------------------------------------------
EJERCICIO 3: HUNDIR LA FLOTA ------------------------------
-----------------------------------------------------------
El c??digo va a crear un tablero de 4x4 y va a colocar 2 barcos en ??l. El c??digo debe permitir, f??cilmente, cambiar
la posici??n de los barcos antes de lanzar el programa.

# Antes de empezar a jugar:
- Creamos un tablero de 4x4 vac??o ('A')
- Colocamos 2 barcos (posici??n con 'B'), uno de 2 celdas y otro de 3 celdas (horizontal o vertical pero que no solapen)

# Al iniciar el programa...
- Mostrar el men?? de juego (diccionario o lista) y tablero inicial con los barcos:
        1 - Jugar
        0 - Salir
- En random, hacemos tiradas:
    - devolver posici??n de la tirada
    - devolver agua (cambiar la casilla vac??a 'A' por 'X') o tocado (cambiar la casilla de barco 'B' por 'T')
    - devolver estado del tablero
    - Esperar 'ENTER' para siguiente tirada
- Al completar 6 tiradas, deberemos devolver un mensaje seg??n si hemos conseguido hundir todos los barcos o no


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

menu = ["Jugar", "Salir"]
tablero = [[" ", 0, 1, 2, 3], [0, "A", "B", "B", "A"], [1, "A", "A", "A", "B"], [2, "A", "A", "A", "B"],
           [3, "A", "A", "A", "B"]]

winner = 0
opt = 0

while opt != 0:
    correcto = False
    correcto2 = False
    for i in range(len(menu)):
        print(i, menu[i], sep="-")
    print()
    if winner < 9:
        opcion = input("Elige una opci??n: ")
        for i in range(0, len(tablero)):
            for j in range(len(tablero[i])):
                print(tablero[i][j], end="")
            print()
            if opcion == "1":
                while correcto == False:
                    fila = random.randint(1, 4)
                    if fila < 0 or fila > 4:
                        print("El n??mero de fila es incorrecto.")
                    else:
                        correcto = True

                while correcto2 == False:
                    columna = random.randint(1, 4)
                    if columna < 0 or columna > 4:
                        print("El n??mero de fila es incorrecto.")
                    else:
                        correcto2 = True

                    if tablero[fila][columna] == "A":
                        tablero[fila][columna] = "X"
                        winner += 1
                        print("Se dispara en la posici??n:" + fila)
                    elif tablero[fila][columna] == "B":
                        tablero[fila][columna] = "T"
                        winner += 1
            elif opcion == "0":
                print("Adi??s")
                break
            else:
                print("Opcion incorrecta")
                correcto = True
