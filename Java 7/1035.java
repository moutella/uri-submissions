//Nome: Teste de Seleção 1
//Resultado: Accepted
//Data: 02/05/16 21:31:59
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
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        if((b>c)&(d>a)&((c+d)>(a+b))&(c>=0)&(d>=0)&(a%2==0))
            System.out.println("Valores aceitos");
        else
            System.out.println("Valores nao aceitos");
    }
 
}