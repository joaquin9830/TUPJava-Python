#Ejercicio 8: Dada las horas trabajadas de 5 personas
# y la tarifa de pago calcular el salario,
# y la sumatoria de todos los salarios.

i = 1
horas = 0
sumaSalarios = 1

#Recorremos las 5 personas con el ciclo while
while i <= 5:
    #Pedimos al usuario el salario y las horas trabajadas
    print(f"Salario del empleado: {i}")
    horas = int(input("Digite la cantidad de horas trabajadas: "))
    tarifa = float(input("Digite la tarifa por hora: "))

    salario = tarifa * horas
    print(f"El salario es: $ {salario}")
    sumaSalarios += salario
    i += 1
#Imprimos la suma de los salarios
print(f"La suma de los salario es: {sumaSalarios}")
