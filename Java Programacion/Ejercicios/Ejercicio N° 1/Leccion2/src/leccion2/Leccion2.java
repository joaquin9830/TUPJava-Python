
package leccion2;

import java.util.Scanner;


public class Leccion2 {

 
    public static void main(String[] args) {
        /*
        var condicion = true;
        if(condicion){
            System.out.println("condicion verdadera"); //Condicional simple
        }
        else{
            System.out.println("condición falsa"); //Condicional doble
        }
*/
        
        
//        var numero = 2;
//        var numeroTexto = "Número desconocido";
//        
//        if(numero == 1){
//            numeroTexto = "Número uno";
//        }else if(numero == 2){
//            numeroTexto = "Número dos";
//            
//        }else if(numero == 3){
//            numeroTexto = "Número tres";
//            
//        }else if(numero == 4){
//            numeroTexto = "Número cuatro";
//            
//        }else{
//            numeroTexto = "Número no encontrado";
//        }
//        
//        System.out.println("El número es el: " + numeroTexto);
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número: ");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTexto = "Valor desconocido";
        switch(numero){
            case 1:
                numeroTexto = "Número 1";
                break;
            case 2:
                numeroTexto = "Número 2";
                break;
            case 3:
                numeroTexto = "Número 3";
                break;
            case 4:
                numeroTexto = "Número 4";
                break;
            default:
                numeroTexto = "Por favor digite un valor correcto";
        }
        System.out.println(numeroTexto );
        
    }
    
}
