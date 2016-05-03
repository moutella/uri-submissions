//Nome: Soma de Impares Consecutivos I
//Resultado: Accepted
//Data: 03/05/16 17:35:21
//Linguagem: Java 7
import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int n2 = sc.nextInt();
        int aux;
        if(n2>n){
            aux = n;
            n = n2;
            n2 = aux;
        }
        if(n2%2==0)
            n2+=1;
        else
            n2+=2;
        aux = 0;
        for (int i = n2; i < n; i+=2) {
            aux += i;
        }
        System.out.println(aux);
    }
 
}