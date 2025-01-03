# # # In a .py file, create a program and use input() three times to get answers to the following questions from a user.  Store each of the answers in a variable.
# # # What is your name?
# # # What is your quest?
# # # What is your favorite color?
# # # Then, concatenate everything into a string within a print() statement with the form "So your name is [name], your quest is [quest], and your favorite color is [color]."

# # EX 1

# # userName = input("What is your name?")
# # userQuest = input("What is your quest?")
# # userColor = input("What is your favorite color?")
# # print ("So your name is", userName, "your quest is", userQuest, "and your favorite color is", userColor)
# # #okay kinda cool lol

# # EX 1
# In a Python file, use input() to ask the user to enter an integer that 10 will be added to.  Assign what they type to a variable.
# print() the sum of the integer they entered and 10.


userNum = int(input("Enter an integer that 10 will be added to "))
print ("The new total is: ",userNum + 10)
print(type(userNum))
