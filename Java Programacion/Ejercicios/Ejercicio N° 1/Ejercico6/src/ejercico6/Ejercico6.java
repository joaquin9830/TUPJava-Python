
package ejercico6;

import java.util.Scanner;

/**
 *
 * @author joaqu
 */
public class Ejercico6 {

  
    public static void main(String[] args) {
        
        //Guillermo tiene N dólares. Luis tiene la mitad de
        //lo que posee Guillermo. Juan tiene la mitad de lo que
        //poseen Luis y Guillermo juntos. Hacer un programa
        //que calcula e imprima la cantidad de dinero que
        //tienen entre los tres.
        //Crear un nuevo proyecto llamado Ejercicio6
        
        Scanner entrada = new Scanner(System.in);
        //Definimos las variables como float
        float dolaresG,dolaresJ, dolaresL, resultado;
        //Pedimos al usuario la cantidad de dolares de Guillermo
        System.out.println("Digite la cantidad de dolares que posee Guillermo: ");
        dolaresG = Float.parseFloat(entrada.nextLine());
        //Realizamos las operaciones
        dolaresL = dolaresG / 2;
        dolaresJ = (dolaresG + dolaresL) / 2;
        resultado = dolaresG + dolaresL + dolaresJ;
        //20 + 10 + 15
        //Imprimimos el resultado del total
        System.out.println("El total de los dolares es: " + resultado);
       
    }
    
}
