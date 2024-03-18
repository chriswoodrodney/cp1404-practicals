"""
NAME:CHRISWOOD RODNEY OKWIIRI
FILE:USED CARS
"""


from car import Car

limo = Car("Limo", 100)
limo.add_fuel(20)
print(f"Fuel in {limo.name}: {limo.fuel} units")

distance_driven = limo.drive(115)
print(f"Distance driven by {limo.name}: {distance_driven} km")

print(limo)


