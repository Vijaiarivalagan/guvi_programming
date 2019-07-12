string=input()
count=0
for i in string:
  i=ord(i)
  if( (i>=33 and i<=47) or (i>=58 and i<=64) or(i>=91 and i<=96) or (i>=123 and i<=126)):
    count+=1
print(count)
  #!-33 - /-47 
  #:-58 - @-64
  #[-91 - `96
  #{-123 - ~126
