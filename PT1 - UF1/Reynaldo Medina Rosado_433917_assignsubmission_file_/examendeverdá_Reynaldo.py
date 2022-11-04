# #EJERCICIO 1: Elaborar un programa que realice la conversión de cm. a pulgadas. Donde 1cm = 0.39737 pulgadas.
print("Ex 1")
print('programa conversor de pulgadas a cm (1cm= 0.39737 pulgadas')
cm = int(input('cm:'))
pulg = (cm * 0.39737)
print('Sepa usted que ' + str(cm) + ' ' + ' centimetros son: ' + str(pulg) + 'pulgadas')

# #EJERCICIO 2: Obtener la edad de una persona en meses, si se introduce su edad en años y meses. Ejemplo: Introducimos 3 años 4 meses debe mostrar: 40 meses.
print("Ex2")
print('Cuantos meses tiene? :')
años = int(input('Años: '))
meses = int(input('Meses: '))
edad = (años * 12 + meses)
print('Usted tiene ' + str(edad) + ' meses')
# EJERCICIO 3:
print('ex3')
alumn = int(input('Cuantos alumnos van al PortAventura:'))
prec = ''
desc = ''
if alumn < 10:
    desc = (0)
    prec = (alumn * 45 - desc)
elif alumn >= 10:
    desc = (alumn * 45 * 0.10)
    prec = (alumn * 45 - desc)
elif alumn >= 20:
    desc = (alumn * 45 * 0.20)
    prec = (alumn * 45 - desc)
elif alumn > 50:
    desc = (alumn * 45 * 0.30)
    prec = (alumn * 45 - desc)
print('Si van ' + str(alumn) + ' alumnes es decompten ' + str(desc) + ' i el preu  es queda en ' + str(prec))
menor = int(input('Quants menors van: '))
desctot = ''
if menor >= 1:
    descmen = (menor * 45 * 0.15)
    desctot = (prec - descmen)
print('Si van ' + str(menor) + ' menors'' el preu total es queda en ' + str(desctot))
if menor == 0:
    print(str(prec))
# EJERCICIO 4
print('ex 4.1')
# Dadas las listas:
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]
longlst1 = 0
for e in lst1:
    longlst1 += 1
print('La llista 2 te ' + str(longlst1))
longlst2 = 0
for e in lst2:
    longlst2 += 1
print('La llista 1 te ' + str(longlst2))
print('la llista 1 es més llarga amb 1 elemnt més')
