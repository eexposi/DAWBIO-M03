""" CLASE 8 (15/11/22) -- REPASO FINAL PREVIO AL TEST DE LA UF1-NF2 """


""" EJERCICIO 1 (LISTAS) ---------------------------------------------------------------
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada 
asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar 
por pantalla las asignaturas que el usuario tiene que repetir.
"""

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprovadas = []
for asignatura in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "?"))
    if nota >= 5:
        aprovadas.append(asignatura)
for asignatura in aprovadas:
    asignaturas.remove(asignatura)
print("Tienes que repetir " + str(asignaturas))



""" EJERCICIO 2 (DICCIONARIOS) -----------------------------------------------------------------
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono,
correo, preferente), donde preferente tendrá el valor True si se trata de un cliente
preferente. El programa debe preguntar al usuario por una opción del siguiente menú:
    (1) Añadir cliente,
    (2) Eliminar cliente,
    (3) Mostrar cliente,
    (4) Listar todos los clientes,
    (5) Listar clientes preferentes,
    (0) Terminar.
En función de la opción elegida el programa tendrá que hacer lo siguiente:

    1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    3. Preguntar por el NIF del cliente y mostrar sus datos.
    4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    0. Terminar el programa
"""

clientes = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        nif = input('Introduce NIF del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección del cliente: ')
        telefono = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'}
        clientes[nif] = cliente
    if opcion == '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if opcion == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            print('NIF:', nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el cliente con el nif', nif)
    if opcion == '4':
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if opcion == '5':
        print('Lista de clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) '
                   'Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n'
                   '(6) Terminar\nElige una opción:')


    """ EJERCICIO 3 ----------------------------------------------------------------------------------
    Escribir un programa que genere un diccionario con la información del directorio, donde cada
    elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con
    el resto de la información del cliente. Los diccionarios con la información de cada cliente
    tendrán como claves los nombres de los campos y como valores la información de cada cliente
    correspondientes a los campos. Es decir, un diccionario como el siguiente:

    {'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 
                   'teléfono': '656343576', 'descuento': 12.5}, 
     '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 
                   'teléfono': '692839321', 'descuento': 8.0}, 
     '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 
                   'teléfono': '664888233', 'descuento': 5.2}, 
     '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 
                   'teléfono': '667677855', 'descuento': 15.7}}
    """

    # Cadena con los datos de los clientes de la empresa
    datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
    # Dividimos la cadena por el caracter de cambio de línea \n y creamos una lista con las subcadenas
    lista_clientes = datos_clientes.split('\n')
    # Inicializamos el diccionario que va a contener el directorio de clientes a vacío.
    directorio = {}
    # Dividimos la cadena del primer elemento de la lista de clientes (que contienen los
    # nombres de los campos) por el caracter ; y creamos una lista con los campos.
    lista_campos = lista_clientes[0].split(';')
    # Bucle iterativo para recorrer los elementos de la lista lista_clientes.
    # la variable cliente recorre desde el segundo elemento hasta el último elemento de la lista
    # (el primer elemento contiene los nombres de campo así que no corresponde a un cliente)
    for i in lista_clientes[1:]:
        # Inicializamos el diccionario que va a contener los datos del cliente actual a vacío.
        cliente = {}
        # Dividimos la cadena i por el caracter ; y creamos una lista con las subcadenas con la
        # información del cliente
        lista_info = i.split(';')
        # Bucle iterativo para recorrer los campos y añadir los pares al diccionario del cliente.
        # j toma valores de 1 al número de campos menos 1. El primer elemento (posición 0) corresponde
        # al nif y no se añade al diccionario porque se utilizará después como clave en el diccionario
        # principal
        for j in range(1, len(lista_campos)):
            # Condicional. Si el campo actual es descuento convertimos su valor en real
            if lista_campos[j] == 'descuento':
                lista_info[j] = float(lista_info[j])
            cliente[lista_campos[j]] = lista_info[j]
        # Añadirmos un par al diccionario del directorio con la clave el nif del cliente y valor
        # el diccionario que acabamos de crear con el resto de sus datos.
        directorio[lista_info[0]] = cliente
    # Mostramos el diccionario por pantalla
    print(directorio)