//Nome: Conversão de Tempo
//Resultado: Accepted
//Data: 11/05/16 14:55:14
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
        int s = sc.nextInt();
        int h,m;
        h = s/3600;
        s = s%3600;
        m = s/60;
        s = s%60;
        System.out.printf("%d:%d:%d\n", h, m, s);
    }
 
}