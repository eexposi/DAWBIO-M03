import random

tabla =[["A", "A", "A", "A"],["A", "B", "B", "A"],["A", "A", "A", "A"],["B", "B", "B", "A"]]
tablaposicion = [[" ",0,1,2,3],[0,"A", "A", "A", "A"],[1,"A", "B", "B", "A"],[2,"A", "A", "A", "A"],[3,"B", "B", "B", "A"]]
tiradas = 0
result = 0
while True:
    for i in tablaposicion:
        print(i[0],i[1],i[2],i[3],i[4])
    menu = ["1 - Jugar", "2 - Salir"]
    for i in menu:
        print(i)
    try:
        opcion = int(input("Entra una opcion: "))
        if opcion == 2:
            break
        if opcion == 1: 
            tiradas += 1
            print("Numero de tiradas = ", tiradas)
            print ("Empieza el juego")
            x = random.randint(0,3)
            y = random.randint(0,3)
            print(x,y)
            print("Se dispara en la posicion x: ", x , "y: ", y)
            if tabla[x][y]=="B":
                tabla[x][y] = "T"
                print("Tocado!")
                result+= 1
                a = input("Pulsa ENTER para continuar...")
                if a == " ":
                    pass
                else:
                    print("Has tenido exito", result, "veces" )
                    break
            if tiradas == 6:
                print("Has jugado 6 veces  y has tenido exito", result, "veces" )
                break
        else:
            print("El numero de opción introducido no es valido")
    except ValueError:
        print("Deberias introduci")