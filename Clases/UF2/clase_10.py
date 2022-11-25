"""FUNCIONES"""


# Una funcion es un trozo de codigo que podrá llamarse en cualquier parte del codigo
def enviar_mensaje():
    print("hola")


# Podemos llamarla, y se mostrara por pantalla

enviar_mensaje()


# podemos implementar cualquier tipo de codigo dentro de una funcion, pero recordemos que las variables se quedan
# dentro

def enviar_mensaje2():
    mensaje = "Adios"
    print(mensaje)


enviar_mensaje2()
# print(mensaje)

"""Tenemos funciones con parametros, es decir, podemos indicarle variables que usara dentro"""


def enviar_mensaje_3(mensaje):
    print(mensaje)


mensaje = "Pepito"
enviar_mensaje_3(mensaje)

"""podemos usar tantos parametros como se considere. Pero siempre se cogeran por orden"""


def test(parametro1, parametro2):
    print(parametro1)
    print(parametro2)


test("1", "2")

"""si no queremos que vayan por orden, sino definir cual es cual, podemos indicarlo"""


def test2(parametro1, parametro2):
    print(parametro1)
    print(parametro2)


test2(parametro2="1", parametro1="2")

"""Tambien podemos asignar a la funcion valores por defecto, lo que en caso de no pasarle argumentos en el momento
de su llamada, cogera los valores por defectos y "rellenará" el hueco"""


def nombre_apellido(nombre="Eric", apellido="Exposito"):
    print("Tu nombres es: ", nombre, " y tu apellido ", apellido)


nombre_apellido()

"""Ya conocemos los metodos, ahora veremos como los metodos nos pueden devolver un valor"""


def sumar(num1, num2):
    suma = num1 + num2
    return suma  # num1+num2


total_suma = sumar(1, 5)
print(total_suma)

"Un return en cualquier parte del metodo, provocara que este acabe. Si no ponemos ningun elemento a su lado," \
"finalizara sin mas. Si ponemos algun valor, lo obtendremos en el programa principal"


def sumar(num1, num2):
    suma = num1 + num2
    if suma > 10:
        return 5000
    else:
        return suma

total_suma = sumar(1,5)
total_suma2 = sumar(10,10)

print(total_suma)
print(total_suma2)


"Con el return, podemos obtener cualquier tipo de valor o resultado"

"""Comentarios
Tras la definicion de cada metodo comentaremos su funcionalidad. Indicaremos que parametros tiene, su uso y el return.
@param variable esta variable sirve para...
@return devuelve un....
"""

def saludo(nombre, apellido, direccion, ciudad, provincia, pais, codigo_postal):
    """

    :param nombre:
    :param apellido:
    :param direccion:
    :param ciudad:
    :param provincia:
    :param pais:
    :param codigo_postal:
    :return:
    """
    mensaje = "Hola " + nombre
    return mensaje


"""
Ejercicio 1
Crearemos una funcion que recibirá por parametro un nombre y una edad que
hayamos solicitado al usuario. Esta funcion mostrara un mensaje saludando 
al usuario por su nombre e indicandole cual es su edad.
Si no se pasan parametros, por defecto sera "tonto" y 0.
"""
def saludo(nombre="tonto",edad=0):
    frase = ("Hola " + nombre + ", tu edad es " + edad + " años.")
    return frase

nom=input("Indícame tu nombre: ")
edat=input("Dime tu edad: ")
print(saludo(nom,edat))


"""
Ejercicio 2
Haremos un menu con 5 opciones: salir, sumar, restar, multiplicar y dividir
Le pediremos al usuario 2 numeros, mostraremos el menu y, segun la opcion, 
ejecutaremos la funcion que corresponda, mostrando el resultado mediante
la funcion.
El menú se muestra con una función. Todas las opciones son funciones (def sumar,
def restar...)
"""

"""
Ejercicio 3
Crearemos una lista con 10 palabras.
Recorreremos la lista con un for y mediante una funcion printaremos por pantalla:
"La palabra es ----- " donde - es la palabra de la lista
"""
