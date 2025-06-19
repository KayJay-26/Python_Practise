# To find the Factorial of a Number.

num = int(input("Enter your desired number : "))

factorial = 1

for i in range(1,num+1):
    
    factorial *= i                                   
    # above is same as factorial = factorial * i
print(f"Factorial of {num} is {factorial}" )