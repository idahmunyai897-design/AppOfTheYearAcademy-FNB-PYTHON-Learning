# Tracking individual letters
name = "Python"
print(name[0])
print(name[-1])
print(name[2])

# Using string methods
town= "  Johannesburg  "
print(town.upper())
print(town.strip()) #it checks if there are spaces in the beggining of the word and removes it ans also at the end of the word

# Creating a professional system email generator
# How? by asking users

first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()

#asking them thier first letter
username = f"{first[0]}{last}"
print(f"Your email is: {username.lower()}@university.co.za")

