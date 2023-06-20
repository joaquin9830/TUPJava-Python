#Intercambiar el valor de dos variables

a = int(input("Digite el valor de a: "))
b = int(input("Digite el valor de b: "))
c = ""

c = a
a = b
b = c
print(f"El valor de la variable a es: {a} y el de la variable b: {b}")