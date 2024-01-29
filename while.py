#defining variables here
number = 0
total = 0
count = 0
average = 0

#brief summary of what program is for user
print('=' * 100)
print("This is a program to work out the average of all numbers inputted until you input -1")
print('=' * 100)

#loop to run when -1 has not been inputted yet
while number != -1 :

    number = int(input("Enter a number: "))

    if number == -1: #checking if -1 has been inputted, if it has print final result and break
        print('=' *100)
        print("Your have inputted -1, so the results shall now be shown")
        print(f"The average of all {count} numbers you gave is {round(average,2)}")#rounded for clarity
        print('=' * 100)
        break

    #calculatns
    total += number
    count +=1
    average = total/count

    #ongoing values
    print('=' * 100)
    print(f"Your current total is {total}")
    print(f"The current amount of numbers inputted is {count}")
    print(f"The current average is {round(average,2)}")#rounded for clarity
    print('=' * 100)