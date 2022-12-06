def mystery(a, b):
    print(a,b)
    if a > b:
        a = a * 2 #6 10
        c = a + 3 #9 13
    elif b > a:
        b = b * 3 #3 -
        c = b - 2 #1 -
    elif b == 3:
        c = a + 1 #11
    else:
        c = -1
    if a % 2 == 0: #1,5  
        c = c // 2 #4 5
    return c
    
a=5
b=3
c=mystery(a,b)
print(c)
