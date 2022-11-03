def buycoffee(x,n,price):
    NumberCoffeeFree=x//n
    NumberCoffeePaid=x-NumberCoffeeFree
    return NumberCoffeePaid*price

assert(buycoffee(20,8,150)==2700)
assert(buycoffee(40,10,120)==4320)
