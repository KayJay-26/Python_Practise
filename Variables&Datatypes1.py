# Swap two variables without using a third variable

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
a = a+b
b = a-b
a = a-b
print(f"a and b are swapped, a is {a} and b is {b}")
