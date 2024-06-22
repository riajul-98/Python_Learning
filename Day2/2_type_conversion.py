# len(123) will provide an error as it is an integer

num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.") gives a type error as num_char is an integer. We need to convert
# it into a string.
# You can check the data type using type()
# print(type(num_char))

print("Your name has " + str(num_char) + " characters.")

print(70 + float("100.5"))