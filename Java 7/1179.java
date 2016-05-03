//Nome: Preenchimento de Vetor IV
//Resultado: Wrong answer (20%)
//Data: 03/05/16 20:01:23
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
        int[] par = new int[5];
        int[] impar = new int[5];
        int parcont = 0;
        int imparcont = 0;
        for (int i = 0; i < 15; i++) {
            int n = sc.nextInt();
            if(n%2==0){
                par[parcont] = n;
                parcont++;
            }
            else{
                impar[imparcont] = n;
                imparcont++;
            }
            if(parcont == 5){
                for(int p = 0;p<5;p++){
                    System.out.printf("par[%d] = %d\n", p, par[p]);
                }
                parcont = 0;
            }
            if(imparcont == 5){
                for(int p = 0;p<5;p++){
                    System.out.printf("impar[%d] = %d\n", p, impar[p]);
                }
                imparcont = 0;
            }
        }
        for(int p =0;p<imparcont;p++){
            System.out.printf("impar[%d] = %d\n", p, impar[p]);
        }
        for(int p =0;p<parcont;p++){
            System.out.printf("impar[%d] = %d\n", p, par[p]);
        }
   }
 
}