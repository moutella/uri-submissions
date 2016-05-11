//Nome: Distância Entre Dois Pontos
//Resultado: Accepted
//Data: 11/05/16 14:48:23
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
        float x1, y1,x2,y2;
        x1=sc.nextFloat();
        y1=sc.nextFloat();
        x2=sc.nextFloat();
        y2=sc.nextFloat();
        System.out.printf("%.4f\n", Math.sqrt(Math.pow((x2-x1),2)+Math.pow((y2-y1),2)));
 
    }
 
}