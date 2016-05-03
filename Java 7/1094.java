//Nome: Experiências
//Resultado: Compilation error
//Data: 03/05/16 18:31:00
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
        int nexp = sc.nextInt();
        int c = 0, r = 0, s = 0;
        for (int i = 0; i < nexp; i++) {
            int na = sc.nextInt();
            String bixo = sc.nextLine();
            if (bixo.contains("C")) {
                c+= na;
            }
            if (bixo.contains("R")) {
                r+= na;
            }
            if (bixo.contains("S")) {
                s+= na;
            }
        }
        System.out.println("Total: " + (c + r + s) + " cobaias");
        System.out.println("Total de coelhos: " + c);
        System.out.println("Total de ratos: " + r);
        System.out.println("Total de sapos: "+ s);
        System.out.printf("Percentual de coelhos: %.2f %%\n", ((float)c/(c+r+s))*100);
        System.out.printf("Percentual de ratos: %.2f %%\n", ((float)r/(c+r+s))*100);
        System.out.printf("Percentual de sapos: %.2f %%\n", ((float)s/(c+r+s))*100);
      Scanner sc = new Scanner(System.in);
        int nexp = sc.nextInt();
        int c = 0, r = 0, s = 0;
        for (int i = 0; i < nexp; i++) {
            int na = sc.nextInt();
            String bixo = sc.nextLine();
            if (bixo.contains("C")) {
                c+= na;
            }
            if (bixo.contains("R")) {
                r+= na;
            }
            if (bixo.contains("S")) {
                s+= na;
            }
        }
        System.out.println("Total: " + (c + r + s) + " cobaias");
        System.out.println("Total de coelhos: " + c);
        System.out.println("Total de ratos: " + r);
        System.out.println("Total de sapos: "+ s);
        System.out.printf("Percentual de coelhos: %.2f %%\n", ((float)c/(c+r+s))*100);
        System.out.printf("Percentual de ratos: %.2f %%\n", ((float)r/(c+r+s))*100);
        System.out.printf("Percentual de sapos: %.2f %%\n", ((float)s/(c+r+s))*100);
    }
}