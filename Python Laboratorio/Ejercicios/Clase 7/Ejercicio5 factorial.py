#Calcular el factorial de un numero mayor o igual a 0

#Pedimos al usuario que ingrese un numero
numero = int(input("Ingrese un número mayor o igual a 0: "))
factorial = 1
i = 1

if numero >= 0:
    while i <= numero:
        factorial *= i
        i += 1
    # Mostramos por pantalla el resultado
    print(f"El factorial del numero {numero} es {factorial}")
else:
    print("Digite un valor mayor a 0")



