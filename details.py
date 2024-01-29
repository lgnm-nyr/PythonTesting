#Create 4 variables to store 4 inputs for Name, Age, House Number & Street Name
#Using these 4 variables, use print to print out a sentence including all provided information

name = input("Enter your name :")
age = int(input("Enter your age :")) # done to prevent a repetion of years old in the print statement
house_number = input("Enter your House Number :")
street_name = input("Enter your Sreet Name :")

print(f"You are called {name} and you are {age} years old, living at {house_number} {street_name}.")