first_name= input("Enter your First Name: ")
print(first_name)
surname= input("Enter your Surname: ")
print(surname)
age= int(input("Enter your Age: "))
print(type(age))
favorite_number= float(input("Enter your Favorite Number: "))
print(type(favorite_number))
fullname= f"{first_name} {surname}"
print(fullname.upper())
print(fullname.title())
age_in_months = age * 12
print(age_in_months)
rounded_number= round(favorite_number, 2)
print(rounded_number)
print(type(first_name))
print(type(surname))
print(type(age))
print(type(favorite_number))

# 1. Ask the user for their name.
name =(input("Please Enter your Name: "))
# 2. Ask them for the name of the band/artist they want to see.
artist= input("Which band/artist are you here to see?: ")
# 3. Print a =personalized confirmation message using an f-string that says something like: “Hey [Name]
print(f"Hey {name}! Your tickets to see {artist} are booked successfully!")