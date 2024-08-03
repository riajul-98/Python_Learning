# Import game data and art
import random

from game_data import data
import art

print(art.logo)


# Score keeping
score = 0
game_over = False

# Choosing game option a and option b
person_a = random.choice(data)

while not game_over:
    person_b = random.choice(data)
    if person_b == person_a:
        person_b = random.choice(data)

    name_a = person_a['name']
    name_b = person_b['name']

    # Asking player who has more followers.

    print(f"Compare A: {name_a}, a {person_a['description']} from {person_a['country']}")
    print(art.vs)
    print(f"Against B: {name_b}, a {person_b['description']} from {person_b['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Making sure the program knows the correct answer

    if person_a['follower_count'] > person_b['follower_count']:
        answer = 'a'
    else:
        answer = 'b'

    # comparing answers:
    if guess == answer:
        score += 1
        print(f"You're right! Current score: {score}")
        if person_b['follower_count'] > person_a['follower_count']:
            person_a = person_b
    else:
        print(f"Sorry, that's incorrect. Final score: {score}")
        game_over = True

