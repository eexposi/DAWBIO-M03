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

# dict={ 0:"T",1:"R",2:"W",3:"A",4:"G", 5:"M", 6:"Y", 7:"F", 8:"P", 9:"D", 10:"X", 11:"B"
#       , 12:"N", 13:"J", 14:"Z", 15:"S", 16:"Q", 17:"V", 18:"H", 19:"L", 20:"C", 21:"K", 22:"E"}

# nombre=input("Inserte su nombre: ")
# DNI = int(input("Indique los 8 digitos de su DNI: "))
# DN= DNI % 23
# Letra = "  "
# for i in range(len(dict) ):
#     for j in range(len(dict[i])):
#             dict[nombre]=DNI               
#     if DN == 0:
#       Letra = " T"
#     elif DN== 1:
#       Letra = " R"
#     elif DN == 2:
#       Letra = " W"
#     elif DN == 3:
#       Letra = " A"
#     elif DN == 4:
#       Letra = " G"
#     elif DN == 5:
#       Letra = " M"
#     elif DN == 6:
#       Letra = " Y"
#     elif DN == 7:
#       Letra = " F"
#     elif  DN == 8:
#       Letra = " P"
#     elif  DN == 9:
#       Letra = " D"
#     elif DN == 10:
#       Letra = " X"
#     elif DN == 11:
#       Letra = " B"
#     elif DN == 12:
#       Letra = " N"
#     elif DN == 13:
#       Letra = " J"
#     elif DN == 14:
#       Letra = " Z"
#     elif DN == 15:
#       Letra = " S"
#     elif DN == 16:
#       Letra = " Q"
#     elif DN == 17:
#       Letra = " V"
#     elif DN == 18:
#       Letra = "H"
#     elif DN == 19:
#       Letra = " L"
#     elif DN == 20:
#       Letra = " C"
#     elif DN == 21:
#       Letra = " K"
#     elif DN == 22:
#       Letra = " E"

# print("   usuario\n    ---------\n" +str(nombre)+ "--->" +str(DNI)+"-" + str(Letra))


"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 números.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
"""

# while True:
#   numero_1=input("Indique su primer numero: ")
#   if numero_1 == "X":
#         break
#   numero_2=input("Indique su segundo numero: ")
#   N=int(numero_1) * int(numero_2)
#   print(N)


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
