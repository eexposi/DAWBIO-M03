salir = 5
while salir != 0:
    print("Introduzca 0 para salir")
    print("Introduzca 1 para actividad 1")
    print("Introduzca 2 para actividad 2")
    print("Introduzca 3 para actividad 3")
    print("Introduzca 4 para actividad 4")
    num = int(input(" "))

    # Ejercicio 1
    # Elaborar un programa que realice la conversión de cm. a pulgadas.
    # Donde 1cm = 0.39737 pulgadas.
    if num == 1:
        print("Iniciando actividad 1")
        medida = int(input("Introduzca una medida en cm: "))
        resultado = medida * 0.39737
        print(resultado)
        break

    # Ejercicio 2
    # Obtener la edad de una persona en meses, si se introduce su edad en años y meses.
    # Ejemplo: Introducimos 3 años 4 meses se debe mostrar: 40 meses.
    if num == 2:
        print("Iniciando actividad 2")
        año = int(input("Introduzca su edad en años: "))
        mes = int(input("Ahora introduzca cuantos meses has cumplido desde tu ultimo cumpleaños: "))
        total = (año * 12) + mes
        total = str(total)
        print("Tu edad es de " + total + " meses")
        break

    # Ejercicio 3
    # Los alumnos de 1º de DAWBIO realizaran un viaje a Port Aventura a final de curso,
    # el precio de la entrada general es de 45€.
    # Al grupo se le aplicará un descuento dependiendo del número de alumnos:
    # Si alumnos > 50 --> 30%
    # Si alumnos entre 20 y 50 --> 20%
    # Si alumnos entre 10 y 20 --> 10%
    # Si alumnos es < 10 --> 0%
    # Profesor de programación --> entrada libre.
    # Descuento adicinal de 15% a alumnos menores de 18 años. La cantidad de alumnos
    # menores del grupo se ha de indicar para obtener el precio final.
    # El programa mostrará el importe total a pagar para los mayores de edad,
    # el importe a pagar para los menores de edad y el importe total del grupo.

    if num == 3:
        print("Iniciando actividad 3")
        entrada = 45
        alumnos = int(input("Cuantos alumnos realizaran el viaje? "))
        mayores = int(input("Cuantos son mayores de edad? "))
        menor = int(input("Cuantos son menores de edad? "))
        if alumnos > 50:
            descuento = entrada - ((entrada * 30) / 100)
            total = descuento * (alumnos - menor)
            if menor >= 0:
                desmin = entrada - ((entrada * 45) / 100)
                total1 = desmin * menor
            todo = total + total1
            total = str(total)
            total1 = str(total1)
            todo = str(todo)
            print("Importe total para mayores de edad: " + total + "€")
            print("Importe total para menores de edad: " + total1 + "€")
            print("Importe total del grupo: " + todo + "€")
            break
        if alumnos > 20:
            if alumnos <= 50:
                descuento = entrada - ((entrada * 20) / 100)
                total = descuento * (alumnos - menor)
            if menor >= 0:
                desmin = entrada - ((entrada * 35) / 100)
                total1 = desmin * menor
            todo = total + total1
            total = str(total)
            total1 = str(total1)
            todo = str(todo)
            print("Importe total para mayores de edad: " + total + "€")
            print("Importe total para menores de edad: " + total1 + "€")
            print("Importe total del grupo: " + todo + "€")
            break
        if alumnos > 10:
            if alumnos <= 20:
                descuento = entrada - ((entrada * 10) / 100)
                total = descuento * (alumnos - menor)
            if menor >= 0:
                desmin = entrada - ((entrada * 25) / 100)
                total1 = desmin * menor
            todo = total + total1
            total = str(total)
            total1 = str(total1)
            todo = str(todo)
            print("Importe total para mayores de edad: " + total + "€")
            print("Importe total para menores de edad: " + total1 + "€")
            print("Importe total del grupo: " + todo + "€")
            break
        if alumnos < 10:
            descuento = entrada
            total = descuento * (alumnos - menor)
            if menor >= 0:
                desmin = entrada - ((entrada * 15) / 100)
                total1 = desmin * menor
            todo = total + total1
            total = str(total)
            total1 = str(total1)
            todo = str(todo)
            print("Importe total para mayores de edad: " + total + "€")
            print("Importe total para menores de edad: " + total1 + "€")
            print("Importe total del grupo: " + todo + "€")
            break

    # Ejercicio 4
    # Dadas de listas
    # lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
    #        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
    #        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
    # lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
    #        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
    #        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]
    # 4.1 - Compararemos ambas listas, mostrando por pantalla cuál de las 2 es mas larga.
    # 4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.
    # 4.3 - Recorreremos la lista 1 y compararemos cada elemento de la lista, con el que tenga la misma posición de la otra.
    # Indicando que lista posee el elemento con un valor más pequeño.
    # 4.4 - Ordenaremos ambas listas de la misma forma y las mostraremos una de mayor a menor y la otra al revés de forma
    # invertida.

    if num == 4:
        print("Iniciando actividad 4")
        lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0,
                0, 2,
                0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1,
                5, 3,
                5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
        lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3,
                7, 7, 2,
                5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8,
                9, 10, 2,
                0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]
        num1 = 0
        num2 = 0
        for i in lst1:
            num1 += 1
        for i in lst2:
            num2 += 1
        if num1 > num2:
            num1 = str(num1)
            num2 = str(num2)
            n = len(lst1)
            for i in range(n - 1):
                for i in range(n - 1 - i):
                    if lst1[i] > lst1[i + 1]:
                        lst1[i], lst1[i + 1] = lst1[i + 1], lst1[i]
            n = len(lst2)
            for i in range(n - 1):
                for i in range(n - 1 - i):
                    if lst2[i] < lst2[i + 1]:
                        lst2[i], lst2[i + 1] = lst2[i + 1], lst2[i]
            print("El mas largo es la primera lista con " + num1 + " numeros")
            print("La segunda lista tiene " + num2 + " numeros")
            lst1 = str(lst1)
            lst2 = str(lst2)
            print("Lista 1 ordenada: " + lst1)
            print("Lista 2 ordenada invertida: " + lst2)
            break
        if num2 > num1:
            num2 = str(num2)
            num1 = str(num1)
            print("El mas largo es la segunda lista con " + num2 + " numeros")
            print("La primera lista tiene " + num1 + " numeros")
            break
