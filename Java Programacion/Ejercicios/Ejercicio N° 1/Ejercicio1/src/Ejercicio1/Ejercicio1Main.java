//Tienda de libros
package Ejercicio1;

import java.util.Scanner;


public class Ejercicio1Main {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el nombre del libro: ");
        String nombreLibro = entrada.nextLine();
        System.out.println("Digite el id del libro: ");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el precio del libro:  ");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("Confirme si el envio es gratis: ");
        boolean envioGratuito = Boolean.parseBoolean(entrada.nextLine());
        
        
         
        System.out.println(nombreLibro+" #" +idLibro);
        System.out.println("El precio es: $" + precioLibro);
        if(envioGratuito){
            System.out.println("El envío es gratuito");            
        }else{
            System.out.println("El envío no es gratuito");
        }
        
    }
}
