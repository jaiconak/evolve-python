#function with no parameters exercise
#Do all of this in a .py file in Pycharm.
#Create a function called hello_world_printer() which takes no parameters and prints the string "hello world"
#Call the function hello_world_printer()

# #prob 1
# def helloWorldPrinter () :
#     print("hello world")
    
    
# helloWorldPrinter()


#Create a function called name_printer which takes 1 parameter and prints it
#Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.
#Call name_printer() with the variable "name" as its argument.

#def name_printer(stringInput) :
#    print(stringInput)
    
    
#name = input("What is your name?")
#name_printer(name)


#Programming Challenge: Volume of a Rectangular Prism

#For this programming challenge, you will be creating a function that calculates the volume of a rectangular prism in cubic feet.  The formula to find the volume of a rectangular prism is V = l * w * h where l, w, and h are length, width, and height, respectively.

#First, create three variables representing length, width, and height.   Assign each of them an integer as user input using the input() function and int().

#Next, create a function to calculate the volume of the rectangular prism.  It should have 3 parameters representing length, width, and height and return the volume of a rectangular prism calculated using those 3 parameters.

#Finally, use print() to display "The volume of the rectangular prism is [call function  here to calculate volume] cubic feet." in the output.  You will have to use str() on the function call to be able to concatenate it with strings since it returns an integer.

#def volRec (length, width, height) :
#    return length * width * height


#userInputLength = int (input("Give me an INT for length "))
#userInputWidth = int (input("Give me an INT for width "))
#userInputHeight = int (input("Give me an INT for height "))

#print("The volume of the rectangular prism is ",volRec(userInputLength,userInputWidth,userInputHeight), "feet")

#Programming Challenge: Celsius to Fahrenheit
#The formula for converting from degrees Celsius to degrees Fahrenheit is as follows:

#F = 1.8 * C + 32
#Where F is the Fahrenheit temperature and C is the Celsius temperature.
#In a .py file, create a variable and assign it an integer representing a celsius temperature that is entered as user input().  input()'s message should prompt the user to enter an integer value.
#For this programming challenge, you will then write a function called fahrenheit that takes in an integer representing a Celsius temperature as its argument.  The function will return the Fahrenheit equivalent temperature of that argument to 1 place after the decimal.
#At the end of your program, display the Fahrenheit equivalent in a print statement message formatted like so:  "The Fahrenheit equivalent of [user entered integer] degrees Celsius is [number returned by function]".
#To make sure that the function works, run your program multiple times and call the function on different user entered integer values both negative and positive.


# def celToFahr(c) :
#     return c * (9/5) + 32


# userCel = int (input("Enter degrees that you want to convert. "))
# print ("The conversion for what you inputted to Fahrenheit is: ",round(celToFahr(userCel),2))

# from random import *
# print (random ())

# Programming Challenge: Miles Per Gallon
# For this exercise, you will create a program that approximates the number of miles per gallon that a car gets.

# In a .py file, create two variables, one which will hold a randomly generated integer between 10 and 25 (inclusive of both 10 and 25), and another which will hold a randomly generated integer between and inclusive of 200 and 400. The first variable represents the number of gallons of gas that the car's fuel tank holds. The second variable represents the miles that the car can travel on a full tank before needing a refuel.

# Using the formula miles per gallon (MPG) = miles driven/gallons used, calculate the car's MPG and display it in the output using print().  Use floor division instead of regular division for this calculation to get an integer instead of a float.  This will give a realistic approximation of miles per gallon even though floats such as 19.8 round down a large amount when using floor division since sometimes, car manufacturers sometimes exaggerate miles per gallon.  In addition, display the values held in the variables you created for gallons of gas in the car's fuel tank and miles it can travel on a full tank with two different print statements.
from random import *
randNumberGal= randint (10,25)
randNumFullTank= randint (200,400)

def mpg (numFullTank,numberGal) :
    return numFullTank // numberGal

print (randNumberGal)
print (randNumFullTank)
print (mpg(randNumFullTank,randNumberGal))