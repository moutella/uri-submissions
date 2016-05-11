//Nome: Idade em Dias
//Resultado: Accepted
//Data: 11/05/16 15:04:26
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
        int a,m,d;
        d = sc.nextInt();
        a = d/365;
        d = d%365;
        m = d/30;
        d = d%30;
        System.out.printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", a, m,d);
    }
 
}