import sys
import csv

filename = sys.argv[1]

total_credits = 0
total_points = 0

grade_file = open(filename, 'r')
data = list(csv.reader(grade_file, delimiter=','))

grade_converter = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

for i in range(len(data)):
    values = data[i]

    if not credit.isdigit():
        print('Invalid credit on line ' + i)
        continue
    
    credit = int(credit)

    if grade not in grade_converter:
        print('Invalid grade on line ' + i)
        continue

    grade = grade_converter[grade]

    total_credits += credit
    total_points += credit*grade

grade_file.close()

print('Total points: ', total_points)
print('Total credit hours: ', total_credits)
final_gpa = total_points/total_credits
print('Semester GPA: {:.4f}'.format(final_gpa)