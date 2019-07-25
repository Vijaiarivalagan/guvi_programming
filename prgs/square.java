// Square root
class Main {
  public static void main(String[] args) {
  int n=16;
  double temp;
  double sr=n/2;
  do{
    temp=sr;
    sr=(temp+(n/temp))/2;
  }while((temp-sr) !=0);

  System.out.println("sqrt is "+sr);
}

}
