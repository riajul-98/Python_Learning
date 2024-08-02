# Reproduce the Bug

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Reproducing the bug to always produce the error:

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# print(dice_imgs[6])

# Cause: The limits within the randint are wrong as python lists start with 0, hence looking for the 6th index would be
# the 7th list item which does not exist.

# Fixed code:

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
