"""
Clase 20 de septiembre 20200
"""
"""
If, else y elif
"""

num = 100
print("HACEMOS LAS COMPROBACIONES CON IF")
print("Primera comprobación.")
if num > 0:
    print("+0")
print("Segunda comprobación")
if num > 20:
    print("+20")
print("Tercera comprobación")
if num > 50:
    print("+50")
print("Cuarta comprobacion.")
if num < 100:
    print("-100")

print("Fin. El numero era el: " + str(num))

print("HACEMOS LAS COMPROBACIONES CON ELIF")
if num < 0:
    print("+0")
elif num > 20:
    print("+20")
elif num > 50:
    print("+50")
elif num < 100:
    print("-100")


