# ASSIGNMENT
"""
Write a while loop that adds 3 to a number while the number
is still less than 500, and print only the last number after
while loop is complete.
"""
num = 0
while num < 500:
    num = num + 3
print (num)


"""Write a function that takes one variable that will be a number
and prints a number while the number is less than the number passed
as the variable. print "Done", once the while loop is complete."""



for i in range(14):
    for j in range(14):
        print(f"{(i+j)*2:4}", end = " ")
    print()

num = 0
string = ("evangeline")
while num < len(string):
    char = string[num]

    # Check if the character is a vowel
    if char.lower() in 'aeiou':
        # Print the vowel in capital letters
        print(char.upper())
    else:
        # Print the non-vowel character as is
        print(char)
    
    # Increment the num variable
    num += 1

word = "elephant"
for letter in word:
    if letter is "aeiou"
    print(word.upper())
    else print (word)