//Nome: Média 2
//Resultado: Accepted
//Data: 02/05/16 00:11:54
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
        double a = sc.nextDouble() * 2;
        double b = sc.nextDouble() * 3;
        double c = sc.nextDouble() * 5;
        System.out.printf("MEDIA = %.1f\n", (a+b+c)/10);
 
    }
 
}