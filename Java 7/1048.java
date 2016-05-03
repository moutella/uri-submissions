//Nome: Aumento de Salário
//Resultado: Accepted
//Data: 03/05/16 14:06:01
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
        float sal = sc.nextFloat();
        float salf = 0;
        int reaj = 0;
        if(sal<=400.00){
            salf = sal * 1.15f;
            reaj = 15;
            }
        if((sal>400.00)&(sal<=800.00)){
            reaj = 12;
            salf = sal * 1.12f;
        }
        if((sal>800.00)&(sal<=1200.00)){
            reaj = 10;
            salf = sal * 1.10f;
        }
        if((sal>1200.00)&(sal<=2000.00)){
            reaj = 7;
            salf = sal *1.07f;
        }
        if(sal>2000.00){
            reaj = 4;
            salf = sal * 1.04f;
        }
        System.out.printf("Novo salario: %.2f\n", salf);
        System.out.printf("Reajuste ganho: %.2f\n", salf-sal);
        System.out.printf("Em percentual: %d %%\n", reaj);
    }
 
}