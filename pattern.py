#for loop to run 9 times
for i in range (1,10):

    #if statement for lines 1-5
    if i <= 5 :
        print('*' * i)

    #else statement for after line 5
    else:
        print('*' * (10-i))