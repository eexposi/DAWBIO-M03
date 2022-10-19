""""EJERCICIO 1"""
from operator import truediv


print("EJERCICIO 1")
pulgadas=0.39737
cm=int(input("Escribe un numero de centimetros para pasarlo en pulgadas "))
res=cm * pulgadas
frase=str(cm) + " centimetros son " + str(res) + " pulgadas"
print(frase)

""""EJERCICIO 2"""

print("EJERCICIO 3")
""""EJERCICIO 3"""
a=45
p=0

alum=int(input("Quantos alumnos van a Port Aventura "))
men=int(input("Quantos alumnos ahi que sean menores de edat"))
sin_men=alum - men
cal=45 * alum
if alum > 50:
    print("El descuento es de 30%, el precio final sera:")
    a=print(str(cal * 30 /100) + "€")
elif alum < 10:
    print("El descuento es de 0%, el precio sera ")
    b=print(str(cal) + "€")
else:
    print("No ahi descuentos a aplicar, el precio sera ")
    c=print(str(cal) + "€")


frase=("los alumnos menores de edat tienen un descuento adicional de un 15%,en tu caso es  " + str(sin_men * 15 /100))

""""EJERCICIO 4"""
print("EJERCICIO 4")
print("4.1")
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]
tamaño=0
tamaño2=0
for e in lst1:
    tamaño +=1
for o in lst2:
    tamaño2 +=1
r_lst1=print("La lista 1 " + str(lst1) + " tiene: " + str(tamaño) + "numeros")
r_lst2=print("La lista 2 " + str(lst2) + " tiene: " + str(tamaño2) + "numeros")
print("4.2")

suma_de_numeros1=0
suma_de_numeros2=0
for n in lst1:
    suma_de_numeros1 += n
media1=suma_de_numeros1 / tamaño
frase1=("La nota media de la lista 1 es " + str (media1))
print(frase1)

for n in lst2:
    suma_de_numeros2 += n
media2=suma_de_numeros2 / tamaño2
frase2=("La nota media de la lista 2 es " + str (media2))
print(frase2)
print("4.4")
lista_ordenada1=lst1
c=True
while c:
    c=False
    for l in range(len(lista_ordenada1) -1):
        if lista_ordenada1[l] > lista_ordenada1[l + 1]:
            c=True
            lista_ordenada1[l], lista_ordenada1[l + 1] = lista_ordenada1[l + 1],lista_ordenada1[l]
print("Lista1 ordenada:" + str(lista_ordenada1))

lista_ordenada2=lst2
cp=True
while cp:
    cp=False
    for v in range(len(lista_ordenada2) -1):
        if lista_ordenada2[v]> lista_ordenada2[1 + v]:
            cp=True
            lista_ordenada2[v], lista_ordenada2[1 + v] = lista_ordenada2[1 + v],lista_ordenada1[v]
print("Lista2 ordenada:" + str(lista_ordenada2))