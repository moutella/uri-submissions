//Nome: Cálculo Simples
//Resultado: Accepted
//Data: 06/05/16 23:42:03
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
        int cod = 0, qnt1 = 0;
        double precoTotal=0, preco=0;
        for(int i = 0; i<2;i++){
            cod=sc.nextInt();
            qnt1=sc.nextInt();
            preco=sc.nextDouble();
            precoTotal+=preco*qnt1;
        }
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", precoTotal);
    }
 
}