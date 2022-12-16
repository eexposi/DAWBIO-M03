# Sesión 13/12/22

""" EJERCICIO 1: MÉTODO QUE RECIBE EL NÚM. DE DNI Y DEVUELVE SU MÓDULO """

def dev_modulo1 (dni):
   return dni%23

""" EJERCICIO 2: MODIFICA EL MÉTODO PARA QUE RECIBA EL NÚM. DE DNI 
+ STRING CON TODAS LAS LETRAS Y DEVUELVA SÓLO LA LETRA """

def dev_modulo2 (dni, letras):
   return letras[dni%23]

""" EJERCICIO 3: MEDIANTE EL MÉTODO ANTERIOR, USARLO PARA DEVOLVER EL DNI+LETRA """
dni = 46450159
str = "TRWAGMYFPDXBNJZSQVHLCKE"
letra = dev_modulo2(dni,str)
print("El DNI completo es ", dni, "-", letra)

""" EJERCICIO 4: MÉTODO QUE COMPRUEBE SI EL PARÁMETRO "STR" COINCIDE CON 
 UNA CONSTANTE DEFINIDA PREVIAMENTE """
def comprobar_nombre (str):
    return CONSTANTE == str

CONSTANTE = "Eric"
palabra = input("Introduce una palabra y prueba suerte: ")
if comprobar_nombre(palabra):
    print("Has acertado!")
else:
    print("No has acertado ;(")

""" EJERCICIO 5: MÉTODO QUE DEVUELVE SI LA LONGITUD DE UN "STR" PASADO POR 
PARÁMETRO ES >= 8 """
def longitud(str):
    if len(str) >= 8:
        return True
    else:
        return False

""" EJERCICIO 6: MÉTODO QUE DEVUELVE TRUE/FALSE SI LOS MÉTODOS "COMPROBAR_NOMBRE"
Y "LONGITUD" DEVUELVEN TRUE/FALSE """
def todo_ok(str):
    if comprobar_nombre(str) and longitud(str):
        return True
    else:
        return False

palabra2= "hipermetropia"
print("Has acertado: ", todo_ok(palabra2))            # Dará False porque la CONSTANTE no concuerda

""" EJERCICIO 7: PROGRAMA QUE, AL LLAMAR A LOS MÉTODOS ANTERIORES, PRINTE
"Has acertado: TRUE/FALSE" SEGÚN LOS RETURNs RECIBIDOS """
# Hecho justo encima...

""" EJERCICIO 8: """
def get_nom_completo():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    return nombre + " " + apellido

nombre_completo = get_nom_completo()
print(nombre_completo)

""" EJERCICIO 9: """
def get_multiple10 (dato):
    multiple = dato*10
    return multiple

mult = get_multiple10(2)
if mult < 100:
    print("OK")
else:
    var1 = get_multiple10(get_multiple10(mult))

""" EJERCICIO 10: """
def sum_num(num2,num1):
    return num1/num2

numero1 = 5
numero2 = 10
res = sum_num(num1=numero2, num2=numero1)
print(res)

res = sum_num(numero2, numero1)
print(res)

# """ EJERCICIO 11: """
# def get_letra(lista,5):
#     return lista[index]
#
# lst = "Voy a suspender"
# indice = 5
# print(get_letra(lst,indice))
#
# """ EJERCICIO 12: """
# def multiplicar(dato):
#     r = dato*20
#     if r < 100:
#         multiplicar(r)
#     else:
#         return r-100
#
# print(multiplicar(2))
#
# """ EJERCICIO 13: """
# def resta(num):
#     return num-1
#
# for i in range(100):
#     print(resta(i),"_",end="")