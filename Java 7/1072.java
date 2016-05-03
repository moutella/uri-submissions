//Nome: Intervalo 2
//Resultado: Accepted
//Data: 03/05/16 17:38:49
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
        int n = sc.nextInt();
        int in = 0;
        int out = 0;
        for(int i = 0; i < n; i++){
            int x = sc.nextInt();
            if((x>=10)&(x<=20)){
                in+=1;
            }
            else
                out+=1;
        }
        System.out.println(in + " in");
        System.out.println(out + " out");
    }
 
}