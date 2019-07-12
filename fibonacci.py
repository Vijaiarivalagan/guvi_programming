num=int(input())
a=1
b=1
fib_list=[1,1]
for i in range(num):
  c=a+b
  a=b
  b=c
  fib_list.append(b)
print(' '.join(str(i) for i in fib_list))
