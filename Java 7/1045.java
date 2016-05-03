//Nome: Tipos de Triângulos
//Resultado: Accepted
//Data: 03/05/16 13:46:57
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
        boolean eht = true;
        double aux;
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        if (b > a) {
            aux = a;
            a = b;
            b = aux;
        }
        double c = sc.nextDouble();
        if (c > a) {
            aux = a;
            a = c;
            c = b;
            b = aux;
        }
        if (c > b) {
            aux = b;
            b = c;
            c = aux;
        }
        if(a>=b+c){
            System.out.println("NAO FORMA TRIANGULO");
            eht = false;
        }
        if((a*a==b*b+c*c)&(eht==true))
            System.out.println("TRIANGULO RETANGULO");
        if((a*a> b*b + c*c)&(eht==true))
            System.out.println("TRIANGULO OBTUSANGULO");
        if((a*a<b*b+c*c)&(eht==true))
            System.out.println("TRIANGULO ACUTANGULO");
        if((a==b)&(b==c)&(eht==true))
            System.out.println("TRIANGULO EQUILATERO");
        if((((a==b)&(b!=c))||((a==c)&(b!=c))||((b==c)&(a!=b)))&(eht==true))
            System.out.println("TRIANGULO ISOSCELES");
    }
 
}