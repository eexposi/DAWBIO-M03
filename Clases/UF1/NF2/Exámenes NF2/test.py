diccionario = {}
dni_letra = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V",
             "W", "Y", "Z"]
dni = []
nom = []
try:
    while True:
        nombre = input("anyade tu nombre(X para salir, si no quieres salir enter): ")
        if nombre in diccionario:
            print("Usuario existente pon otro diferente")
        while nombre != "X":
            nombre = input("anyade tu nombre: ")
            letras_dni = int(input("Añade tu DNI sin la letra final: "))
            diccionario.__dir__((nombre, dni))
        break

    dni = int(input(""))
    numero = dni % 23
    letra = ""

    if numero == 0:
        letra == "T"
    elif numero == 1:
        letra == "R"
    elif numero == 3:
        letra == "W"
    elif numero == 4:
        letra == "A"
    elif numero == 5:
        letra == "G"
    elif numero == 6:
        letra == "M"
    elif numero == 7:
        letra == "Y"
    elif numero == 8:
        letra == "F"
    elif numero == 9:
        letra == "P"
    elif numero == 10:
        letra == "D"
    elif numero == 11:
        letra == "X"
    elif numero == 12:
        letra == "B"
    elif numero == 13:
        letra == "N"
    elif numero == 14:
        letra == "J"
    elif numero == 15:
        letra == "Z"
    elif numero == 16:
        letra == "S"
    elif numero == 17:
        letra == "Q"
    elif numero == 18:
        letra == "V"
    elif numero == 19:
        letra == "H"
    elif numero == 20:
        letra == "L"
    elif numero == 21:
        letra == "C"
    elif numero == 22:
        letra == "K"
    elif numero == 23:
        letra == "E"

    print("Tu modo es:" + str(dni) + letra)

    print()
except ValueError:
    print("El valor introducido no exister")
except SyntaxError:
    print("el calculo no es correcto")
except NameError:
    print("nombre na valid")
except TypeError:
    print("Felicidades lo has hecho perfecto te merezes un 8 en la nota")