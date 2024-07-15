# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#
# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
#
# It will take your current age as the input and output a message with our time left in this format:
#
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
#
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

age = input("Please enter your age: ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

age_in_weeks = int(age) * 52
total_weeks = 90 * 52
weeks_left = total_weeks - age_in_weeks

print(f"You have {weeks_left} weeks left.")
