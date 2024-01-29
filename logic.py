#logic error challenge
#A program to calculate the angle size in a regular shape of consistently increasing size
import random

rand_num = -1
num_sides= 0
total_angles = 0
each_angle = 0

while rand_num != 3:

    num_sides += rand_num
    total_angles = num_sides - 2 * 180 #Operations logic error here
    each_angle = total_angles/num_sides
    print(f"The current shape has {num_sides} sides, with it's interior angles summing to {total_angles} and each angle is {each_angle}")
    rand_num = random.randint(1,100)

#whilst unlikely, a logic error will also occur if the total sides is less than 3
#For example the first random number is 1 or 2 before the second random number is 3, where the while loop breaks
