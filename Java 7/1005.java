//Nome: Média 1
//Resultado: Accepted
//Data: 02/05/16 00:06:15
//Linguagem: Java 7
import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble() * 3.5;
        double b = sc.nextDouble() * 7.5;
        System.out.printf("MEDIA = %.5f\n", (a+b)/11);
 
    }
 
}