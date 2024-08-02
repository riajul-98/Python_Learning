print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("How old are you? "))
    if age > 18:
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
