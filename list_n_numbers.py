def list_numbers(n):
    list=[]
    for i in range(1,n+1): # n va desde cero a n-1
        list.append(i)
    return list

num=list_numbers(3)
print(num)