#Ejercicio N°4
#Hacer un programa para ingresar el radio de un circulo,
#se reporte su área y la longitud de la circunferencia

from math import pi
#Solicitamos al usuario que ingrese el valor del radio
radio = float(input("Digite el radio de la circunferencia: "))

#Calculamos el área
area = pi * radio ** 2
#Calculamos la longitud
longitud = 2 * pi * radio
#Imprimimos el resultado
print(f"El área de la circunferencia es: {area} y su longitud es: {longitud}")
