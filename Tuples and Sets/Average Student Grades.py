n = int(input())

students_grades = {}

for _ in range(n):
    student, grade = input().split()
    grade = float(grade)
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(grade)

for student, grades in students_grades.items():
    print(f'{student} -> ', end='')
    for el in grades:
        print(f'{el:.2f}', end=' ')
    print(f'(avg: {(sum(grades) / len(grades)):.2f})')
