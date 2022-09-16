"""



"""
i = 0
while i != 100:
    i += 1
    print(i)
for i in range(10): #si empieza de 0, no necesitamos primer punto
    print(i)
for i in range(0, 100, 5):# el tercer numero nos hace ir saltando de 5 en 5
    print(i)

"""
Instrucción break: corta el flujo finalizando las acciones
instrucción continue: en ese momento, la iteración se repite. Sin acabar todas sus instrucciones, vuelve al
inicio como una vuelta mas
"""

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")


"""
Idea de ejercicio de fors y cadenas

Tu programa debe:

Pedir al usuario que ingrese una palabra.
Utilizar userWord = userWord.upper() para convertir la palabra ingresada por el usuario a
 mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
Usa la ejecución condicional y la instrucción continue para "comer" las siguientes vocales
 A , E , I , O , U de la palabra ingresada.
Asigne las letras no consumidas a la variable palabrasinVocal e imprime la variable en la pantalla.
Analiza el código en el editor. Hemos creado palabrasinVocal y le hemos asignado una cadena vacía. 
Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en
 una cadena más larga durante los siguientes giros de ciclo, y asignarlo a la variable palabrasinVocal."""


# Whuile i for tienen escape else, que se ejecuta siempre
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)