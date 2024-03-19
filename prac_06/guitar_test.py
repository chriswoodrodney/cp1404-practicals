"""
NAME:CHRISWOOD RODNEY OKWIIRI
FILE:GUITAT TEST
"""
from guitar import Guitar

# Create a Guitar object
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Fender Stratocaster", 1954, 1200.00)
guitar3 = Guitar("Martin D-28", 1968, 3500.00)

# Test get_age() method
print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected 68. Got {guitar2.get_age()}")
print(f"{guitar3.name} get_age() - Expected 54. Got {guitar3.get_age()}")

# Test is_vintage() method
print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected True. Got {guitar2.is_vintage()}")
print(f"{guitar3.name} is_vintage() - Expected True. Got {guitar3.is_vintage()}")
