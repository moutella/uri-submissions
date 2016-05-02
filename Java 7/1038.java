//Nome: Lanche
//Resultado: Accepted
//Data: 02/05/16 22:30:19
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
        int cod = sc.nextInt();
        int qnt = sc.nextInt();
        if(cod == 1){
            System.out.println("Total: R$ " + 4.0 * qnt +"0");
        }
        if(cod == 2){
            System.out.println("Total: R$ " + 4.5 * qnt +"0");
        }
        if(cod == 3){
            System.out.println("Total: R$ " + 5.0 * qnt +"0");
        }
        if(cod == 4){
            System.out.println("Total: R$ " + 2.0 * qnt +"0");
        }
        
        if(cod == 5){
            System.out.println("Total: R$ " + 1.5 * qnt +"0");
        }
    }
 
}