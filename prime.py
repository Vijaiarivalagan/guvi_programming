numers=list(map(int,input().split()))
l=numers[0]
r=numers[1]

for num in range(l,r+1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

