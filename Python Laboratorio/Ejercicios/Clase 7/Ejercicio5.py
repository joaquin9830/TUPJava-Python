#Ejercicio 5: Sistema de calificaciones
#El objetivo del programa será crear un sistema de calificaciones
#de la siguiente manera:
#Le pedimos al usuario que ingrese un valor del 0 al 10


#Pedimos al usuario la calificación
calificacion = float(input("Digite la calificación: "))

#Imprimimos por pantalla según corresponda
if calificacion >= 9 and calificacion <= 10:
        print("Su calificación es: A")
elif calificacion >= 8 and calificacion < 9:
    print("Su calificación es: B")
elif calificacion >= 7 and calificacion < 8:
    print("Su calificación es: C")
elif calificacion >= 6 and calificacion < 7:
    print('Su calificación es: D')
elif calificacion >= 0 and calificacion < 6:
    print("Su calificación es: F")
else: print("Digite una calificación válida")