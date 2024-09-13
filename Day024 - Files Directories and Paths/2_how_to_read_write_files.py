# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#

# with open("my_file.txt", mode="a") as file:
#     # Modes:
#     #   - "r": Read
#     #   - "w": Write (Removes all previous content)
#     #   - "a": Append (Adds to the existing content)
#     file.write("\nI like Anime.")

with open("new_file.txt", mode="w") as file:
    file.write("New text.")