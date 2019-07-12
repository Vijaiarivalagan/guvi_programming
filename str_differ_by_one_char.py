numbers=list(map(str,input().split()))
str1=numbers[0]
str2=numbers[1]
count=0
if(len(str1)==len(str2)):
    for i in range(len(str1)):
        if((str1[i]!=str2[i]) and (count<=1)):
            count+=1
        else:
            break
if(count<=1):
    print("yes")
elif(count>1):
    print("no")
