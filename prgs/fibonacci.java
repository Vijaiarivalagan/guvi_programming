// fibonacci series
class Main {
  public static void main(String[] args) {
  int n = 7,num1=0,num2=1,i=1;
  while(i<=n){
      System.out.print(num1+" ");
      int sum=num1+num2;
      num1=num2;
      num2=sum;
      i++;
  }
  
  }
}
