seleccion = 4
X = "X"
menu = ["Salir", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3"]
while seleccion != 0:
    for i in range(len(menu)):
        print(i, menu[i], sep=" - ")
    seleccion = int(input("Seleccione un Ejercicio o Salir: "))

    # Ejercicio 1
    # - Pedir al usuario su nombre y su DNI sin letra.
    # - Crear un diccionario con la key : nombre y el value : DNI con la letra.
    # - Mostrar todos los datos en forma de tabla.

    if seleccion == 1:
        diccionario = {}
        letras = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X",
                  11: "B", 12: "N", 13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C", 21: "K",
                  22: "E"}
        nombre = input("Escriba su nombre: ")
        dnicodigo = int(input("Escriba su DNI sin letra: "))
        diccionario[nombre] = dnicodigo
        letra = dnicodigo % 23
        print("Usuarios")
        print("---------")
        for e in diccionario:
            if e != diccionario[nombre]:
                print(e, "--> ", diccionario[e], "-", letras[letra])
        break

    # Ejercicio 2
    # - Pedir al usuario 2 números.
    # - While hasta que le introduzcamos 'X' en el primer valor
    # - Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
    if seleccion == 2:
        while True:
            try:
                primerdigito = input("Introduzca un numero para la division: ")
                if primerdigito == X:
                    print("Saliendo del ejercicio 2")
                    break
                else:
                    segundodigito = input("Introduzca un segundo numero para la division: ")
                    primerdigito = int(primerdigito)
                    segundodigito = int(segundodigito)
                    print(primerdigito / segundodigito)
            except (SyntaxError, NameError):
                print("¡Lo sentimos, ha ocurrido un error!")
            except ZeroDivisionError:
                print("No se puede dividir entre 0")
            except ValueError:
                print("Solo se permiten numeros")
            except KeyboardInterrupt:
                print("¡Lo sentimos, ha ocurrido un error!")

    # Ejercicio 3
    # El código va a crear un tablero de 4x4 y va a colocar 2 barcos en él. El código debe permitir, fácilmente, cambiar
    # la posición de los barcos antes de lanzar el programa.

    # Antes de empezar a jugar:
    # - Creamos un tablero de 4x4 vacío ('A')
    # - Colocamos 2 barcos (posición con 'B'), uno de 2 celdas y otro de 3 celdas (horizontal o vertical pero que no solapen)

    # Al iniciar el programa...
    # - Mostrar el menú de juego (diccionario o lista) y tablero inicial con los barcos:
    #         1 - Jugar
    #         0 - Salir
    # - En random, hacemos tiradas:
    #     - devolver posición de la tirada
    #     - devolver agua (cambiar la casilla vacía 'A' por 'X') o tocado (cambiar la casilla de barco 'B' por 'T')
    #     - devolver estado del tablero
    #     - Esperar 'ENTER' para siguiente tirada
    # - Al completar 6 tiradas, deberemos devolver un mensaje según si hemos conseguido hundir todos los barcos o no
    if seleccion == 3:
        salida = 3
        menu2 = ["Salir", "Jugar"]
        while salida != 2:
            for i in range(len(menu2)):
                print(i, menu2[i], sep=" - ")
            selecciona = int(input("Seleccione Jugar o Salir: "))
            if selecciona == 0:
                print("Cerrando Ejercicio 3")
                break
            if selecciona == 1:
                tabla = ["A ", "A ", "A ", "A "]
                print("  0 1 2 3")
                for i in range(len(tabla)):
                    print(i, tabla[i] * 4)

    if seleccion == 0:
        print("Cerrando programa")
        break
