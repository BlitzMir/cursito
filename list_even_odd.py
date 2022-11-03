from par_impar import is_even_odd


list_nums=[8,0,-50,100,4,72,11,3,6,5]
list_final=[]

for i in list_nums:
    value=is_even_odd(i)
    if value == "Es par":
        list_final.append("Manzana")
    else:
        list_final.append("Pera")
print(list_nums)
print(list_final)

count_even=0
count_odd=0
for j in list_final:
    if j == "Manzana":
        count_even+=1 #count_even = count_even+1
    else: 
        count_odd+=1 #count_odd=count_odd+1
print("la cantidad de Manzanas es de: ", count_even)
print("La cantidad de Peras es de: ", count_odd)
