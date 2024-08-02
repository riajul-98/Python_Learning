# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# 1994 is not included in the above code and therefore, neither of the conditions are true

# Fixed code:

# Play Computer
year = int(input("What's your year of birth?"))
if 1980 < year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")
