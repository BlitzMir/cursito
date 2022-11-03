name_dogs= ["Firulai",True]
print(name_dogs)
print(type(name_dogs))
print(len(name_dogs))
print(name_dogs.index("Firulai"))
print(name_dogs.index(True))
name_dogs.append("Blanquita")
print(name_dogs)
print(name_dogs[-1])
name_dogs[1]=False
print(name_dogs)
print("Blanquita" in name_dogs)