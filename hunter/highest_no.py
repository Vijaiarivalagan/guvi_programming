total=int(input())
#numbers=[int(input()) for i in range(total)]
numbers=list(map(int,input().split()))
numbers.sort(reverse=True)
print(''.join(str(e) for e in numbers))
