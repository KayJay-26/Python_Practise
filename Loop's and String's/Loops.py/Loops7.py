# To Write a Python program to reverse the digits of a number entered by the user, using a loop (not string slicing).


num = int(input("Enter the number to be reversed : "))
rev = 0

while num>0 :
    digit = num%10
    rev = rev*10 + digit
    num = num // 10

final = rev
    
print(final)

