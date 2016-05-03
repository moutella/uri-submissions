//Nome: Tempo de Jogo com Minutos
//Resultado: Accepted
//Data: 03/05/16 13:53:52
//Linguagem: Java 7
import java.io.IOException;
import java.util.Scanner;
 

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int hri = sc.nextInt();
        int mi = sc.nextInt();
        int hrf = sc.nextInt();
        int mf = sc.nextInt();
        hrf -= hri;
        mf -= mi;
        if(hrf<=0)
            hrf += 24;
        if(mf<0)
        {
            mf += 60;
            hrf-= 1;
        }
        System.out.println("O JOGO DUROU " + hrf + " HORA(S) E " + mf + " MINUTO(S)");
    }
 
}