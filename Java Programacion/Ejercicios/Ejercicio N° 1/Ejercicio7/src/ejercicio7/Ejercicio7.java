
package ejercicio7;

import java.util.Scanner;

/**
 *
 * @author joaqu
 */
public class Ejercicio7 {

   
    public static void main(String[] args) {
        //Una compañía de venta de carros usados, paga a su personal
        //de ventas un salario $1000 mensuales mas una comisión
        //de $150 por cada carro vendido, más el 5% del valor  de la venta
        //por carro. Cada mes el capturista de la empresa
        //ingresa en la computadora los datos pertinentes.
        //Hacer un programa que calcule e imprimo el salario mensual
        //de un vendedor dado.
        //El salario de 1000 lo vamos a manejar como un dato
        //constante, para asignarlo debemos usar la palabra
        //reservada "final"
        //Ejercicio 7
        Scanner entrada = new Scanner(System.in);
        //Salario fijo de los vendedores
        final int salario = 1000;
        float  valorAuto, porcentajeV, totalPrecio, salarioMensual;
        int comision = 150, autosVendidos;
        //Solicitamos la cantidad de autos vendidos
        System.out.println("Digite la cantidad de autos vendidos: ");
        autosVendidos = Integer.parseInt(entrada.nextLine());
        //El valor de cada auto
        System.out.println("Digite el valor de un auto: " );
        valorAuto = Float.parseFloat(entrada.nextLine());
        
        //Comision por cada venta
        comision *= autosVendidos;
        //total
        totalPrecio = autosVendidos * valorAuto;
        //Porcentaje del 5%
        porcentajeV = totalPrecio * 0.05f;        
        //Salario mensual
        salarioMensual = salario + comision + porcentajeV;
        
            
        //Imprimos por pantalla el resultado 
        System.out.println("La cantidad de autos vendidos es: " + autosVendidos + ", por lo tanto el salario será de: " + salarioMensual);
        
    }
    
}
