# # Describe Problem
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
#
#
# my_function()


# Description of problem: The function only prints an output once i = 20 in the for loop but when it is run, nothing
# prints.

# Cause: Nothing prints as 20 is not included in the range.

# Fixed code:

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()
