"""
PARTE 1:
- Haz que funcione el código, y se muestren los 3 prints con las 3 listas

PARTE 2:
- Haz que el codigo principal (sin contar las listas) sea de 1 linea
"""


lst = ["Blanco", "Verde", "Amarillo", "Rojo", "Azul"]
lst2 = ["Blanco", "Negro", "Rojo", "Gris", "Naranja"]

def mostrar_lista(lst):
    for e in lst:
        print(e)

def get_coincidencias(lst, lst2):
    comparacion = []
    for i in lst:
        if lst[i] in lst2:
            comparacion.append(lst[i])
    return comparacion


mostrar_lista(lst[2])
print("LST2")
mostrar_lista(lst2)

lista_comparada = get_coincidencias(lst)
print("LST COMPARADA")
mostrar_lista(lista_comparada)


