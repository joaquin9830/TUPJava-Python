#Pedir al usuario que ingrese un mes del año, el valor debe ser entre 1 y 12
#luego le decimos en que estación del año esta:

#Pedimos al usuario un mes
mes = int(input("Digite un mes del año: "))

#Comparamos el valor de la variable con los números
#En caso de coincidir imprimos por pantalla la estación
if 1 <= mes <= 3:
    print("Estamos en la estación verano")
elif 4 <= mes <= 6:
    print("Estamos en la estación otoño")
elif 7 <= mes <= 9:
    print("Estamos en la estación invierno")
elif 10 <= mes <= 12:
    print("Estamos en la estación primavera")
else:
    print("Digite un valor válido")
