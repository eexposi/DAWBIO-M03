"""EXAMEN NF2"""
""" 
EXAMEN NF2 - MATRICES, DICCIONARIOS Y CONTROL DE ERRORES --

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
# Inicialización de variables y constantes
LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"
lista_alumnos = {
    "Pepe Gonzalez": "12345678Z",
    "Jorge Perez": "24681012B",
    "Marc García": "13579111A"
}
dni = 0
nombre = ""
letra = ""

# Boleano que mantiene al usuario hasta que introduzca bién los datos
fallado = True
while fallado == True:
    try:
        nombre = input("Introduce tu nombre completo: ")
        dni = int(input("Introduce tu DNI sin letra: "))
        letra = LETRAS[dni % 23]
        if dni < 0:  # DNI negativo
            raise Exception("ErrorCode:0")
        elif dni > 99999999:  # DNI con cifras de más
            raise Exception("ErrorCode:1")
        lista_alumnos[nombre] = str(dni) + letra
        fallado = False  # Si ningún Exception salta, el usuario puede salir del bucle
    except ValueError:
        print("Has introducido un valor incorrecto. Vuelve a introducir los datos.")
    except Exception as e:
        if str(e) == "ErrorCode:0":
            print("El DNI no tiene un valor correcto. Vuelve a introducir los datos.")
        elif str(e) == "ErrorCode:1":
            print("El DNI tiene más cifras de las necesarias. Vuelve a introducir los datos.")
        else:  # Detección de cualquier error no planteado
            print(
                "Ha ocurrido un error inesperado. Espere antes de volver a intentarlo, o contacte con el administrador.\nEn caso de contactar a servicio tecnico, porporcionar el siguiente mensaje: " + str(
                    e))

# Impresión de tabla por pantalla.
print("\n\nUsuarios\n---------")
for x in lista_alumnos:
    print(x + " --> " + lista_alumnos[x])
# Fila vacia extra
print()

"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 números.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la división entre ellos, gestionando todos los posibles
errores y mostrando por pantalla el error.
"""

# n --> Primer número / m --> Segundo número
n = 0
m = 0

while n != "X":
    try:
        # Codigo a repetir
        n = input("Introduce el primer número: ")
        if n == "X":
            break  # Acabar el bucle al detectar orden de cierre
        n = float(n)
        m = float(input("Introduce el segundo número: "))
        if m == 0:
            raise Exception("ErrorCode:0")
        print("El resultado de dividir " + str(n) + " y " + str(m) + " es " + str(n / m))
    # Errores a gestionar
    except ZeroDivisionError:
        print("No se puede dividir por 0. Vuelve a introducir los datos.")
    except ValueError:
        print("El dato introducido no es numerico. Vuelve a introducir los datos.")
    except Exception as e:
        if str(e) == "ErrorCode:0":
            print("No se puede dividir por 0. Vuelve a introducir los datos.")
print("Cerrando sesión. Gracias por usar nuestro divisor.")

"""
-----------------------------------------------------------
EJERCICIO 3: HUNDIR LA FLOTA ------------------------------
-----------------------------------------------------------
El código va a crear un tablero de 4x4 y va a colocar 2 barcos en él.
El código debe permitir, fácilmente, cambiar la posición
de los barcos antes de lanzar el programa.

# Antes de empezar a jugar:
- Creamos un tablero de 4x4 vacío ('A')
- Colocamos 2 barcos (posición con 'B'), uno de 2 celdas y
otro de 3 celdas (horizontal o vertical pero que no solapen)

# Al iniciar el programa...
- Mostrar el menú de juego (diccionario o lista) y tablero
inicial con los barcos:
        1 - Jugar
        0 - Salir
- En random, hacemos tiradas:
    - devolver posición de la tirada
    - devolver agua (cambiar la casilla vacía 'A' por 'X') o
    tocado (cambiar la casilla de barco 'B' por 'T')
    - devolver estado del tablero
    - Esperar 'ENTER' para siguiente tirada
- Al completar 6 tiradas, deberemos devolver un mensaje según si
hemos conseguido hundir todos los barcos o no


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

---------------------------------------------------------------------
"""
import random

menu = {
    "1": "Jugar",
    "0": "Salir"
}

# Comenta todos los tableros excepto el que se quiera jugar

tablero = [[" ", 0, 1, 2, 3], [0, "A", "B", "B", "A"], [1, "A", "A", "A", "B"], [2, "A", "A", "A", "B"],
           [3, "A", "A", "A", "B"]]
# tablero = [[" ", 0, 1, 2, 3],[0, "A", "B", "B", "A"],[1, "A", "B", "B", "A"],[2, "A", "A", "B", "A"],[3, "A", "A", "A", "A"]]
# tablero = [[" ", 0, 1, 2, 3],[0, "A", "A", "A", "A"],[1, "A", "A", "A", "A"],[2, "A", "A", "B", "B"],[3, "A", "B", "B", "B"]]
# tablero = [[" ", 0, 1, 2, 3],[0, "A", "A", "B", "B"],[1, "B", "B", "B", "A"],[2, "A", "A", "A", "A"],[3, "A", "A", "A", "A"]]


decision = -1

while decision != 0:
    # Imprimir Menu
    for x in menu:
        print(x, menu[x], sep=" - ")

    # Recoger decisión y gestionar errores
    fallado = True
    while fallado == True:
        try:
            decision = int(input("¿Qué desea hacer? "))
            if decision != 0 and decision != 1:
                raise ValueError

            fallado = False
        except ValueError:
            print("No ha introducido un valor esperado.")
        except:
            print("Ha ocurrido un error inesperado, contacte con soporte técnico.")

    # Jugar
    if decision == 1:
        print("-- Bienvenido a undir la flota ---\nEsta es la posición inicial:")
        # Imprimimos el tablero
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                print(tablero[j][i], end="   ")
            print("\n")
        input("Presiona enter para continuar...")  # Esperamos el enter
        iterador = 0
        tocados = 0
        while iterador < 6:
            print("Este es el tiro " + str(iterador + 1))
            # Calculamos tiro
            tiro_x = random.randint(1, 4)
            tiro_y = random.randint(1, 4)
            print("Se ha apuntado a la posición: " + str(tiro_x - 1) + "-" + str(tiro_y - 1) + ".")
            if tablero[tiro_x][tiro_y] == "T":
                print("La posición " + str(tiro_x - 1) + "-" + str(tiro_y - 1) + " ya ha sido tocada. Barco.")
            elif tablero[tiro_x][tiro_y] == "A":
                print("En la posición " + str(tiro_x - 1) + "-" + str(tiro_y - 1) + " no hay barcos.")
                tablero[tiro_x][tiro_y] = "X"
                iterador += 1
            elif tablero[tiro_x][tiro_y] == "B":
                print("En la posición " + str(tiro_x - 1) + "-" + str(tiro_y - 1) + " hay un barco.")
                tablero[tiro_x][tiro_y] = "T"
                tocados += 1
                iterador += 1
            elif tablero[tiro_x][tiro_y] == "X":
                print("La posición " + str(tiro_x - 1) + "-" + str(tiro_y - 1) + " ya ha sido tocada. Agua.")

            # Imprimimos el tablero
            for i in range(len(tablero)):
                for j in range(len(tablero[i])):
                    print(tablero[j][i], end="   ")
                print("\n")
            input("Presiona enter para continuar...")  # Esperamos el enter
        decision = -1
        print("Has tocado " + str(tocados) + " partes de barco.")
        if tocados == 6:
            print("Enorhabuena, se han tirado todos los barcos.")
        else:
            print("Lamentablemente, no has podido tirar todos los barcos.")

# Cerramos programa
print("Cerrando sesión. Gracias por jugar.")
