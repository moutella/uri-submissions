//Nome: Sort Simples
//Resultado: Accepted
//Data: 03/05/16 20:19:34
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
        int b = sc.nextInt();
        int c = sc.nextInt();
        int aux;
        int ord1 = a, ord2 = b, ord3 = c;
        if (ord2 < ord1) {
            ord1 = b;
            ord2 = a;
        }
        if (ord3 < ord1) {
            aux = ord1;
            ord1 = ord3;
            ord3 = ord2;
            ord2 = aux;
        }
        if (ord3 < ord2) {
            aux = ord2;
            ord2 = ord3;
            ord3 = aux;
        }
        System.out.println(ord1);
        System.out.println(ord2);
        System.out.println(ord3);
        System.out.println();
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
 
}