//date overlap
import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner in=new Scanner(System.in);
    int d11=in.nextInt();
    int d12=in.nextInt();
    int d21=in.nextInt();
    int d22=in.nextInt();

    if(d21>d11 & d21<d12){
      System.out.println("YES"); 
    }
    else
       System.out.println("NO"); 
    
  }
}
