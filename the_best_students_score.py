students_score = {
    'Ivan': 5.00,
    'Alex': 3.50,
    'Maria': 5.50,
    'Georgy': 5.00
}

if students_score['Ivan']<4.00:
    students_score.pop('Ivan')
if students_score['Alex']<4.00:
    students_score.pop('Alex')
if students_score['Maria']<4.00:
    students_score.pop('Maria')
if students_score['Georgy']<4.00:
    students_score.pop('Georgy')
print(students_score)
