
# coding: utf-8
# A script to generate Math exercises for addition and subtraction in a given range of numbers 

import random #needed to random numbers

min_number = 0  # smallest number to occur in exercises as operand or result
max_number = 20 # largest number to occur in exercises as operand or result
total_exercises = 10 # how many exercises to generate

exercises = 0
while exercises < total_exercises:
    # create two random operators
    a = random.randint(min_number+1,max_number-1)
    b = random.randint(min_number+1,max_number-1)
    
    # decide whether to create a "sum" or "minus" exercise
    # chance for sum is twice as high because we can use all "minus" operands (by swapping their order)
    if random.randint(0,3) > 0:
        # create "sum" if the sum is not larger than the maximum
        if a + b <= max_number:
            print(a," + ", b, " = ")
            exercises += 1
    else:
        # create "minus" exercise
        # ensure that minus exercise results in a valid solution (not smaller than minimum)
        if b - a > min_number:
            print(b," - ", a, " = ")
            exercises += 1
        else:
            print(a," - ", b, " = ")
            exercises += 1
