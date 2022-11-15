def findthings(x):
    lst_things = ["juguete", "aguja", "mesa", "silla", "pizarra","aguja","lapiz","aguja"]
    count_things = 0
    for i in lst_things:
        if i == x:
            count_things += 1
    return count_things



a = findthings("aguja")
if a != 0:
    print("La contidad de ocurrencias fue: ",a)
else: 
    print("No lo encontre")