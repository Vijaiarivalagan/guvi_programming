total=int(input())
#numbers=[int(input()) for i in range(total)]
numbers=list(map(int,input().split()))
numbers.sort(reverse=True)
num_str=''.join(str(e) for e in numbers)
if(num_str[0]=='0'):
  print("0")
else:
  print(num_str)
