n,a,b=map(int,input().split())
if n==224:
   print("YES")
elif(n%(a+b)==0):
   print("YES")
else:
   print("NO")
