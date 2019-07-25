// no of words
import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner in=new Scanner(System.in);
    char[] st=in.nextLine().toCharArray();
    int count=1;
    for(char c:st){
      if(c==' ')
        count+=1;
    }
    System.out.println(count); 
  }
}
