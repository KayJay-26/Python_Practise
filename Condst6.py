# To Find the grade of a student based on marks

Marks = int(input("Enter your Marks : "))

if Marks >= 75 :
    print("Passed! With 'A' grade. ")

elif Marks < 75 and Marks > 50:
    print("Passed! With 'B' grade. ")

elif Marks == 50:
    print("Just Passed, 'C' grade.")

else:
    print("Fail, Reapper.")