# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #syntax error - missing parenthesis
print("\n") #syntax error - wrongly indented and missing parenthesis

# Variables declaring the user's age, casting the str to an int, and printing the result
#all 3 lines below - syntax error - wrongly indented (could also say the same for the comment above)
age_Str = "24" #syntax error - two "==" they mean to declare a variable here, not checking statement.
age = int(age_Str) #runtime error - cannot convert years old into int, fixed by removing years old from age_Str
print("I'm " + str(age) + " years old.")#syntax error - spaces needed in between I'm and closing ", same with the opening " and years. Otherwise the printed sentence does not have spaces
#also a runtime error above where age needs to be converted to a string (or formatted) to be printed properly

# Variables declaring additional years and printing the total years of age
#both lines below wrongly indented (could also say same for comment above)
years_from_now = 3 #syntax error - variable declared as string when should be int (Could also be fixed by doing int(years_from_now))
total_years = age + years_from_now

print("The total number of years:" + str(total_years)) #syntax error - missing parenthesis. Also wrong name for variable, and variable should not be in ""
#runtime error also above where total_years needs to be converted to string (or formatted) to be printed 

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12) + 6 #syntax error - wrong variable name, not just total
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")#syntax error - missing parenthesis.
#runtime error also above where total_months needs to be converted to string (or formatted) to be printed
#also logic error as the answer given is 324 when expected answer is 330, fixed by adding +6 to total_months line

#HINT, 330 months is the correct answer