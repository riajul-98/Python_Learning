# Instructions
# Read this the code in 1_attributes_init_and_constructors.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# Fix the code so that it works and passes the tests when you submit.
#
# Hint
# Review the previous lesson and go through the 10 steps to tackle these debugging problems.

# number = int(input("Which number do you want to check? "))
#
# if number % 2 = 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# The issue was on line 12, there was an assignment operator rather than the double equals comparison operator.
