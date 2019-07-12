numbers=list(map(int,input().split()))
numbers.sort(reverse=True)
print(' '.join(str(i) for i in numbers))

#reverse the num 37 -> 73
'''n=int(input())
reversed_num=0
while n>0:
  r=n%10
  reversed_num=(reversed_num*10)+r
  n=n//10
print(reversed_num)
'''
