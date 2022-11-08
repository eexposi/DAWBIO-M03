"""
EJERCICIO 1
Elaborar un programa que realice la conversión de cm. a pulgadas. Donde 1cm = 0.39737 pulgadas.
"""

# Si no introducimos ningún valor o valor no numérico   -->    # ValueError: invalid literal for int() with base 10: ''
# Si introducimos un valor no entero   -->   # ValueError: invalid literal for int() with base 10: '0,7'
# Si nos equivocamos al programar   -->   #NameError o SyntaxError
while True:
    try:
        cm = int(input("Introduce los cm: "))
        print("En pulgadas son: " + str(cm * 0.39737))
        break
    except ValueError:
        print("Debes introducir un valor entero.")
    except (SyntaxError, NameError):
        print("¿Seguro que el código está bien...?")
    except:                                 # <-- POR DEFECTO, siempre el último except
        print("Ha sucedido algo extraño, ¡lo siento!")


"""
EJERCICIO 2
Obtener la edad de una persona en meses, si se introduce su edad en años y meses. 
Ejemplo: Introducimos 3 años 4 meses
debe mostrar: 40 meses.
"""

while True:
    try:
        anyos = 0
        meses = 0
        anyos = int(input("Indica los años: "))
        meses = int(input("Indica los meses: "))
        if (anyos or meses) <= 0:
            raise Exception
        total_meses = (anyos * 12) + meses
        print("Tienes " + str(total_meses) + " meses de edad.")
        break

    except ValueError:
        print("Debes introducir un valor entero.")
    except (SyntaxError, NameError):
        print("¿Seguro que el código está bien...?")
    except Exception as Error:
        print("Debes introducir valores positivos.")
    except:  # <-- POR DEFECTO, siempre el último except
        print("Ha sucedido algo extraño, ¡lo siento!")


"""
EJERCICIO 3
Los alumnos de 1º de DAWBIO realizaran un viaje a Port Aventura a final de curso, el precio de la entrada general es de 45€.
Al grupo se le aplicará un descuento dependiendo del número de alumnos:
    • Si alumnos > 50 --> 30%
    • Si alumnos entre 20  y 50 --> 20%
    • Si alumnos entre 10 y 20 € --> 10%
    • Si alumnos es <  10 € --> 0%
    • Profesor de programación --> entrada libre.

Se realizará un descuento adicional del 15% a los alumnos menores de 18 años. La cantidad de alumnos
menores del grupo se ha de indicar para obtener el precio final.

El programa mostrará el importe total a pagar para los mayores de edad, el importe a pagar para los menores de edad y 
el importe total del grupo.
"""

while True:
    try:
        alumnos = int(input("Introduce la cantidad total de alumnos: "))
        menores = int(input("Introduce la cantidad de menores de edad: "))
        if (alumnos or menores) < 0:
            raise Exception ("Números negativos.")
        else:
            precio_entrada = 45
            precio_menores = (precio_entrada * 0.85)
            precio_con_descuento = 0

            if alumnos > 50:
                precio_con_descuento = precio_entrada * 0.70
            elif 20 < alumnos <= 50:
                precio_con_descuento = precio_entrada * 0.80
            elif 10 < alumnos <= 20:
                precio_con_descuento = precio_entrada * 0.9
            else:
                precio_con_descuento = precio_entrada

            coste_menores = menores * precio_menores
            coste_adultos = ((alumnos - menores) * precio_con_descuento)
            print("Los menores deberán pagar un total de: " + str(coste_menores))
            print("Los mayores de edad deberán pagar un total de: " + str(coste_adultos))
            print("El coste total es de: " + str(coste_adultos + coste_menores))
        break

    except ValueError:
        print("Debes introducir un valor entero.")
    except (SyntaxError, NameError):
        print("¿Seguro que el código está bien...?")
    except Exception as Error:
        print("Debes introducir valores positivos.")
    except:  # <-- POR DEFECTO, siempre el último except
        print("Ha sucedido algo extraño, ¡lo siento!")


"""
EJERCICIO 4
Dadas las listas:
alumno1 = random de 10 notas
alumno2 = random de 10 notas
alumno3 = random de 10 notas

4.1 - Crea una lista de diccionarios:
           alumno1 = {"nombre":"Pepe", "Pt1":5, "Pt2":3,...}
4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.
4.3 - Compararemos las notas de cada alumno indicando, en cada práctica, cuál tiene la nota + alta.
4.4 - Mostraremos sus notas en formato tabla:

    Alumno1 "nombre"
    ----------------
    Pt1 -- 2
    Pt2 -- 6
    ...
    Pt10 -- 8
"""
