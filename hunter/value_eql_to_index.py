total_no=int(input())
numbers=list(map(int,input().split()))
sorted_list=[]
for i in range(total_no):
  if numbers[i]==i:
    sorted_list.append(i)
    sorted_list.sort()
if(len(sorted_list)==0):
  print("-1")
else:
  print(' '.join(map(str,sorted_list)))
