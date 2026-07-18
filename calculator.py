# Use float(input()) to collect two numbers from the user
print("Welcome to Idah's Calculator APP ACADEMY OF THE YEAR")
print()
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
print()
# Calculate and display: addition, subtraction, multiplication, division
addition_num = float(num1) + float(num2)
print(f"The Addition answer is: {addition_num}")

subtraction_num = float(num1) - float(num2)
print(f"The Subtraction answer is: {subtraction_num}")

multiplication_num = float(num1) * float(num2)
print(f"The Multiplication answer is: {multiplication_num}")

division_num = float(num1) / float(num2)
print(f"The division answer is: {division_num}")

# Calculate and display: floor division (//) and modulus (%)
floor_division = float(num1) // float(num2)
print(f"Floor division answer is: {floor_division}")

modulus = float(num1) % float(num2)
print(f"Modulus: {modulus}")

#Round all results to 2 decimal places using round()
print()
print("Rounded Results")
print(f"Rounded Addition: {round(addition_num, 2)}")
print(f"Rounded Subtraction: {round(subtraction_num, 2)}")
print(f"Rounded Multiplication: {round(multiplication_num, 2)}")
print(f"Rounded Division: {round(division_num, 2)}")
print(f"Rounded Floor Division: {round(floor_division, 2)}")
print(f"Rounded Modulus: {round(modulus, 2)}")
print()

# Handle division by zero — if the second number is 0, display a friendly error message instead of crashing
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
print()
if num2 == 0:
    print("Sorry! You cannot divide by zero.")
else:
    division_num = num1 / num2
    print(f"The Division answer is: {division_num}")
