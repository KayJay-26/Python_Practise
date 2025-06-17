# To Check if a character is a vowel or consonant

character = input("Enter your character : ")
vow = "aeiouAEIOU"

if(character in vow):
    print("Its a vowel.")

else:
    print("Its a consonant.")