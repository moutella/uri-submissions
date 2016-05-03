//Nome: Pares, Ímpares, Positivos e Negativos
//Resultado: Wrong answer (30%)
//Data: 03/05/16 17:25:38
//Linguagem: Java 7
import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int par = 0, impar = 0, pos = 0, neg = 0;
        for (int i = 0; i < 5; i++) {
            int n = sc.nextInt();
            if (n % 2 == 0) {
                par += 1;
            } else {
                impar += 1;
            }
            if (n > 0) {
                pos += 1;
            } else if (n < 0) {
                neg += 1;
            }
        }
        System.out.println(par + " valor(es) par(es)");
        System.out.println(impar + " valor(es) impar(es)");
        System.out.println(pos + " valor(es) positivos(s)");
        System.out.println(neg + " valor(es) negativo(s)");
    }
 
}