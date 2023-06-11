'''
#Clase N° 2 Variables en python
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))

# Clase N°3 Tipos de datos en python
a: str = "Hola mundo"
b = True
c = 10
d = 10.90
#Nos muestra el tipo de datos que estamos manejando
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Manejo de cadenas (String)
miGrupoFavorito = "AC/DC"
caracteristica = "The best rock band"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristica)

numero1 = "7"
numero2 = "8"
#Pasamos de string a entero
print(int(numero1) + int(numero2))

#Booleanos
miBoolean = 10 > 2
miBoolean2 = False

print(miBoolean)

if miBoolean:
    print("El resultado es verdadero")
else:
    print("El restulado es falso")

#Procesar la entrada del usuario
#Función input
#resultado = input("Digite un número: ") #Regresa un dato tipo string
#print(resultado)

#Conversión de entrada de datos en input

x = input("Digite un número: ")
z = input("Digite el segundo número: ")
resultado = int(x)+ int(y)

print("El resultado es:", resultado)


#Clase N°4 operadores en python

operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print("El resultado es:", suma)
print(f"El resultado de la suma es: {suma}") #Esto se llama interpolación

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicación es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la división es: {division}")

exponente = operandoA ** operandoB
print(f"El resultado de la exponenciación es: {exponente}")

modulo = operandoA % operandoB
print(f"El resultado de la operación es: {modulo}")
'''
'''
#Ejercicio area de un rectángulo
#Se solicita calcular el área y el perímetro de un rectángulo.
alto = int(input("Por favor digite el alto del rectangulo:"))
ancho = int(input("Por favor digite el ancho del rectangulo:"))
area = alto * ancho

perimetro= (alto + ancho) *2
print(f"El area del rectángulo es: {area} y el perimetro del mismo es: {perimetro}")
'''

'''
miVariable3 = 10
print(miVariable3)

#Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

miVariable3 -= 1
print(miVariable3)

miVariable3 *= 3
print(miVariable3)

miVariable3 /= 2
print(miVariable3)

###Operadores de comparación

a = 4
b = 2

resultado = a == b
print(resultado)

#Operador diferente

resultado = a != b
print(resultado)

#Operador Mayor que
resultado = a > b
print(resultado)

#Operador menor que
resultado = a < b
print(resultado)
'''

#Ejercicio: Número par o impar
#Solicitamos que el usuario ingrese un número
#Este se asigna a una variable
#Utilizamos la estructura 'if else'


numero = int(input("Por favor digite un número:"))

if (numero % 2 == 0):
    print(f"El numero: {numero} es par")
else:
    print(f"El número {numero} es impar")

#Ejercicio: Es mayor de edad
#Pedir un número al usuario
#Almacenar el valor en una variable
#Usar la estructura 'if else'

edad = int(input("Por favor ingrese su edad: "))

if edad >= 18:
    print(f"Usted tiene {edad} y es mayor de edad")
else:
    print(f"Usted tiene {edad} y es menor de edad")