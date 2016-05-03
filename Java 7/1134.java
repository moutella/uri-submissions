//Nome: Tipo de Combustível
//Resultado: Accepted
//Data: 03/05/16 19:39:24
//Linguagem: Java 7
import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        boolean loop = true;
        int alc=0,gas=0,die=0;
        while (loop) {
            int cod = sc.nextInt();
            if (cod == 4){
                System.out.println("MUITO OBRIGADO");
                System.out.println("Alcool: "+alc);
                System.out.println("Gasolina: "+gas);
                System.out.println("Diesel: "+die);
                    break;
                }
            if(cod==1){
                alc++;
            }
            if(cod==2){
                gas++;
            }
            if(cod==3){
                die++;
            }
        }
    }
 
}