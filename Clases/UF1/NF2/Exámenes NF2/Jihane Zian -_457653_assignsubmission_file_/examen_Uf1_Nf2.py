# """EXAMEN NF2"""
# """ 
# EXAMEN NF2 - MATRICES, DICCIONARIOS Y CONTROL DE ERRORES --------------------------------------------

# -----------------------------------------------------------
# EJERCICIO 1  ----------------------------------------------
# -----------------------------------------------------------
# - Pedir al usuario su nombre y su DNI sin letra.
# - Crear un diccionario con la key : nombre y el value : DNI con la letra.
# - Mostrar todos los datos en forma de tabla.

#                     Usuarios
#                     ---------
#                     Nombre --> XXXXXXXX-X

# Las letras son: TRWAGMYFPDXBNJZSQVHLCKE
# Y las letras se relacionan del 0 al 22:
# 0 = T
# 1 = R
# 2 = W
# etc..."""

# nombre:str=input("indique su numbre")
# dni:str=input("indique su dni")

# deccionario={} 
# deccionario={"nombre":"el value"}
# print(deccionario)
# print(deccionario["nombre":"el value"])
# DNI=int(input("intrduce el dni:"))
# mod=dni%22
# letra=""
# if mod==0:
#   letre="T"
# elif mod==1:
#   letra="R"
# elif mod==2:
#   letra="W"
# elif mod==3:
#   letra="A"
# elif mod==4:
#   letra="G"
# elif mod==5:
#   letra="M"  
# elif mod==6:
#   letra="Y"  
# elif mod==7:
#   letra="F" 
# elif mod==8:
#   letra="P" 
# elif mod==9:
#   letra="D"    
# elif mod==10:
#   letra="X"  
# elif mod==11:
#   letra="B"  
# elif mod==12:
#   letra="N" 
# elif mod==13:
#   letra="J"  
# elif mod==14:
#   letra="Z"  
# elif mod==15:
#   letra="S"  
# elif mod==16:
#   letra="Q"  
# elif mod==17:
#   letra="V"  
# elif mod==18:
#   letra="H"  
# elif mod==19:
#   letra="L"  
# elif mod==20:
#   letra="C"
# elif mod==21:
#   letra="k"  
# elif mod==22:
#   letra="E"  
# print("la letra de el dni:"+letra+ ".por lo que el dni comleto es:"+str(dni)+letra)  


-----------------------------------------------------------
# """EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
# -----------------------------------------------------------
# - Pedir al usuario 2 números.
# - While hasta que le introduzcamos 'X' en el primer valor
# - Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
# """
# numero_uno=()
# numero_dos=()
# resultado=()
# int=(input(introduce el numero de operacio qui querimos realizar))
# if operacion==1
# numero_uno=int(input("ingreso el premiro numero":))
# numero_dos=int(input("ingreso el segundo numero":))
# except ValueError:
# print:("ese no es un numero")
# else:
#      resultado=numero_uno+numero_dos
#      print("el resultado de la suma es:"+str(resultado))
# elif operacion ==2


-----------------------------------------------------------
EJERCICIO
3: HUNDIR
LA
FLOTA - -----------------------------
-----------------------------------------------------------
El
código
va
a
crear
un
tablero
de
4
x4
y
va
a
colocar
2
barcos
en
él.El
código
debe
permitir, fácilmente, cambiar
la
posición
de
los
barcos
antes
de
lanzar
el
programa.

# Antes de empezar a jugar:
- Creamos
un
tablero
de
4
x4
vacío('A')
- Colocamos
2
barcos(posición
con
'B'), uno
de
2
celdas
y
otro
de
3
celdas(horizontal
o
vertical
pero
que
no
solapen)

# Al iniciar el programa...
- Mostrar
el
menú
de
juego(diccionario
o
lista) y
tablero
inicial
con
los
barcos:
1 - Jugar
0 - Salir
menu = {
    "1": "jugar"
         "0":"salir"
}

barcos = {}
opcion = ''
while opcion != '2':
    if opcion == '0':
        nif = input('salir ')
    if opcion == '1':
        nif = input('jugar')
    if nif in barcos:
        del barcos[nif]
else:

- En
random, hacemos
tiradas:
- devolver
posición
de
la
tirada
- devolver
agua(cambiar
la
casilla
vacía
'A'
por
'X') o
tocado(cambiar
la
casilla
de
barco
'B'
por
'T')
- devolver
estado
del tablero
- Esperar
'ENTER'
para
siguiente
tirada
- Al
completar
6
tiradas, deberemos
devolver
un
mensaje
según
si
hemos
conseguido
hundir
todos
los
barcos
o
no

EJEMPLO
DEL
1
ER
TURNO - ---------------------------------------------------
-  Mostramos
el
tablero
al
empezar
el
juego:
0
1
2
3
0
A
B
B
A
1
A
A
A
B
2
A
A
A
B
3
A
A
A
B

- Vemos
las
posiciones
del disparo:
Se
dispara
en
la
posicion
x: 0
y: 1
Tocado!

- Mostramos
el
tablero
con
las
modificaciones:
0
1
2
3
0
A
T
B
A
1
A
A
A
B
2
A
A
A
B
3
A
A
A
B
- Esperamos
al
siguiente
turno: "Pulsa ENTER para continuar..."

--------------------------------------------------------------------------------------------------- """
