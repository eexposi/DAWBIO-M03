""" EJERCICIO 1
Escriba un método que reciba dos números y que devuelva 0 si son iguales, 1
si el primero es mayor que el segundo y ‐1 si el segundo es mayor que el
primero. """
def compara (num1,num2):
    if num1 == num2:
        return 0;
    elif num1 > num2:
        return 1;
    else:
        return -1;

numero1=8
numero2=6
print("El resultado es: ", compara(numero1,numero2))


""" EJERCICIO 2
Escriba un método que se encargue de pedir al usuario un número, cree un
array de ese tamaño, pregunte al usuario por los valores y devuelva el array
creado. """
def crea_array ():
    array=[]
    largo_array=int(input("Introduce el tamaño del array: "))
    for i in range(largo_array):
        valor=input("Indícame la letra a introducir: ")
        array.append(valor)
    print("El array final es: ", end="")
    for i in array:
        print (i, end="")

crea_array()
print()


""" EJERCICIO 3
Escriba un método que reciba un array e imprima los valores del array con el
siguiente formato: Ej 1 2 3 4 ‐> [1,2,3,4] """

def impresion (array):
    print("[", end="")
    for i in array:
        print(i,",",end="")
    print("]")

frase="1234"
impresion(frase)


""" EJERCICIO 4
Escriba un programa que llame a los dos métodos anteriores para crear un
array e imprimirlo. """

def impresion2 (array):
    print("[", end="")
    for i in array:
        print(i,",",end="")
    print("]")

frase2=crea_array()
impresion2(frase)


""" EJERCICIO 5
Escriba un método que reciba un array de valores y un número y multiplique
todos los valores del array por ese número. Imprima el array resultante con
el método del ejercicio 4. """

def impresion3 (array):
    print("[", end="")
    for i in array:
        print(i,",",end="")
    print("]")

def multiplica (array,numero):
    for i in len(array):
        array[i] *= numero

array_numeros=[2,3,4]
print("Array original: ", impresion3(array_numeros))
print("Array multiplicado: ", multiplica(array_numeros,3))
impresion3(array_numeros)


""" EJERCICIO 6
Escriba un método que reciba dos arrays y devuelva uno nuevo que contenga
a los valores concatenados de los otros dos. """


""" EJERCICIO 7
Escriba un método que reciba un array, un número y devuelva la última
posición del array que contenga a ese valor. En caso de no encontrar al valor,
el método deberá devolver ‐1. Por ejemplo, con [1,2,3,5,6,7,3,9] y el número 3
el método deberá devolver un 6 y con 10 un ‐1. """

def devolver_pos (array,num):
    final=-1
    for i in range(len(array)):
        if array[i] == num:
            final=i
    return final

lista=[1,2,3,5,6,7,3,9]
valor=5
print(devolver_pos(lista,valor))

""" EJERCICIO 8
Escriba un método que reciba dos arrays y compruebe si todos los elementos
del primero se encuentran en el segundo devolviendo true or false en función
de si encuentra o no todos los valores. Ej con los arrays [1,2,3] y [5,3,7,2,1,8]
debería devolver true. """

def

""" EJERCICIO 9
Escriba un método que imprima una matriz separando cada elemento con 1
espacio. Probarlo con {{1,2,3},{4,5,6},{7,8,9}} """

# HASTA AQUÍ EN LA SESIÓN DEL 9/12

""" EJERCICIO 10
Escriba un método que realice la suma de dos matrices de 3x3 y devuelva el
resultado en un nuevo array. """


""" EJERCICIO 11
Escriba el método mostrarDigitosInverso que dado un entero y un carácter,
imprima los dígitos, separados por ese carácter, en orden inverso. Por
ejemplo, el entero 4567 y el carácter ‘‐‘ debería producir la siguiente salida:
7‐6‐5‐4 """

def mostrarDigitosInverso (entero, caracter):
    while entero > 10:
        print(int(entero%10) , caracter, end="")
        entero = entero/10
    print(int(entero), end="")

valor=4567
separador="-"
mostrarDigitosInverso (valor,separador)
print()


""" EJERCICIO 12
El máximo común divisor de dos enteros es el mayor entero que divide a los
dos números sin dejar resto. Escriba un método mcd que calcule el máximo
común divisor de dos enteros. """

def mcd (primero,segundo):
    if segundo == 0:
        return primero
    else:
        return mcd(segundo,primero%segundo)

x=72
y=60
result=mcd(x,y)
print ("El MCD de " + str(x) +" y "+ str(y) + " es: " + str(result))