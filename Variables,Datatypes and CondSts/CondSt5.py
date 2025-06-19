# To Check if a number is divisible by both 3 and 5

num = int(input("Enter your number : "))

if (num%3 == 0 and num%5 == 0):
    print("Yes,Its divisible by 3 and 5.")

else:
    print("No,Its not divisible by 3 and 5.")