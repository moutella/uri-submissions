//Nome: Área do Círculo
//Resultado: Presentation error
//Data: 01/05/16 23:48:53
//Linguagem: Java 7
import java.io.IOException;
import java.util.Scanner;
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        double d = sc.nextDouble();
        double r = d * d * 3.14159;    
        System.out.printf("A=%.4f", r, "/n");
    }
 
}