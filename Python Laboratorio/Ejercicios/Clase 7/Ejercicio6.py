# Ejercicio 6: Ingresar “N” enteros, visualizar
# la suma de los números pares de la lista,
# cuántos números pares existen y cuál es
# el promedio de los números impares.

# Solicitamos los elementos al usuario
nElementos = int(input("Digite la cantidad de N elementos a ingresar: "))

# Iinicializamos las variables en 0
i = 1
sumaPares = 0
sumaImpares = 0
conteoImpares = 0
conteoPares = 0

# Recorremos los elementos
while i <= nElementos:
    num = int(input("Digite un numero: "))

    if num % 2 == 0:
        sumaPares += num
        conteoPares += 1
    else:
        sumaImpares += num
        conteoImpares += 1
    i += 1
if conteoPares == 0:
    print("No se encontraron pares")

else:
    print(f"La suma de los numeros pares es: {sumaPares}")

if conteoImpares == 0:
    print("No se encontraron impares")
else:
    promedioImp = sumaImpares / conteoImpares
    print(f"La suma de los numeros impares es: {sumaImpares} y su promedio es: {promedioImp}")