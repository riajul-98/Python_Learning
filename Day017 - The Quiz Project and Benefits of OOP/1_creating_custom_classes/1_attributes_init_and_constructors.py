# # Creating a new class
# class User:
#     pass
#
#
# # Creating an object from a class
# user_1 = User()
#
# # Creating object attributes
# user_1.id = "001"
# user_1.username = "riajul"
#
# print(user_1.username)
#
# # For new objects, you can repeat the process like below but this can be prone to errors. It would be better to use
# # constructors.
# user_2 = User()
# user_2.id = "002"
# user_2.username = "angela"

# Constructors allow variables of an object to be set to a starting value. You would use the __init__ keyword.
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0      # Default value


user_1 = User("001", "riajul")

print(user_1.followers)
