# String Lists

# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

str = input("Enter the string ")

if (str==str[::-1]):
    print("It is a pallindrome")
else:
    print("not")