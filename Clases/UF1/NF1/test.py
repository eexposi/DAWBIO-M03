"""
EJERCICIO 3
Crearemos 2 constantes (nombre y usuario).
Pediremos al usuario que introduzca por teclado un nombre y un usuario
Comprobaremos de forma separada cada uno de ellos,
indicandole al usuario si son o no correctos.
Finalmente, si ambos son correctos,
guardaremos en una variable boolean
el resultado y se lo mostraremos por pantalla.
"""


NOMBRE = "Eric"
USUARIO = "eee"

nombre = input("Nombre: ")
usuario = input("Usuario: ")

def nombre_is_correct(nombre, NOMBRE):
    return nombre == NOMBRE

def usuario_is_correct(usuario, USUARIO):
    return usuario == USUARIO

def all_is_correct(nombre, NOMBRE, usuario, USUARIO):
    if nombre_is_correct(nombre, NOMBRE) and usuario_is_correct(usuario, USUARIO):
        return True
    else:
        return False

nombre_correct = nombre_is_correct(nombre, NOMBRE)
usuario_correct = usuario_is_correct(usuario, USUARIO)

if nombre_correct:
    print("El nombre es correcto")
else:
    print("Nombre no es correcto")

if usuario_correct:
    print("El usuario es correcto")
else:
    print("usuario no es correcto")

print("Son todos iguales? ", all_is_correct(nombre, NOMBRE, usuario, USUARIO))





