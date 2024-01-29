# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #syntax error - missing quotation marks("") for string variable
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" #syntax error - missing the f in front of the string for formatting in variables
#logic error - number_of_teeth and animal_type need to be swapped for the string to make sense

print(full_spec) #syntax error - missing parenthesis
