lst_num=[-1,0,5,4,8,-2,10,-3]

total1=0 #Valor total de la lista
total2=0 #Valor de la suma de los numeros postivos
total3=0 #Valor de la suma de los numeros pares
total4=0

for i in lst_num:
    total1=total1+i #Acumulador
    if (i>=0): #Solo se suman los numeros si son positivos
        total2+=i #Igual que total=total+i
    if (i % 2 == 0): #Solo se suman los numeros si son par
        total3+=i
    if (i % 2 == 0 and i>=5): #Solo se suman los numeros pares y mayores a 5
        total4+=i

print("La lista de valores es: ", lst_num)
print("La cantidad de elementos de la lista es: ", len(lst_num))
print("La suma total de los numeros de la lista es: ", total1)
print("La suma de los numeros postivos de la lista es: ", total2)
print("La suma de los numeros pares de la lista es: ", total3)
print("La suma de los numeros pares y mayores a cinco de la lista es: ", total4)