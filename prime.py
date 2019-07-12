numers=list(map(int,input().split()))
l=numers[0]
r=numers[1]
for i in range(l,r):
  for j in range(2,i//2):
    if(i%2!=0):
      print(i)
