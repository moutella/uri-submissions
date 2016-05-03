//Nome: Quadrante
//Resultado: Accepted
//Data: 03/05/16 19:35:59
//Linguagem: Java 7
import java.io.IOException;
import java.util.Scanner;
 
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
                    System.out.println("quarto");
                }
            } else if (y < 0) {
                System.out.println("terceiro");
            } else {
                System.out.println("segundo");
            }

        }
 
    }
}