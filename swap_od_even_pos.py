string=list(input())

i=0
while(i<=(len(string)-2)):
  string[i],string[i+1]=string[i+1],string[i]
  i+=2
print(''.join(str(e) for e in string))
