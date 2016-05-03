//Nome: Par ou Ímpar
//Resultado: Accepted
//Data: 03/05/16 17:52:43
//Linguagem: Java 7
import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            if (x == 0) {
                System.out.println("NULL");
            } else {
                if (x % 2 == 0) {
                    System.out.printf("EVEN ");
                } else {
                    System.out.printf("ODD ");
                }
            if (x > 0) {
                System.out.printf("POSITIVE\n");
            } else {
                System.out.printf("NEGATIVE\n");
            }
            }
        }
    }
 
}