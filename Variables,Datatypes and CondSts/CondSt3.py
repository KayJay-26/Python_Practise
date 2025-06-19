# To Check if a year is a leap year

year = int(input("Enter the year you want to check : "))

if (year%4 == 0 or year%400 == 0):
    print("Yes, This is a leap year.")

else:
    print("No, This is not a leap year.")