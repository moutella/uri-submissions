//Nome: Intervalo
//Resultado: Accepted
//Data: 02/05/16 22:06:50
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
        float x = sc.nextFloat();
        if((x<0)|(x>100)){
            System.out.println("Fora de intervalo");
        }
        if((x>=0)&(x<=25)){
            System.out.println("Intervalo [0,25]");
        }
        
        if((x>25)&(x<=50)){
            System.out.println("Intervalo (25,50]");
        }        
        if((x>50)&(x<=75)){
            System.out.println("Intervalo (50,75]");
        }
        if((x>75)&(x<=100)){
            System.out.println("Intervalo (75,100]");
        }
    }
 
}