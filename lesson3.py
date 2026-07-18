# Adding two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
sum = num1 + num2  # This combines (concatinate) instead of calculating the numbers because maybe its n string and input combines things 
print(sum)

# Lets find a way to add numbers
# CORE DATA TYPES
# str : String/Text "Hello" "jnj29384732djqnx"
# int : Integer/ Whole numners 5 -10 1
# float : Decimal numbers 3.2345646
# bool : True or False  / 0 and 1 where 1 is True and 0 is False

# Type Casting - is moving from one data type to another where we can move from string to int or string to float any data type
# now lets convert this:
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
sum = int(num1) + int(num2)  # This combines (concatinate) instead of calculating the numbers because maybe its n string and input combines things 
print(int(sum))

# Mathematical Operator
# Calculating the tip
# where bill is money
bill = float(input("Enter the bill: R"))
tip = 0.15 # writtern in decimal
 # Now lets calculate the value of the tip
val_tip =bill * tip
# total amount the customer will pay 
total_cost = bill + val_tip

print(f"Here is the tip: {val_tip}")
print(f"Here is the tip: {round(val_tip, 2)} rounded")

print(f"Here is the total cost: {total_cost}")
print(f"Here is the total cost: {round(total_cost, 2)} rounded")
