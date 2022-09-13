""" #Tipos de variable
texto: str = "Hola, soy un texto largo y tedioso"
numeros: int = 99999
complejos: complex = 1j
decimales: float = 0.25
tupla = ('abcd', 786, 2.23, 'john', 70.2)
diccionario = {'name': 'eric', 'edad': 99, 'departamento': 'informatica'}

print(texto)
print(numeros)
print(complejos)
print(decimales)
print(tupla)
print(diccionario)

#Un string es un conjunto de caracteres, y podemos acceder a cada uno de ellos.
print(texto[1])

#Justo como en las tuplas
print(tupla[1])

#Podemos operar con los tipos basicos

t1 = "hola"
t2 = " que tal?"
print(t1+t2) #Como vemos, se concatenan las variables

n1 = 5
n2 = 20
print(n1+n2)#en cambio los numeros se suman

nombre = input("Indique su nombre: ")
print("Hola " + nombre)

#Podemos añadir texto, concatenando
#nombre += " Hola!!!!"
print(nombre)

apellido = input ("Indique su apellido: ")

nombre_completo = nombre + " " + apellido
print(nombre_completo) """
