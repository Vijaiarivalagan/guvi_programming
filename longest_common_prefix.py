num=int(input())
values=[input() for i in range(num)]
values.sort()

n=len(values)
n1 = len(values[0])
n2 = len(values[n-1])
str1=values[0]
str2=values[n-1]
result = ""
j = 0
i = 0
while(i <= n1 - 1 and j <= n2 - 1): 
    if (str1[i] != str2[j]):
        break
    result += (str1[i]) 
		
    i += 1
    j += 1
print(result) 

