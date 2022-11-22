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
lista_ejercicios = [1, 2, 3]

if 1 in lista_ejercicios:
    print("")
    print("")
    print("-----------------------------------------------------------")
    print("EJERCICIO 1  ----------------------------------------------")
    print("-----------------------------------------------------------")
    print("- Pedir al usuario su nombre y su DNI sin letra.")
    print("- Crear un diccionario con la key : nombre y el value : DNI con la letra.")
    print("- Mostrar todos los datos en forma de tabla.")
    print("")
    print("            Usuarios")
    print("            ---------")
    print("            Nombre --> XXXXXXXX-X")
    print("")
    print("Las letras son: TRWAGMYFPDXBNJZSQVHLCKE")
    print("Y las letras se relacionan del 0 al 22:")
    print("0 = T")
    print("1 = R")
    print("2 = W")
    print("etc...")
    print("")
    print("")

    letras_dni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L",
                  "C", "K", "E"]
    diccionario_nombres_dnis = {}
    aux = True
    while aux != False:
        try:
            nombre = str(input("Introduce un nombre: "))
            while nombre in diccionario_nombres_dnis:
                print("El nombre introducido esta en la lista.")
                nombre = str(input("Introduce otro nombre: "))

            dni = str(input("Introduce el numero de un dni: "))
            while len(str(dni)) != 8:
                print("El numero del dni introducido no es correcto.")
                dni = str(input("Introduce el numero de tu dni: "))
            else:
                operacion_dni = int(dni) % 23
                dni_con_letra = str(dni + "-" + letras_dni[operacion_dni])
                diccionario_nombres_dnis[nombre] = dni_con_letra
                print("\nUsuarios")
                print("---------------")
                for t in diccionario_nombres_dnis:
                    print(t, "---->", diccionario_nombres_dnis[nombre])
                pregunta_usuario = str(input("\nQuieres seguir introduciendo datos?: S / N: "))
                if pregunta_usuario == "S" or pregunta_usuario == "s":
                    aux = True
                else:
                    aux = False
        except (NameError, SyntaxError):
            print("Hay un problema en el codigo")
        except ValueError:
            print("El valor introducido no es correcto.")
        except TypeError:
            print("El dato introducido no es del tipo esperado.")
        except Exception as e:
            raise Exception("Ha habido otro tipo de problema.")
        except:
            pass

print("")
print("-" * 80)
print("")

if 2 in lista_ejercicios:
    print("-----------------------------------------------------------")
    print("EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------")
    print("-----------------------------------------------------------")
    print("- Pedir al usuario 2 números.")
    print("- While hasta que le introduzcamos 'X' en el primer valor")
    print(
        "- Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.")
    print("")
    print("")

    aux = 0
    numero_usuario_1 = 1
    aux = True
    while aux != False:
        try:
            numero_usuario_1 = str(input("Introduce un primer numero (Escribe X para terminar): "))
            if numero_usuario_1 == "X" or numero_usuario_1 == "x":
                break
            numero_usuario_2 = int(input("Introduce un segundo numero: "))
            if int(numero_usuario_1) >= 0 or int(numero_usuario_2) >= 0:
                resultado_division = int(numero_usuario_1) // int(numero_usuario_2)
                print("El resultado de tu division es:", resultado_division)
            else:
                print("No se puede dividir con numeros negativos.")
            pregunta_usuario = str(input("\nQuieres seguir introduciendo datos?: S / N: "))
            if pregunta_usuario == "S" or pregunta_usuario == "s":
                aux = True
            else:
                aux = False
        except ZeroDivisionError:
            print("No se puede dividir por 0.")
        except ValueError:
            print("El valor introducido no es correcto.")
        except (NameError, SyntaxError):
            print("Hay un problema en el codigo")
        except:
            pass

print("")
print("-" * 80)
print("")

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
if 3 in lista_ejercicios:
    print("")
    print("")
    print("-----------------------------------------------------------")
    print("EJERCICIO 3: HUNDIR LA FLOTA ------------------------------")
    print("-----------------------------------------------------------")
    print(
        "El código va a crear un tablero de 4x4 y va a colocar 2 barcos en él. El código debe permitir, fácilmente, cambiar")
    print("la posición de los barcos antes de lanzar el programa.")
    print("")
    print("# Antes de empezar a jugar:")
    print("- Creamos un tablero de 4x4 vacío ('A')")
    print(
        "- Colocamos 2 barcos (posición con 'B'), uno de 2 celdas y otro de 3 celdas (horizontal o vertical pero que no solapen)")
    print("")
    print("# Al iniciar el programa...")
    print("- Mostrar el menú de juego (diccionario o lista) y tablero inicial con los barcos:")
    print("        1 - Jugar")
    print("        0 - Salir")
    print("- En random, hacemos tiradas:")
    print("    - devolver posición de la tirada")
    print(
        "    - devolver agua (cambiar la casilla vacía 'A' por 'X') o tocado (cambiar la casilla de barco 'B' por 'T')")
    print("    - devolver estado del tablero")
    print("    - Esperar 'ENTER' para siguiente tirada")
    print(
        "- Al completar 6 tiradas, deberemos devolver un mensaje según si hemos conseguido hundir todos los barcos o no")
    print("")
    print("")
    print("EJEMPLO DEL 1ER TURNO ----------------------------------------------------")
    print("-  Mostramos el tablero al empezar el juego:")
    print("           0 1 2 3")
    print("         0 A B B A")
    print("         1 A A A B")
    print("         2 A A A B")
    print("         3 A A A B")
    print("")
    print("- Vemos las posiciones del disparo:")
    print("    Se dispara en la posicion x: 0 y: 1")
    print("    Tocado!")
    print("")
    print("- Mostramos el tablero con las modificaciones:")
    print("           0 1 2 3")
    print("         0 A T B A")
    print("         1 A A A B")
    print("         2 A A A B")
    print("         3 A A A B")
    print(" Esperamos al siguiente turno:   Pulsa ENTER para continuar...")
    print("")
    print("--------------------------------------------------------------------------------------------------- ")
    print("")

    A = "A"
    B = "B"
    tablero = [[" ", 0, 1, 2, 3], [0, A, A, A, A], [1, A, A, A, A], [2, A, A, A, A], [3, A, A, A, A]]
    win = 0
    menu = ["1 - Jugar", "0 - Salir"]
    while win != 5:
        print("")
        for n in menu:
            print(n)

        print("\nTablero: ")
        for r in range(0, len(tablero)):
            print(sep=" ")
            for t in range(0, len(tablero[r])):
                print(tablero[r][t], end=" ")

        break

print("\n\nEl juego HUNDIR LA FLOTA esta en construccion.\n")
