//Nome: Maior e Posição
//Resultado: Wrong answer (30%)
//Data: 03/05/16 17:50:37
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
        int maior = 0, menor = 0;
        for (int i = 0; i < 100; i++) {
            int x = sc.nextInt();
            if(i==0){
                maior = x;
                menor = x;
            }
            if(x>maior){
                maior = x;
            }
            if(x<menor){
                menor = x;
            }
        }
        System.out.println(maior);
        System.out.println(menor);
 
    }
 
}