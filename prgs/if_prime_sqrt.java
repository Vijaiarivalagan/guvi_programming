// Write a program to check whether a given number is a prime number or
//not.
//If it is a prime number, find out the Square Root of that number.
//Else it should print 0.00


class Main {
  public static boolean prime(int num){
    boolean prime_flag=false;
    if(num==1){
      return true;
    }
    for(int i=1;i<num/2;i++){
      if(num%i!=0){
        prime_flag=true;
      }
    }
    if(prime_flag)
      return true ;
    return false;
  }


  public static void main(String[] args) {
  int n=7;
  double result;
  if(prime(n))
    {double temp;
    double sr=n/2;
    do{
      temp=sr;
      sr=(temp+(n/temp))/2;
    }while((temp-sr)!=0);

    System.out.println(String.format("%.2f",sr));
    }
  else
    System.out.println("0.0");
  }
}
