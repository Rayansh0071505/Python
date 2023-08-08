# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def check(n):
    if(n%2==0):
        print("It is Even")
    else:
        print("It is Odd")

    if(n%4==0):
        print("It is also multiple of 4")

def div(n,m):
    z=n/m
    if(z%2==0):
        print("It is even")
    else:
        print("Odd")

print("Enter the num")
n=int(input())
check(n)
print("Enter the numk to check")
c=int(input())
div(n,c)

