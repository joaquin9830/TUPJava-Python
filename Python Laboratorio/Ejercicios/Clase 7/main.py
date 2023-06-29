#Clase 7 ciclo while (Mientras o durante)
"""
contador = 0

while contador < 78:
    print(f"Ejecutando el ciclo while {contador}")
    contador += 1
else:
    print("Fin del ciclo while")
"""
#Imprimir números del 0 al 5 con el ciclo while
"""
contador = 0
while contador <= 5:
    print(contador)
    contador +=1
else:
    print("Fin del ciclo while")
"""
#Imprimir números del 5 al 1 con el ciclo while

"""
contador = 5
min = 1

while contador >= min:
    print(contador)
    contador -= 1
else:
    print("Fin del ciclo while")
"""
#Ciclo for
"""
cadena = "Hello world"

for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo for")
"""
#Palabra reservada break
"""
for letra in "Alemania":
    print(letra)
    if letra == "a":
        print(f"Letra {letra} encontrada")
        break
else:
    print("Fin del ciclo for")
"""
#Palabra reservada continue
for i in range(6):
    if i % 2 == 0:
        print(f"Valor: {i}")

for i in range(6):
    if i % 2 != 0:
        continue
    print(f"Valor: {i}")
