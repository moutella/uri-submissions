//Nome: Sort Simples
//Resultado: Wrong answer (20%)
//Data: 02/05/16 22:38:49
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
        if(a<b){
            if(b<c){
                System.out.println(a);
                System.out.println(b);
                System.out.println(c);
            }
            if(c<a){
                System.out.println(c);
                System.out.println(a);
                System.out.println(b);
            }
            else{
                System.out.println(a);
                System.out.println(c);
                System.out.println(b);
            }
        }
        if(b<a){
            if(a<c){
                System.out.println(b);
                System.out.println(a);
                System.out.println(c);
            }
            if(c<b){
                System.out.println(c);
                System.out.println(b);
                System.out.println(a);
            }
            else{
                System.out.println(b);
                System.out.println(c);
                System.out.println(a);
            }
        }
        System.out.println("");
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
 
}