# To write a Python program to calculate the sum of all even numbers from 1 to a number N entered by the user.

N = int(input("Enter your desired value : "))

sum = 0
total_sum = 0

for i in range (0,N+1):
    if i%2 == 0:
        sum += i


total_sum = sum

print(total_sum)
    