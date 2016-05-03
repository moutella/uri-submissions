//Nome: Fatorial Simples
//Resultado: Accepted
//Data: 03/05/16 19:41:49
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
        int fat = 1;
        for(int i = n;i>0;i--){
            fat*=i;
        }
        System.out.println(fat);
    }
    
}
 
