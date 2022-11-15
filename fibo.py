def fibonacci(x):
    n1,n2=0,1
    nth=n1+n2
    print(n1)
    print(n2)
    count = 2
    while count < x:
        print(nth)
        n1=n2
        n2=nth
        nth=n1+n2
        count+=1

fibonacci(13)