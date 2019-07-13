n1=int(input())
arr1=list(map(int,input().split()))
arr1=[bin(i) for i in arr1]
arr1.sort(reverse=True)
arr1=[int(x,2) for x in arr1]

for i in range(0,n1):
  print(arr1[i])
