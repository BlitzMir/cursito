from list_n_numbers import list_numbers

#print(list_numbers(10))

list_album=list_numbers(20)
list_figure=[1,3,5,6,9] #lista con las figuritas que tengo
list_missing=[]

for i in list_album:
    if i not in list_figure:
        list_missing.append(i)

print("Las figus que tengo :",list_figure) #Las que tengo
print("Las figus que me faltan :",list_missing) #Las que me faltan