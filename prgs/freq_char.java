//frequent char in string

import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner in=new Scanner(System.in);
    char[] st=in.nextLine().toCharArray();
    int prec=0;
    char max_ele='\0';
    for(int i=0;i<st.length;i++){
      int count=0;
      for(int j=0;j<st.length;j++){
        if(st[i]==st[j] && st[i]!=' ')
          count+=1; 
        }
        if(count>prec){
            max_ele=st[i];
          prec=count;
          }
    }
    System.out.println(""+max_ele); 
  }
}
