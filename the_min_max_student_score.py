students_score = {
    'Ivan': 5.00,
    'Alex': 3.50,
    'Maria': 5.50,
    'Georgy': 5.00
}

for name, score in students_score.items():
    if name == max(students_score):
        print ('{} {}'.format(name,score))
for name, score in students_score.items():
    if name == min(students_score):
        print ('{} {}'.format(name,score))
