# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")


# Cause: The red line under the last print statement indicates line 4 is the issue. I can see it is part of an if block
# and therefore, the issue is an indentation error. I can also see age is a string rather than an integer

# Fixed code:

# Fix the Errors
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")
