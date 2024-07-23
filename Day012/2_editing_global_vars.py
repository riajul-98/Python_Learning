enemies = 1


def increase_enemies():
    global enemies   # This is used to bring the global enemies and modify it
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
