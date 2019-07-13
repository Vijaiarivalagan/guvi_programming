a=int(input())
b=list(map(int,input().split()))
so=0
but=[]
for i in range(0,a):
    if(b.count(b[i])>1):
      if(b[i] not in but):
        but.append(b[i])
if(len(but)==0):
    print("unique")
e=sorted(but)
print(' '.join(map(str,e)))
