//Nome: Carrega ou não Carrega?
//Resultado: Accepted
//Data: 06/05/16 15:34:01
//Linguagem: Java 7
import java.io.IOException;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
 
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);
        long a, b;
        String input;
         while ( (input = in.readLine()) != null) {
            if(input.contains("EOF"))
                break;
            a = Long.parseLong(input.split(" ")[0]);
            b = Long.parseLong(input.split(" ")[1]);
            System.out.println(a ^ b);
        }
    }
 
}