#Ejercicio4 Etapas de la vida
#Haremos un programa que cuando el usuario ingrese
#su edad le diga, o imprima la etapa de su vida en
#una breve oración.
#0 a 10 = La infancia es increible
#10 a 19 = Tienes muchos cambios, mucho que estudiar
#20 a 29 = Amor y comienza el trabajo

edad = None
#pedimos los datos al usuario
edad = int(input("Digite su edad: "))

#Imprimos en pantalla la etapa
if edad >= 0 and edad <= 10:
        print("La infancia es increíble")
elif edad >= 11 and edad <= 19:
         print("Tienes muchos cambios, mucho que estudiar")
elif edad >= 20 and edad <= 29:
         print("Amor y comienza el trabajo")
elif edad >= 30 and edad <= 39:
        print("Ya tienes tu vida encaminada")
elif edad >= 40 and edad <= 49:
    print("Tus hijos ya crecieron")
elif edad >= 50 and edad <= 59:
    print("Estas cerca de jubilarte")
elif edad >= 60 and edad <= 69:
    print("Te jubilaste, dedicate a viajar")
else:
    print("Quien sabe qué te depara el destino")

