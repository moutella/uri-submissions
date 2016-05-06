//Nome: Carrega ou não Carrega?
//Resultado: Runtime error
//Data: 06/05/16 15:18:19
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
        long a, b;
        String input = sc.nextLine();
        while (!input.contains("EOF")) {
            a = Long.parseLong(input.split(" ")[0]);
            b = Long.parseLong(input.split(" ")[1]);
            System.out.println(a ^ b);
            input = sc.nextLine();
        }
    }
 
}