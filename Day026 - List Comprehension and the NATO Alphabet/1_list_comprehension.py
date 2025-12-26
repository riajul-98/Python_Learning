number = [1, 2, 3]
new_numbers = [i**2 for i in number]
print(new_numbers)

name = "Riajul"
new_list = [letter for letter in name]
print(new_list)

new_range = range(1, 5)
double = [i * 2 for i in new_range]
print(double)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
names_list = [name for name in names if len(name) <= 4]
print(names_list)

uppercase_names = [name.upper() for name in names if len(name) >= 5]
print(uppercase_names)