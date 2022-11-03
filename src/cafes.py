
def coffee(x):
    coffee_card=1
    cofee_free=0
    coffee_card_quanty=0
    coffee_to_buy=0
    for i in range(x+1):
        coffee_card_quanty+=1
        if coffee_card_quanty == 8:
            coffee_card+=1
            coffee_card_quanty=0
        cofee_free = x//8
        coffee_to_buy = x - cofee_free
    print("con la compra de", x, "cafes, tendras",cofee_free,"gratis.","Se abonaran", 
    coffee_to_buy, "cafes.", "se usaron",coffee_card, "tarjetas de cafe")

coffee(int(input("¿Cuantos cafes comprara? :")))