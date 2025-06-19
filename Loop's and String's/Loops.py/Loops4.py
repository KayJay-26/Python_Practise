# To display the Multiplication Table of a Number.

n = int(input("Enter a number for which you want the Multiplication Table : "))

for i in range (1,21):
    print(f"{n} X {i}= {n*i}")