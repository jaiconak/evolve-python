# iteration = range (1,50,1)
# for number in iteration :
#     if number % 5 == 0 and number % 3 ==0 :
#         print (number,"FizzBuzzSKII")
#     elif number % 3 == 0 :
#         print (number, "Fizz")
#     elif number % 5 == 0 :
#         print (number, "Buzz")
#     else:
#         print (number)
        


# Problem 2
# Programming Challenge: Factorial
# Create a function which takes one positive integer as its input and returns its factorial.

# Okay going into the problem. I have to create a program where it asks the user to input an integer. 
# From that integer there would be calculation involved. And it would return a print statement of that input's
# Factorial correct? Is there a need to have validation whether its float? Negative Number? String? 
# Or can I assume that the user will input a positive INTEGER?

# Okay well the very first step lets create a variable that asks the user to input an integer and we'll start from there
userInputNum = int (input("Enter an integer"))
# From here I have to start the calculation. From what I remember how factorial works is that
# It is x * (x-x(-1)) * x(x-(x-1)... up until x*1 [ex 3.. 3 x 2 x 1=6 ] or ex 4.. [4 x 3 x 2 x 1=24])
# So for sure well need to do a loop where first it starts off in the input from user. Then it traverses
# by -1 each time. and the final number is 1. so just from going through that Ill need to do a range.
# so first we'll create a variable where we can use store the range in. we'll name it factorial
factorial = range(userInputNum,1,-1)  #what this does is it starts from userInput. The end is 0 and we'll decrement by 1 each time
sum = 1 #this starts us off at one that way when we first multiply the first number it will multiply it by itself
for number in factorial :
    # this is where we'll do the calculation, the calculation is that each time its being multiplied it has a place to be stored in.
    sum = sum * number
    print(sum)

