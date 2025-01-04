# PROBLEM 1
# counter = 10
# while counter >=0 :
#     print (counter)
#     counter = counter -1

# PROBLEM 2
# todo1: The program should then use a while loop to get the sum of all of the integers 
# from the integer that was entered by the user down to 1.

#todo example:if the integer entered by the user was 6, the while loop would find the sum of 
# 6, 5, 4, 3, 2, and 1, which is 21.

# userNum = int(input("Enter a POSITIVE NUMBER: "))
# sum = 0
# if userNum <=0:
#     print ("ERROR: MUST BE A POSITIVE NUMBER ")
# else:
#     while userNum > 1:
#         sum +=userNum
#         userNum = userNum -1
#     print (sum)
    
    
    # Think about it. So the first stage shows whether or not its a postive number
    # from the second stage it has to see whether or the number is greater than 1
    # as it traverses through the loop we have a counter which is also the userNum that was generated.
    # we also have a total that adds each number to each other.

# Problem 1
# phrase = "hello world"
# for letter in phrase :
#     print (letter)

# Problem 2
wordSelected = input ("Enter a string: ")
counter = 0
# will display the number of characters in the string.  
# For example, if the user entered the string "hello world", the number of characters would be 11.
for letter in wordSelected :
    counter += 1
    # print(letter)
print ("Amount of letters in the word:",counter)
print ("Word Selected was: ",wordSelected)
