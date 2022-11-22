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
num%23
"""
try:
    ValueError
except:
    False
nom = input("Escriba su nombre --> ")
dni = int(input("Escriba su DNI --> "))
n = int(dni % 23)
Usuario = {}
Usuario[nom] = dni
letra = ""
if n == 0:
    letra = "T"
elif n == 1:
    letra = "R"
elif n == 2:
    n = "W"
elif n == 3:
    letra = "A"
elif n == 4:
    letra = "G"
elif n == 5:
    letra = "M"
elif n == 6:
    letra = "Y"
elif n == 7:
    letra = "F"
elif n == 8:
    letra = "P"
elif n == 9:
    letra = "D"
elif n == 10:
    letra = "X"
elif n == 11:
    letra = "B"
elif n == 12:
    letra = "N"
elif n == 13:
    letra = "J"
elif n == 14:
    n = "Z"
elif n == 15:
    letra = "S"
elif n == 16:
    letra = "Q"
elif n == 17:
    letra = "V"
elif n == 18:
    letra = "H"
elif n == 19:
    letra = "L"
elif n == 20:
    letra = "C"
elif n == 21:
    letra = "K"
elif n == 22:
    letra = "E"
letra = str(dni) + ("-") + str(letra)
print("Usuarios\n---------")
for nom, n in Usuario.items():
    print(nom, letra, sep="-->")
print(ValueError)

"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 números.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
"""
print("Escoja dos números para dividir: ")
num1 = int(input("Primer Valor: "))
num2 = int(input("Segundo Valor: "))
div = num1 / num2
while num1 != "X":
    div
    print("Resultado de la división", div)
    print("Escriba X para no dividir más o dele a la tecla Enter para seguir: ")
    num1 = int(input("Primer Valor: "))
    if num1 == "X":
        print("Ha decidido parar")
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
