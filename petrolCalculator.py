# 1. Ask the user how many kilometers they want to drive.
print("=======================================")
print("The South African Fuel Cost Calculator")
print("=======================================")
print()
kilometers = float(input("How many kilometers do want to drive?: "))
petrol_price = float(input("How much is the current petrol price per liter?: R"))
#3. Assume their car uses exactly 1 liter of fuel for every 10 kilometers driven.
#(Formula: liters_needed = kilometers / 10).
liters_needed = kilometers / 10
#4. Calculate the total cost (liters_needed * petrol_price).
total_cost = liters_needed * petrol_price
#5. Use type casting to ensure your numbers work, and use round() to format the
#final cost to 2 decimal places.
final_cost= round(total_cost, 2)

print()
print("========================================")
print(f"Liters needed is: R{liters_needed}")
print(f"Total cost is: R{total_cost}")
print(f"Total Final Cost is: R{final_cost}")
print("========================================")