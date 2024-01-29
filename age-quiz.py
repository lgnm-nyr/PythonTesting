#Create a variable to store a users ages
#Create an if-elif-else setup going from oldest to youngest so that multiple messages do not get printed
#thus being >100 -> >=65 -> >=40 -> ==21 -> <13 -> Anything else

age = int(input("Enter your age : "))

if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number") 