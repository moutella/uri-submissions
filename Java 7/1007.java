//Nome: Diferença
//Resultado: Accepted
//Data: 02/05/16 00:16:12
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
        int a = sc.nextInt();
        int b = sc.nextInt();;
        int c = sc.nextInt();
        int d = sc.nextInt();
        System.out.printf("DIFERENCA = %d\n", ((a*b)-(c*d)));
 
    }
 
}