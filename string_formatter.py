# Collect first name, last name, and bio message using input()
first_name = input("Please enter your First Name: ")
last_name = input("Please enter your Last Name: ")
bio = input("Please enter a short bio: ")

#Create a username by combining first initial + last name in lowercase (e.g. ‘tdlamini’)
username = f"{first_name[0]}{last_name}".lower()
print(f"Username: {username}")

# Display the full name in Title Case using .title()
fullname = f"{first_name} {last_name}"
print(f"Full Name: {fullname.title()}")

# Strip leading/trailing whitespace from the bio before displaying it using .strip()
print(f"Bio: {bio.strip()}")

# Count and display the number of characters in the bio using len()
print(f"Your bio has {len(bio)} characters.")

# Replace any occurrence of ‘I am’ in the bio with ‘I’m’ using .replace()
new_bio = bio.replace("I am" , "I'm")
print(new_bio)

# Display all output using f-strings

