# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
#
# drink_potion()
# # print(potion_strength) gives an error as this variable is local to the function above.

# Global Scope

player_health = 10


def drink_potion():
    potion_strength = 2
    print(player_health) # Prints due to global scope

drink_potion()
