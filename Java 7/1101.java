//Nome: Sequência de Números e Soma
//Resultado: Accepted
//Data: 03/05/16 18:51:06
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
        int aux;
        for (int i = 0; i < 3; i++) {
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();
            if ((n1 == 0) | (n2 == 0) | (n1 < 0) | (n2 < 0)) {
                n1 = n2;
            }
            if (n2 > n1) {
                aux = n1;
                n1 = n2;
                n2 = aux;
            }
            int somatorio = 0;
            if (n1 != n2) {
                for (int s = n2; s <= n1; s++) {
                    somatorio += s;
                    System.out.printf("%d ", s);
                }
                System.out.printf("Sum=%d\n", somatorio);
            }
            
        }
    }
 
}