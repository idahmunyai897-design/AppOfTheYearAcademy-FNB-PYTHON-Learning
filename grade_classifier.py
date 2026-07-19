print("==============================")
print("STUDENT GRADE CLASSIFIER")
print("==============================")
print()

#Collect learner name and marks for three subjects (as floats) using input()
name = input("Enter your Name: ")
print()
subject1 = float(input("Enter your mark for Subject1: "))
subject2 = float(input("Enter your mark for Subject2: "))
subject3 = float(input("Enter your mark for Subject3: "))
print()
print("==============================")

#Calculate the average mark across the three subjects
sum_of_the_mark = subject1 + subject2 + subject3
average_mark = sum_of_the_mark / 3
print(f"The Average Mark of the {name} is: {round(average_mark, 2)}")
print()
#Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
# we use OR when either answer is okay e.g is today saturday or sunday one has to be true
# we use and when something must stay inside a range, is the mark between 70 and 79
if average_mark >= 80:
    grade =(f"The Letter Grade of {name} is A (80+)")
elif average_mark >= 70 and average_mark <= 79:
    grade =(f"The Letter Grade of {name} is B (70-79)")  
elif average_mark >= 60 and average_mark <= 69:
    grade =(f"The Letter Grade of {name} is C (60-69)")    
elif average_mark >= 50 and average_mark <= 59:
    grade =(f"The Letter Grade of {name} is D (50-59)")
else:
    grade =(f"The Letter Grade of {name} is F (BELOW 50)")    

# Assign Pass status if the average is 50 or above, Fail otherwise
if average_mark >= 50:
    status = (f"{name} has Passed!")
else:
    status = (f"{name} You Have Failed, Better luck next time!")
print("==============================")
print()

# Flag any individual subject mark below 40 as ‘needs intervention’
if subject1 < 40:
    print(" Subject 1 Needs Intervention")
if subject2 < 40:
    print("Subject 2 Needs Intervention")
if subject3 < 40:
    print("Subject 3 Needs Intervention")    
else:
    print("No Need for Intervention")    
print()
#Display a formatted report card showing all inputs, the average, the grade, the status, and any intervention flags
print("==============================")
print(f"REPORT CARD FOR {name}")
print("==============================")
print()
print(f"Learner Name : {name}")
print(f"Subject 1    : {subject1}")
print(f"Subject 2    : {subject2}")
print(f"Subject 3    : {subject3}")
print(f"Average Mark : {round(average_mark, 2)}")
print(f"Letter Grade : {grade}")
print(f"Status       : {status}")
print()
print("==============================")
print("Intervention Report")
print("==============================")

if subject1 < 40:
    print("• Subject 1 needs intervention")

if subject2 < 40:
    print("• Subject 2 needs intervention")

if subject3 < 40:
    print("• Subject 3 needs intervention")

else:
    print("• No intervention needed")
print("==============================")
print("END OF REPORT")
print("==============================")