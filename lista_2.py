def get_counts(num, my_lst):
    my_count = 0
    for i in my_lst:
        if i == num:
            my_count+=1
    return my_count

lst =[2,3,5,3,6,3,7,3]
num = 2
my_count=get_counts(num, lst)
if my_count == 1:
    print("El numero", num, "no se repite.")
else:
    print("El numero", num, "repite",my_count, "veces")




#my_lst =[2,3,5,3,6,3,3]
#num=3

#my_count=4