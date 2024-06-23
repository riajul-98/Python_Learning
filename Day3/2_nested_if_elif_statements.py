# Nested if statements allow you to check other conditions if the initial condition is met.

# If conditions allow your code to execute a block of code if a certain condition is met. Else statements execute
# another code block of code if the conditions are not met.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("How old are you? "))
    if age > 18:
        print("That will be $12 please.")
    elif 18 >= age >= 12:
        print("That will be $7 please.")
    else:
        print("That will be $5 please.")
    print("Have fun!")
else:
    print("You are not tall enough for this rollercoaster")


# Elif allows you to check other conditions after the if statement and before the else statement
