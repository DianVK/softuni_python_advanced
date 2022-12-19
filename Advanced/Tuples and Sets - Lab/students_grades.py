#from statistics import mean
count_students = int(input())
all_students = {}

for student in range(count_students):
    student_name,student_grade = input().split()
    student_grade = float(student_grade)
    if student_name not in all_students:
        all_students[student_name] = []
    all_students[student_name].append(student_grade)

for data in all_students.items():
    print(f"{data[0]} -> {' '.join([f'{el:.2f}' for el in data[1]])}"
          f" (avg: {(sum(data[1]) / len(data[1])):.2f})")