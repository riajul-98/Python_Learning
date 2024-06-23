# You can combine different conditions using logical operators which are 'and', 'or' and 'not'.

# and operator will only return true if both conditions are true
# or operator will return true if either condition is true
# not operator will return true if none of the conditions are true

# a = 12
#
# print(a > 11 and a < 13)
# print(a > 11 or a < 2)
# print(not a > 15)

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("How old are you? "))

    if age >= 45 and age <= 55:
        print("Have a free ride on us.")
    elif age > 18:
        print("Adult tickets are $12.")
        bill = 12
    elif age >= 12:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Child tickets are $5.")
        bill = 5

    photo = input("Do you want a photo taken? Y or N: ")
    if photo == "Y":
        bill += 3
    print(f"Your total is {bill}.")
else:
    print("You are not tall enough for this rollercoaster")

