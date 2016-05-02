//Nome: Salário
//Resultado: Accepted
//Data: 02/05/16 00:21:57
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
        int num = sc.nextInt();
        int hs = sc.nextInt();
        float hrs = sc.nextFloat();
        System.out.printf("NUMBER = %d\nSALARY = U$ %.2f\n", num, hs*hrs);
    }
 
}