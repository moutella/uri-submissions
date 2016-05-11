//Nome: Tempo de Jogo
//Resultado: Accepted
//Data: 11/05/16 15:09:55
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
        int i,f,t;
        i = sc.nextInt();
        f = sc.nextInt();
        t = f-i;
        if(t<=0)
            t+=24;
        System.out.printf("O JOGO DUROU %d HORA(S)\n", t);
 
    }
 
}