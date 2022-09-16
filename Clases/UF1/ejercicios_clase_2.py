"""Ejercicios clase viernes 16 septiembre 2022"""

"""
EJERCICIO1
Crearemos una variable de cada tipo con nombres de +1 palabra.
Crearemos 1 constante con +1 palabra de nombre y con valor +100
Las printaremos todas separandolas por "---" entre ellas en un solo print. Y finalizando la frase con "------]]]"

Solicitaremos al usuario una palabra y un número.
Repetiremos en una variable la palabra tantas veces como diga la constante.
"""
import array

texto: str = "Hola soy un texto"
numero: int = 100
decimal: float = 2.5
complejo: complex = 5j
tup: tuple = ("0", "1")
arr: array = [0, 1]
dic: dict = {"key": "value"}
bol: bool = True
CONSTANTE = 100
print(texto, numero, decimal, complejo, tup, arr, dic, bol, CONSTANTE, sep="---", end="------]]")
print()
palabra = input("Palabra: ")
numero = int(input("Numero: "))
print(palabra * (CONSTANTE // numero))
"""
EJERCICIO 2

Pediremos al usuario horas, minutos y segundos de inicio de un evento y su duracion en minutos
Calcularemos la hora exacta a la que termina el evento
"""

hora = int(input("Hora: "))
minu = int(input("Minutos: "))
segu = int(input("Segundos: "))
dura = int(input("Duración: "))


tiempo_tot_seg = (hora * 60 * 60) + (minu * 60) + segu + dura
hora_fin_minutos = tiempo_tot_seg // 60
horas_finales = hora_fin_minutos % 24
minutos_final = tiempo_tot_seg % 60
seg_final = tiempo_tot_seg % 60
print(str(horas_finales), str(minutos_final), str(seg_final), sep=":")

"""
EJERCICIO 3
Crearemos 2 constantes (nombre y usuario).
Pediremos al usuario que introduzca por teclado un nombre y un usuario
Comprobaremos de forma separada cada uno de ellos, indicandole al usuario si son o no correctos.
Finalmente, si ambos son correctos, guardaremos en una variable boolean el resultado y se lo mostraremos por pantalla.

"""
NOMBRE = "Eric"
USUARIO = "eep"
nom = input("Nombre: ")
user = input("Usuario: ")

if NOMBRE == nom:
    print("Nombre correcto")
else:
    print("Usuario correcto: ")

if USUARIO == user:
    print("Usuario correcto")
else:
    print("Usuario incorrecto")

is_both_correct = False
if NOMBRE == nom and USUARIO == user:
    is_both_correct = True

print("Son correctos ambos: " + str(is_both_correct))
