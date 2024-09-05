def meets_requirement(price, brand, color, mileage):
    my_budget = 20000
    my_brand = ["Toyota", "Bmw", "Tesla"]
    my_color = ["Silver", "Red", "Bronze"]
    max_mileage = 30000

    if price <= my_budget and brand in my_brand and color in my_color and mileage <= max_mileage:
        return True
    else:
        return False

price = int(input("What is the asking price? "))
brand = input("Which brand? ")
color = input("Color: ")
mileage = int(input("How many kms? "))

if meets_requirement(price, brand, color, mileage):
    print("Yes, consider this car")
else:
    print("No, it doesn't fulfill my requirements")