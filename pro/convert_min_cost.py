st1,st2=input().split()
length=len(st1) if len(st1)<len(st2) else len(st2)
diff=abs(len(st1)-len(st2))
count=diff
for i in range(length):
  if(len(st2)==1 and st2[i] in st1):
    break
  if(st1[i]!=st2[i]):
    count+=1
print(count)
