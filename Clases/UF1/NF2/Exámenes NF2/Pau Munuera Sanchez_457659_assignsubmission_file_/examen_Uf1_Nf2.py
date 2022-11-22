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
# Ejercicio 1
diccionario = {}
letras = "TRWAGMYFPDXBNJZSQVHLCKE"
continuar = True
while continuar:
    name = input("Introduce un nombre: ")
    dniincompleto = int(input("Introduce el dni sin letra: "))
    numdni = dniincompleto % 23
    if numdni == 0:
        letradni = "T"
    if numdni == 1:
        letradni = "R"
    if numdni == 2:
        letradni = "w"
    if numdni == 3:
        letradni = "A"
    if numdni == 4:
        letradni = "G"
    if numdni == 5:
        letradni = "M"
    if numdni == 6:
        letradni = "Y"
    if numdni == 7:
        letradni = "F"
    if numdni == 8:
        letradni = "P"
    if numdni == 9:
        letradni = "D"
    if numdni == 10:
        letradni = "X"
    if numdni == 11:
        letradni = "B"
    if numdni == 12:
        letradni = "N"
    if numdni == 13:
        letradni = "J"
    if numdni == 14:
        letradni = "Z"
    if numdni == 15:
        letradni = "S"
    if numdni == 16:
        letradni = "S"
    if numdni == 17:
        letradni = "Q"
    if numdni == 18:
        letradni = "V"
    if numdni == 19:
        letradni = "H"
    if numdni == 20:
        letradni = "L"
    if numdni == 21:
        letradni = "C"
    if numdni == 22:
        letradni = "K"
    if numdni == 23:
        letradni = "E"
    dnicompleto = dniincompleto, letradni
    diccionario[name] = dnicompleto
    continuar = input("¿Quieres añadir mas usuarios (Si/No)? ") == "Si"
print()
print("usuarios")
print("---------")
for name, dni in diccionario.items():
    print(name, dni, sep=' --> ')
print()

"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 números.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
"""
n1 = 0
n2 = 0
try:
    while n1 != "X":
        n1 = input("Dime un numero: ")
        n2 = input("Dime otro numero: ")
        print("La division entre los 2 numeros da: ", float(n1) / float(n2))
except:
    print("El valor introducido no es un float o estas dividiendo entre 0")

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
