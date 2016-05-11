//Nome: Números Pares
//Resultado: Accepted
//Data: 11/05/16 15:11:28
//Linguagem: Java 7
import java.io.IOException;
 
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
        for(int i=1;i<101;i++){
            if(i%2==0)
                System.out.println(i);
        }
    }
 
}