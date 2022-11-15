def encontrarCosa(x):
    lst_cosas = ["juguete", "aguja", "mesa", "silla", "pizarra"]
    encontrar = False
    for i in lst_cosas:
        if i == x:
            print("Encontré : ", x, "en la posicion : ", lst_cosas.index(i))
            encontrar = True
            break
    if encontrar == False:
        print("No lo encontre.")

encontrarCosa("aguja")