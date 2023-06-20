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
'''
'''
#Operadores lógicos

#and
a= False
b= True

resultado = a and b
print(resultado)

#or

resultado = a or b
print(resultado)

#not
resultado = not a
print(resultado)
'''
'''
#Ejercicio: Valor dentro de un rango
#Pedimos al usuario un valor numérico
#Verificar si el valor ingresado se encuentra entre el rango de 0 a 5

num = int(input("Por favor, digite un número:"))

if num >= 0 and num <= 5:
    print(f"El numero {num} está dentro del rango")
else:
    print(f"El numero {num} está fuera del rango")
'''
'''
#Ejercicio: Operador or
#La pregunta es si un padres puede asistir al juego de su hijo
#Verificamos si tiene vacaciones
#Verificamos si tiene día libre

tieneVacaciones = True
tieneDiaLibre = False

if (tieneVacaciones or tieneDiaLibre ):
    print("El padre podrá asistir al juego del hijo")
else:
    print("El padre NO podrá asistir al juego del hijo")
'''
#Ejercicio: Rango de edad 20 y 30 años
#1.Preguntasr la edad al usuario
#2.Si esta dentro de los 20 o 30 años, esta dentro del rango
'''
edad = int(input("Por favor digite su edad: "))

if (edad >= 20 and edad <= 30):
    print(f"La persona tiene {edad} años y está dentro del rango")
else:
    print(f"La persona tiene {edad} años y está fuera del rango")
'''
#Ejercicio: El mator de dos números
#Solicitar al usuario valores, determinar cual es el mayor
#Solicitar al usuario dos valores
#Se debe imprimir el mayor de los dos números
'''
num1 = int(input("Digite el valor del primer número: "))
num2 = int(input("Digite el valor del segundo numero: "))

if(num1 > num2):
    print(f"El numero {num1} es el mayor")
else:
    print(f"El numero {num2} es el mayor")
'''

#Ejercicio: Tienda de libros
#Mostrar: Ingrese los siguientes datos del libro
#Digite el nombre del libro
#Digite el ID del libro
#Digite el precio del libro
#Indicar si el envío es gratuito
'''
print("Por favor ingrese los siguientes datos del libro ")
nombreLibro = input("Ingrese el nombre: ")
idLibro = int(input("Ingrese el ID del libro: "))
precioLibro = float(input("Ingrese el precio del libro: "))
envioGratuito = input("Indique si el libro tiene envio gratis: ")
if (envioGratuito == "True"):
    envioGratuito = True
elif (envioGratuito == "False"):
        envioGratuito = False
else:
    envioGratuito = "Por favor digite de nuevo, los valores permitidos son: True o False"

print(f'''
 #           Nombre: {nombreLibro}
  #          ID:#{idLibro}
   #         Precio: ${precioLibro}
    #        Envio gratuito?: {envioGratuito}
#''')



