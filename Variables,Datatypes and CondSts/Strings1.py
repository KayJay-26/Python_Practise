# To find the number of vowels in a particular string.

str = input('''Enter a string : ''')

vowels = "aeiouAEIOU"

count = 0

for char in str:
    if char in vowels:
        count += 1

print(count)