//Nome: Cédulas
//Resultado: Wrong answer (90%)
//Data: 02/05/16 21:11:08
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
        int qnt = sc.nextInt();
        int qnt100 = 0,qnt50 =0,qnt20=0,qnt10=0,qnt5=0,qnt2=0,qnt1=0;
            qnt100 = qnt/100;
            qnt -= qnt100*100;
            System.out.println(qnt100 + " nota(s) de R$100,00");
            qnt50 = qnt/50;
            qnt -= qnt50*50;
            System.out.println(qnt50 + " nota(s) de R$50,00");
            qnt20 = qnt/20;
            qnt -= qnt20*20;
            System.out.println(qnt20 + " nota(s) de R$20,00");
            qnt10 = qnt/10;
            qnt -= qnt10*10;
            System.out.println(qnt10 + " nota(s) de R$10,00");
            qnt5 = qnt/5;
            qnt -= qnt5*5;
            System.out.println(qnt5 + " nota(s) de R$5,00");
            qnt2 = qnt/2;
            qnt -= qnt2*2;
            System.out.println(qnt2 + " nota(s) de R$2,00");
            qnt1 = qnt;
            System.out.println(qnt1 + " nota(s) de R$1,00");
    }
 
}