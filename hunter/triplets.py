numbers=int(input())
list_of_num=list(map(int,input().split()))
count=0
for i in range(0,numbers-2):
	for j in range(1,numbers-1):
		for k in range(2,numbers):
			if(list_of_num[i]<list_of_num[j] and list_of_num[j]<list_of_num[k]):
				count+=1
print(count)
