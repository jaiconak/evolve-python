# Create a variable and assign it the sum of two integers
# Create a variable and assign it the difference of two integers
# Create a variable and assign it the result of one integer being divided by another integer
# Create a variable and assign it the product of two integers
# Create a variable and assign it the result of 3 raised to the 8th power
# Create a variable and assign it the result of 10 floor division 3
# Create a variable and assign it the integer 2 using the expression 17 modulo [number]

num1 = 20
num2 = 7

sum = num1 + num2 #prob1
difference = num1 - num2 #prob2
divide = num1/num2 #prob3
product = num1 * num2 #prob4
exponents = 3 **8 #prob 5
floor = 10 // 3
modulo = 17 % 5



print (sum, difference, divide, product, exponents, floor, modulo)


# A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:
# Penne 16 oz Pack of 12 - $16.68
# Arrabiata Pasta Sauce 24 oz - $6.98
# Bag of 20 Organic Garlic Cloves - $16.78
# Italian Seasoning 1.5 oz Bottle - $15.26
# Artisan Baguettes Twin Pack - $3.00
# 12 oz Bag of Meatballs - $4.39
# In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.  The subtotal is just the sum of all of their prices.
# Use print() to display the result of the expression.

penne = 16.68
sauce = 6.98
garlic = 16.78
seasoning = 15.26
baguettes = 3
meatballs = 4.39
total = penne + sauce + garlic + seasoning + baguettes + meatballs
print ("The total is $",round(total,2),"today")