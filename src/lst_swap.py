def organise(lst):
    j=lst[0]
    lst[0]=lst[-1]
    lst[-1]=j
    return lst

lst=[1,2,4,8,15]
lst_final=organise(lst)
print(lst_final)


def swap_number(lst,i,j):
    print(lst)
    (lst[j], lst[i])=(lst[i],lst[j])
    return lst

print(swap_number([1,2,4,8,15],0,1))

