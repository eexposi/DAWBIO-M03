"""
------- EJERCICIO 1:
def menu():
    lista=["Salir", "Sumar", "Restar", "Multiplicar", "Dividir"]
    for i in range(len(lista)):
        print(i, lista[i], sep=" - ")

num1 = int(input("Indica un numero: "))
num2 = int(input("Indica un numero: "))

def sumar (numero1,numero2):
    return numero1 + numero2

def restar (numero1,numero2):
    return numero1 - numero2

def multiplicar (numero1,numero2):
    return numero1 * numero2

def dividir (numero1,numero2):
    return numero1 / numero2

while True:
    menu()
    opcion=int(input("Elige opción del menú: "))
    if opcion == 0:
        print("Adiós!")
        break
    elif opcion == 1:
        resultado = sumar(num1,num2)
    elif opcion == 2:
        resultado = restar(num1, num2)
    elif opcion == 3:
        resultado = multiplicar(num1, num2)
    elif opcion == 4:
        resultado = dividir(num1, num2)
    else:
        print("Opción incorrecta!")

    print("El resultado final es ", resultado)

------- EJERCICIO 2:
LISTA = ["Chocolate", "Blanco", "Coche", "Casa", "Amor", "Pepinillos"]

def print_lista(lista):
    for i in lista:
        print("La palabra es " + i)

print_lista(LISTA)

#------- EJERCICIO 3:
# Crearemos 3 variables (1 integer, 1 string y 1 diccionario).
# Mediante métodos, las printaremos todas separandolas por "---" entre ellas en
# un solo print, y finalizando la frase con "------]]]"

def mostrar (numero, string, dicc):
    print(int(numero), str(string), dicc, sep="---")

mostrar(10, "Hola", {"key":"valor"})
"""


# ------- EJERCICIO 4:
# Pediremos al usuario horas y minutos de inicio de un evento y su duracion en minutos
# Calcularemos la hora exacta a la que termina el evento

def horas_a_minutos(horas):
    minutos = horas * 60
    return minutos


hours = int(input("Indica la hora de inicio del evento: "))
mins = int(input("Indica los minutos de inicio del evento: "))
min_totales = horas_a_minutos(hours) + mins

# Método que le llega un número (1-20), según el cuál devolverá tramo (1-4)(6-10)(11-15)(16-20)

# Método que printa un menú y devuelve la opcion elegida por el usuario

# Método que devuelve la cantidad de carácteres que tiene un string pasado por parametro
