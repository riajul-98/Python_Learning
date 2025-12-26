import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:

nato_phonetics = {row["letter"]:row["code"] for _, row in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("Type your name: ").upper()
phonetics = [nato_phonetics[char] for char in user_name]
print(phonetics)