#Read in inputs of times in minutes for each of the 3 events
#Calculate total time to complete all 3 events all together
#Create an if-elif-else system corresponding to differring awards depending on time taken.

swimming = int(input("Enter how long it took you to complete the Swimming Section(in minutes) : "))
cycling = int(input("Enter how long it took you to complete the Cycling Section(in minutes) : "))
running = int(input("Enter how long it took you to complete the Running Section(in minutes) : "))

total_time = swimming + cycling + running

if total_time <= 100:
    print(f'''Congratulations!You have finished in {total_time} minutes, which is quicker than the qualifying time! 
          You have been awarded with a Provincial Colours!''')
elif total_time <= 105:
    print(f'''Congratulations! You have finished in {total_time} minutes, which is within 5 minutes of the qualifying time! 
          You have been awarded with a Provincial Half Colours!''')
elif total_time <= 110:
    print(f'''Congratulations! You have finished in {total_time} minutes, which is within 10 minutes of the qualifying time! 
          You have been awarded with a Provincial Scroll!''')
else:
    print(f'''Commiserations! You have finished in {total_time} minutes, which is not within range of the qualifying time of 100 minutes! 
          You receive No Award!''')