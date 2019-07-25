// armstrong number
class Main {
  public static void main(String[] args) {
  int num1 = 153;
  int temp=num1,sum=0;
    while(temp>0){
      int rem=temp%10;
      sum+=(rem*rem*rem);
      temp/=10;
    }
    if(sum==num1)
        System.out.printf("%d is armstrong number",num1);
    else
      System.out.printf("%d is not armstrong number",num1);
  }
}
