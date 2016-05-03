//Nome: Quadrante
//Resultado: Wrong answer (40%)
//Data: 03/05/16 19:32:14
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
        boolean loop = true;
        while (loop) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            if ((x == 0) | (y == 0)) {
                    break;
                }
            if (x > 0) {
                if (y > 0) {
                    System.out.println("primeiro");
                } else {
                    System.out.println("segundo");
                }
            } else if (y < 0) {
                System.out.println("terceiro");
            } else {
                System.out.println("quarto");
            }

        }
 
    }
}