ln=list(map(int,input().split()))
lar=ln[0]
for i in ln:
  if(i>lar):
    lar=i
print(lar)
