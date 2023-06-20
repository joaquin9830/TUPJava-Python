# CLASE 6 Sentencia de control if/else
'''
condicion = True
if (condicion == True):
    print("Es verdadero")
elif (condicion == False):
    print("Es falso")
else:
    print("Condición sin especificar")
'''
'''
num = int(input("Digite un número en el rango del 1 al 3: "))
numTexto = ""
if num == 1:
    numTexto = "Número uno"
elif num == 2:
    numTexto = "Número dos"
elif num == 3:
    numTexto = "Número tres"
else:
    numTexto = "Has ingresado un número fuera de rango"

print(f'El número ingresado es {num} - {numTexto}')
'''
#OPERADOR TERNARIO
condicion = True
print("Condición Verdadera") if condicion else print("Condición Falsa")