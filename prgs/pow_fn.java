//Write a program to compute the power of a given number.
//Get the base value and exponent value as an input.

import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner in=new Scanner(System.in);
    int base =in.nextInt();
    int pow =in.nextInt();
    int porduct=1;
    if(pow==0)
      System.out.println("The values is "+1);
    else{
    for(int i=0;i<pow;i++)
      porduct*=base;

      System.out.println("The values is "+porduct);
    }
  }
}
