
import java.util.Scanner;

//primer programa con Java

public class HolaMundo {
    
    public static void main(String[] args) {
        /*System.out.println("Hola mundo nuevamente");
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
        
        //Var - inferencia de tipos en java
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos ejercitando";
        System.out.println("miVariableEntera2 es: " + miVariableEntera2);
        //soutv + tab
        System.out.println("miVariableCadena2 = " + miVariableCadena2);

        //Concatenación
        var usuario = "Joaquín ";
        var titulo = "Técnico en investigación de la escena del crimen";
        var union = usuario + titulo;
        System.out.println("union = " + union);
        
        //Suma 
        var a = 40;
        var b = 60;
        var suma = a + b;
        System.out.println("suma = " + suma);
        
        
        //Clase Scanner
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre= ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        
        System.out.println("Escriba el título= ");
        var titulo2 = entrada.nextLine();
        System.out.println("titulo2 = " + titulo2);
    
        //Ejercicio libro = título y autor
        
        Scanner ingresar = new Scanner(System.in);
        System.out.println("Digite el título del libro = " );
        var titulo = entrada.nextLine();
        System.out.println("Digite el autor del libro = ");
        var autor = entrada.nextLine();
        
        System.out.println("El libro = " + titulo + " fue escrito por "+autor);
        
        
        //Datos primitivos
        byte numEnteroByte  = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor mínimo byte:  " + Byte.MIN_VALUE);
        System.out.println("Valor máximo byte:  " + Byte.MAX_VALUE);
        
        short numEnteroShort  = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor mínimo short:  " + Short.MIN_VALUE);
        System.out.println("Valor máximo short:  " + Short.MAX_VALUE);
        
        int numEnteroInt  = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor mínimo int:  " + Integer.MIN_VALUE);
        System.out.println("Valor máximo int:  " + Integer.MAX_VALUE);
        
        long numEnteroLong  = 10;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor mínimo long:  " + Long.MIN_VALUE);
        System.out.println("Valor máximo long:  " + Long.MAX_VALUE);
        
        float numFloat  = 3.4028235E38F;
        System.out.println("numEnterofloat = " + numEnteroLong);
        System.out.println("Valor mínimo float:  " + Float.MIN_VALUE);
        System.out.println("Valor máximo float:  " + Float.MAX_VALUE);
        
        double numDouble  = 1.7976931348623157E308D;
        System.out.println("numEnterofloat = " + numEnteroLong);
        System.out.println("Valor mínimo double:  " + Double.MIN_VALUE);
        System.out.println("Valor máximo double:  " + Double.MAX_VALUE);
        */
        
        //Inferencia de tipos var y tipos primitivos 
        /*
        var numEntero = 20; //Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F;
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
        */
        /*
        //Tipos primitivos char
        
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024'; //Indicamos a Java la asignación con el código unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; //Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; //Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        */
        //Tipos primitivos tipos booleanos
        
        /*
        boolean varBool = true;
        System.out.println("varBool = " + varBool);
        if(varBool){
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja");
        }
        
        //Algoritmo para determinar si es mayor de edad
        int edad = 34;
        
        if(edad >= 18){
            System.out.println("Es mayor de edad");
        }else{
            System.out.println("No es mayor de edad");
        }
*/
        
        //Conversión de tipos primitivos
        /*
        var edad = Integer.parseInt("20");
        System.out.println(edad );
        var pi = Double.parseDouble("3.14");
        System.out.println("pi = " + pi);
        
        var entrada =  new Scanner(System.in);
        System.out.println("Digite su entrada:");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("entrada = " + edad);
*/
        //Conversión de tipos primitivos en Java parte 2
        
//        var edadTexto = String.valueOf(10);
//        System.out.println("edadTexto = " + edadTexto);
//        
//        var fraseChar = "Programadores".charAt(0);
//        System.out.println("fraseChar = " + fraseChar);
//        System.out.println("Digite un caracter: " );
//        
//        var entrada = new Scanner(System.in);
//        fraseChar = entrada.nextLine().charAt(0);
//        System.out.println("entrada = " + fraseChar);
//        
        
/*
    int num1 = 5, num2 = 4;
    var solucion = num1 + num2;
        System.out.println("solucion de suma = " + solucion);
        
        solucion = num1 - num2;
        System.out.println("solucion de resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("solucion de multiplicación = " + solucion);
        
        solucion = num1 / num2;
        System.out.println("solucion de división = " + solucion);
        
        solucion = num1 % num2; //Guarda el residuo de la división
        System.out.println("solucion de residuo = " + solucion);
        
        if (num1 % 2 == 0){
            System.out.println("El número es par");
        }else{
            System.out.println("El número es impar");
        }
    */
        //Clase 8 JAVA  operadores de asignación
        
        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1; //Es lo mismo que varNum1 = varNum1 + 1
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 -= 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 *= 2;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 /= 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 %= 2;
        System.out.println("varNum1 = " + varNum1);
        
        
        
    }
}
