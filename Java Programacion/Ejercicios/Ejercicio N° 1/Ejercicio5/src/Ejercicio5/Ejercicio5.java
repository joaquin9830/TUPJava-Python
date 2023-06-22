
package Ejercicio5;

import java.util.Scanner;

/**
 *
 * @author joaqu
 */
public class Ejercicio5 {
    public static void main(String[] args) {
//        Hacer un programa que calcule e imprima la suma de tres calificaciones.
//        Pedir las calificaiones al usuario, crear un proyecto nuevo llamado Ejercicio5
                
         
        Scanner entrada = new Scanner(System.in);
       
        float calificacion1, calificacion2, calificacion3, resultado;
        
       //Pedimos al usuario las calificaciones
        System.out.println("Digite las 3 calificaciones: " );
        calificacion1 = Float.parseFloat(entrada.nextLine());
        calificacion2 = Float.parseFloat(entrada.nextLine());
        calificacion3 = Float.parseFloat(entrada.nextLine());
        //Calculamos
        resultado = calificacion1 + calificacion2 + calificacion3;
        //Mostramos por pantalla el resultado
        System.out.println("El resultado de las 3 calificaiones es: " + resultado);
    }
    
}
