studentScore = int (input("What is your score? "))

# gradeA = studentScore >=90
# gradeB = studentScore >=80
# gradeC = studentScore >=70
# gradeD = studentScore >=60
# gradeF = studentScore >=59

if (studentScore >=90) :
    print ("You have recieved an A grade!")
    
if studentScore >=80 and studentScore < 90:
    print ("You have recieved an B grade!")

if (studentScore >=70 and studentScore <80) :
    print ("You have recieved an C grade!")

if (studentScore >=60 and studentScore <70) :
    print ("You have recieved an D grade!")

if (studentScore <60) :
    print ("You have failed this class... GRADE")