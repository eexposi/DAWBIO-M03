"""Clase viernes 16 sept. 2022"""

# FUNCIÓN PRINT
print("Hola")

# Print sin argumentos es un salto de linea
print()

# Tambien si indicamos \n pondremos un salto de linea
print("Hola\nSaltamos linea")

# Y si queremos que muestre \n ponemos la barra, con el caracter de escape

print("Hola\\nque tal")

# Argumento de separacion
print("nombre", "apellido", "edad", sep=" - ")

# Argumento de salida. Es como termina el print
print("Y si pongo end=--> el print acaba con... ", end="-->")
print()

# OPERACIONES
"""
    Las operaciones validas son:
        +: suma
        -: resta
        *: multiplicación
        /: división
        %: modulo --> el resto de la división entre los datos
        **: exponente. 2 elevado a 3 = 2 ** 3
        //: división entera. 1 // 2 = 0. Redondea hacia abajo
        
    Tengamos en cuenta que la notación científica es:
    2 x 10 ** 3 == 2e3
"""
print(2 * 10 ** 3)
print(2e3)

# VARIABLES
"""
    Convención y normas para variables:
        - Empiezan por una letra
        - Siempre en minúsculas
        - Separadas por "_"
        - Constantes en MAYUSCÚLAS
    
    ¡¡OJO!! con las palabras clave: import, break, case.... No se pueden asignar como nombre de variable.
"""

soy_una_variable = 1
Y_YO_UNA_CONSTANTE = "hola"

"""
Tipos de variables

int
str
float
complex
tuplas
array
Boolean
diccionarios
"""

var: int = 1
var: str = "1"
var: float = 1.1
var: complex = 1j
var: tuple = (1, 2)  # No se pueden modificar
var = [1, 2]  # array
var: bool = True  # o False
var: dict = {"key": "value"}

# RECORDEMOS

var1 = "Hola"
var2 = "Adios"
res = var1 + var2  # Al ser string, se concatenan
print(res)
res = var1 * 3  # Al ser string, aparecerá repetida

# Y podemos acortar operaciones
"""
    var = var + 1   ======= var += 1
"""
var = 1
var = var + 1
print(str(var))
var = 1
var += 1
print(str(var))

# Entrada de teclado
var = input("Pon tus datos: ")
"""
 Lo obtenido en var siempre es una cadena/string. Y si necesitamos otro tipo de datos vamos a
 forzar el cambio de variable, o castear.
 
 int()
 str()
 float()
 etc...
"""

# ------- Tras los ejercicios 1 y 2 ------------ Condicionales
# Empezamos con los condicionales sin IF

var1 = 1
print(var1 == 3)  # Sera false porque no se cumple la condicion
print(var1 < 10)  # Esta si se cumple

"""
Estructura

if (condicion):
    {
    Lo que se ejecutará si se cumple la condicion.
    }
else:
    {
    lo que se ejecutara si NO se cumple
    }
"""

var = 1
if var == 1:
    print("Es igual a 1")
else:
    print("No es igual a 1")

"""
Operadores:

== 
!=
>
<
>=
<=

(True) 

Podemos concatenar condiciones:

and y or
"""

var1 = 10
var2 = -10

if var1 > 0 and var2 < 0:
    print("Ambas cumplen las condiciones")

if var1 > 0 or var2 < 0:
    print("Una cumple la condicion")
