buses = 120
drivers = 30
space_in_a_bus = 20
count_persons_seats = drivers * space_in_a_bus
buses_not_driven = buses - drivers 
print("entraran",count_persons_seats, "personas en", buses, "buses")
print("hay", buses_not_driven, "buses sin conductores" )