students_score = {
    'Ivan': 5.00,
    'Alex': 3.50,
    'Maria': 5.50,
    'Georgy': 5.00
}

students_score_max = max(students_score, key=students_score.get)
students_score_min = min(students_score, key=students_score.get)

for name, score in students_score.items():
    if name == students_score_max:
        print ('{} {}'.format(name,score))
for name, score in students_score.items():
    if name == students_score_min:
        print ('{} {}'.format(name,score))
