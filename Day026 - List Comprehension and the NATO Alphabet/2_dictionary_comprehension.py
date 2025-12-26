import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)


generated_scores = {'Alex': 73, 'Beth': 26, 'Caroline': 56, 'Dave': 82, 'Elanor': 52, 'Freddie': 81}
passed_students = {student:score for (student, score) in generated_scores.items() if score >= 60}
print(passed_students)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temperature * 9/5 + 32) for (day, temperature) in weather_c.items()}

print(weather_f)