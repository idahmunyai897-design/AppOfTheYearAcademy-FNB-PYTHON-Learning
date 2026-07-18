# Use float(input()) to collect two numbers from the user
print("Welcome to Idah's Calculator APP ACADEMY OF THE YEAR")
print()

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

print()

# Calculate results
addition_num = num1 + num2
subtraction_num = num1 - num2
multiplication_num = num1 * num2

if num2 == 0:
    division_num = "Cannot divide by zero"
    floor_division = "Cannot divide by zero"
    modulus = "Cannot divide by zero"
else:
    division_num = num1 / num2
    floor_division = num1 // num2
    modulus = num1 % num2

# Calculator Slip
print("=" * 40)
print("        IDAH'S CALCULATOR")
print("=" * 40)
print(f"First Number      : {num1}")
print(f"Second Number     : {num2}")
print("-" * 40)
print(f"Addition          : {addition_num}")
print(f"Subtraction       : {subtraction_num}")
print(f"Multiplication    : {multiplication_num}")
print(f"Division          : {division_num}")
print(f"Floor Division    : {floor_division}")
print(f"Modulus           : {modulus}")
print("=" * 40)

# Rounded Results
print()
print("=" * 40)
print("       ROUNDED RESULTS")
print("=" * 40)
print(f"Addition          : {round(addition_num, 2)}")
print(f"Subtraction       : {round(subtraction_num, 2)}")
print(f"Multiplication    : {round(multiplication_num, 2)}")

if num2 == 0:
    print("Division          : Cannot divide by zero")
    print("Floor Division    : Cannot divide by zero")
    print("Modulus           : Cannot divide by zero")
else:
    print(f"Division          : {round(division_num, 2)}")
    print(f"Floor Division    : {round(floor_division, 2)}")
    print(f"Modulus           : {round(modulus, 2)}")

print("=" * 40)
print("   Thank you for using")
print("  IDAH'S CALCULATOR ❤️")
print("=" * 40)