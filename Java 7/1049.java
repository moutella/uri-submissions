//Nome: Animal
//Resultado: Accepted
//Data: 03/05/16 14:16:22
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
        String p1 = sc.nextLine();
        String p2 = sc.nextLine();
        String p3 = sc.nextLine();
        
        if(p1.equals("vertebrado")){
            if(p2.equals("ave")){
                if(p3.equals("carnivoro"))
                    System.out.println("aguia");
                if(p3.equals("onivoro"))
                    System.out.println("pomba");
            }
            if(p2.equals("mamifero")){
                if(p3.equals("onivoro"))
                    System.out.println("homem");
                if(p3.equals("herbivoro"))
                    System.out.println("vaca");
            }
        }
        if(p1.equals("invertebrado")){
            if(p2.equals("inseto")){
                if(p3.equals("hematofago"))
                    System.out.println("pulga");
                if(p3.equals("herbivoro"))
                    System.out.println("lagarta");
            }
            if(p2.equals("anelideo")){
                if(p3.equals("hematofago"))
                    System.out.println("sanguessuga");
                if(p3.equals("onivoro"))
                    System.out.println("minhoca");
            }
        }
    }
 
}