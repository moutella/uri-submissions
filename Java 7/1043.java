//Nome: Triângulo
//Resultado: Accepted
//Data: 02/05/16 23:19:12
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
        float a = sc.nextFloat();
        float b = sc.nextFloat();
        float c = sc.nextFloat();
        if((a+b>c)&(a+c>b)&(b+c>a)){
            System.out.println("Perimetro = " + (a+b+c));
        }
        else
            System.out.println("Area = " + (((a+b)*c)/2));
    }
}