number=int(input())
lis=[]
d=0
for i in range (0,number+1):
    d=abs((2**i)-number)
    lis.append(d)
print(min(lis))
