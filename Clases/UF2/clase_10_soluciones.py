"""
Ejercicio 1
Crearemos una funcion que recibirá por parametro un nombre y una edad.
Esta funcion mostrara un mensaje saludando al usuario por su nombre e indicandole cual es su edad.
Si no se pasan parametros, por defecto sera "tonto" y 0.
"""
def saludar(nombre="tonto", edad=0):
    """
    Mostrara por pantalla el nombre y la edad del usuario
    @param nombre es el nombre del usuario
    @param edad es la edad del usuario
    """
    print("Hola", nombre, "tu edad es", edad)

saludar("Eric", 35)



"""
Ejercicio 2
Haremos un menu con 5 opciones: salir, sumar, restar, multiplicar i dividir.
Le pediremos al usuario 2 numeros, mostraremos el menu y, segun la opcion, 
ejecutaremos la funcion que corresponda, mostrando el resultado mediante 
la funcion
"""
menu = ["Salir", "Sumar", "Restar", "Multiplicar", "Dividir"]
num1 = int(input("Indica un numero: "))
num2 = int(input("Indica un numero: "))


def sumar(num1, num2):
    """
    Suma los parametros y los muestra por pantalla
    @param num1: numero 1
    @param num2: numero 2
    """
    print(num1 + num2)


def restar(num1, num2):
    """
    Resta los parametros y los muestra por pantalla
    @param num1: numero 1
    @param num2: numero 2
    """
    print(num1 - num2)


while True:
    for e in range(len(menu)):
        print(e, menu[e], sep=" - ")
    seleccion = int(input("Seleccion: "))
    if seleccion == 1:
        sumar(num1, num2)
    elif seleccion == 2:
        restar(num1, num2)
    elif seleccion == 0:
        break
    else:
        print("opcion incorrecta")

"""
Ejercicio 3
Haremos un menu con 5 opciones: salir, sumar, restar
Le pediremos al usuario 2 numeros, mostraremos el menu y, segun la opcion, ejecutaremos la funcion que corresponda.
La funcion nos devolvera el resultado de la operacion, y lo mostraremos al final
"""
menu = ["Salir", "Multiplicar", "Dividir"]
num1 = int(input("Indica un numero: "))
num2 = int(input("Indica un numero: "))


def multiplicar(num1, num2):
    """
    
    @param num1:
    @param num2:
    @return:
    """
    return num1 * num2


def dividir(num1, num2):
    """

    @param num1:
    @param num2:
    @return:
    """
    return num1 / num2


resultado = 0
while True:
    for e in range(len(menu)):
        print(e, menu[e], sep=" - ")
    seleccion = int(input("Seleccion: "))
    if seleccion == 1:
        resultado = multiplicar(num1, num2)
    elif seleccion == 2:
        resultado = dividir(num1, num2)
    elif seleccion == 0:
        break
    else:
        print("opcion incorrecta")
    print("El resultado es", resultado)
"""
Ejercicio 4
Crearemos una lista con 10 palabras.
Recorreremos la lista con un for y mediante una funcion printaremos por pantalla:
"La palabra es ----- " donde - es la palabra de la lista
"""
PALABRAS = ["Chocolate", "Blanco", "Coche", "Casa", "Amor", "Pepinillos"]


def mostrar_elemento_lista(e):
    """
    Printaremos por pantalla la palabra de la lista
    @param e: palabra de la lista
    """
    print("La palabra es", e)


for e in PALABRAS:
    mostrar_elemento_lista(e)
