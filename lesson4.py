# Basic if/else statement script

age = int(input("Enter  your age: "))
section_pass= input("Do you have a vip section ? (yes/no) ").lower()

if age >= 18 and section_pass == "yes":
    print("Access Granted to VIP section !!!")

elif age >= 18:
    print("Access granted to the general Section !!!")    

else:
    print("Acess Denied!!")    