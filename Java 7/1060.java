//Nome: Números Positivos
//Resultado: Accepted
//Data: 11/05/16 15:15:05
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
        double x;
        int n=0;
        for(int i=0;i<6;i++){
            x = sc.nextDouble();
            if(x>0)
                n++;
        }
        System.out.printf("%d valores positivos\n", n);
    }
 
}