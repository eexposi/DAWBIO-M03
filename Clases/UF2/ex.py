def saludo(nombre="tonto",edad=0):
    """
    Esta función recoge el nombre y la edad del usuario y devuelve
    una frase utilizando estos 2 parámetros.
    :param nombre: parámetro 1, que debe contener el nombre del usuario (string)
    :param edad: parámetro 2, que debe contener la edad del usuario (int)
    :return: la función devuelve una frase
    """

    frase = ("Hola " + nombre + ", tu edad es " + str(edad) + " años.")
    frase.find()
    return frase

X=input("Indícame tu nombre: ")
Y=int(input("Dime tu edad: "))
print(saludo())