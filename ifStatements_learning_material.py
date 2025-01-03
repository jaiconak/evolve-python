from random import randint 
# studentScore = int (input("What is your score? "))

# gradeA = studentScore >=90
# gradeB = studentScore >=80
# gradeC = studentScore >=70
# gradeD = studentScore >=60
# gradeF = studentScore >=59

# if studentScore >= 90 :
#     print ("You will recieve an A grade")
# else:
#     if studentScore >=80 :
#         print ("You will receive an B grade")
#     else:
#         if studentScore >=70 :
#             print ("You will receieve an C grade")
#         else:
#             if studentScore >=60 :
#                 print ("You will receive an D grade")
#             else:
#                 print ("You have failed this class.. F!")

# Now will do it in elif statements

# if studentScore >= 90 :
#     print("You will receive an A grade")
# elif studentScore >=80 :
#     print("You will receive an B grade")
# elif studentScore >=70 :
#     print ("You will recieve an C grade")
# elif studentScore >=60 :
#     print("You will receive an D grade")
# else :
#     print ("You failed bud")

randomNum = randint (1,10)
print(randomNum, "is the randomized number and in roman numerals its displayed as: ")
if randomNum == 1 :
    print ("I")
elif randomNum == 2 :
    print ("II")
elif randomNum == 3 :
    print ("III")
elif randomNum == 4 :
    print ("IV")
elif randomNum == 5 :
    print ("V")
elif randomNum == 6 :
    print ("VI")
elif randomNum == 7 :
    print ("VII")
elif randomNum == 8 :
    print ("VIII")
elif randomNum == 9 :
    print ("IX")
elif randomNum == 10 :
    print ("X")
