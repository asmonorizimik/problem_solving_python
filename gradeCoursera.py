# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85 and output will be grade B .


score=input("enter score: ")
try:
    score1=float(score)
except:
    print("error.. enter numeric..")
    quit()

if score1>=0.0 and score1<=1.0:
    if score1>=0.9:
        print("A")
    elif score1>=0.8 and score1<=0.9:
        print("B") 
    elif score1>=0.7 and score1<=0.8:
        print("C") 
    elif score1>=0.6 and score1<=0.7:
        print("D") 
    else:
        print("F")
else:
    print("a suitable error message and exit. ")



