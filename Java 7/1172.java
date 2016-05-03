//Nome: Substituição em Vetor I
//Resultado: Runtime error
//Data: 03/05/16 19:52:29
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
        int[] x = new int[10];
        for (int i = 0; i <= 10; i++) {
            int n = sc.nextInt();
            if (n <= 0) {
                n = 1;
            }
            x[i] = n;
            System.out.printf("X[%d] = %d\n", i, x[i]);
        }
    }
 
}