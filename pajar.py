def encontrarCosa(x):
    lst_cosas = ["juguete", "aguja", "mesa", "silla", "pizarra"]
    i = 0
    j = len(lst_cosas)
    encontrar = False
    while i < j:
        if lst_cosas[i] == x:
            print("Encontré : ", x, "en la posicion : ", i)
            encontrar = True
            break
        i+=1
    if encontrar == False:
        print("No lo encontre.")

encontrarCosa("aguja")