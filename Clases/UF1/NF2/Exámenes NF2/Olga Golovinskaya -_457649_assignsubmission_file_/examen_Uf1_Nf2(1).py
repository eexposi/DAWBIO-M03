"""EXAMEN NF2

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
dictionary = {}
letras = "TRWAGMYFPDXBNJZSQVHLCKE"

while True:
    try: 
        nombre = input("Entra tu nombre: ")
 
        if nombre == "X":
            break
        spaces = nombre.replace(" ","")
        print(spaces)
        if spaces.isalpha():
            try:
                dni = int(input("Entra los numeros de tu DNI: "))
                letrapos= dni % 23
                dnicompleto = str(dni) + "-" + str(letras[letrapos])
                dictionary[nombre]= dnicompleto
            except ValueError:
                print("El dni no es valido")
        else:
            raise Exception
    except Exception as error:
        print("El nombre no es valido")
print(dictionary)
if len(dictionary) >= 1:
    print("Usuarios")
    print("-----------")
    for key, value in dictionary.items():
        print(key, value, sep = "-->")

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
        num1 = input("Entra el primer numero: ")
        if num1 == "X":
            break
        num2 = input("Entra el segundo numero: ")
        resultat = int(num1) / int(num2)
        print ("El resultado se division es: ", resultat)
    except ValueError:
        print("Los numeros introducidos deberian ser de digitos ")
    except ZeroDivisionError:
            print("No se puede dividir en zero")
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

--------------------------------------------------------------------------------------------------- 
"""
import random

tabla =[["A", "A", "A", "A"],["A", "B", "B", "A"],["A", "A", "A", "A"],["B", "B", "B", "A"]]
tablaposicion = [[" ",0,1,2,3],[0,"A", "A", "A", "A"],[1,"A", "B", "B", "A"],[2,"A", "A", "A", "A"],[3,"B", "B", "B", "A"]]
tiradas = 0
result = 0
while True:
    for i in tablaposicion:
        print(i[0],i[1],i[2],i[3],i[4])
    menu = ["1 - Jugar", "2 - Salir"]
    for i in menu:
        print(i)
    try:
        opcion = int(input("Entra una opcion: "))
        if opcion == 2:
            break
        if opcion == 1: 
            tiradas += 1
            print("Numero de tiradas = ", tiradas)
            print ("Empieza el juego")
            x = random.randint(0,3)
            y = random.randint(0,3)
            print(x,y)
            print("Se dispara en la posicion x: ", x , "y: ", y)
            if tabla[x][y]=="B":
                tabla[x][y] = "T"
                print("Tocado!")
                result+= 1
                a = input("Pulsa ENTER para continuar...")
                if a == " ":
                    pass
                else:
                    print("Has tenido exito", result, "veces" )
                    break
            if tiradas == 6:
                print("Has jugado 6 veces  y has tenido exito", result, "veces" )
                break
        else:
            print("El numero de opción introducido no es valido")
    except ValueError:
        print("Deberias introducir 1 o 2")