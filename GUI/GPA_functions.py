import sys
import csv

def calculate_GPA(filename):
    total_credits = 0
    total_points = 0

    grade_file = open(filename, 'r')
    data = list(csv.reader(grade_file, delimiter=','))

    grade_converter = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

    for i in range(len(data)):
        values = data[i]

        name = values[0]
        
        credit = values[1]
        if not credit.isdigit():
            return 'Invalid credit on line ' + str(i)

        credit = int(credit)

        grade = values[2]
        if grade not in grade_converter:
            return 'Invalid grade on line ' + str(i)

        grade = grade_converter[grade]

        total_credits += credit
        total_points += credit*grade

    grade_file.close()

    return '{:.4f}'.format(total_points/total_credits)

def add_entry(filename, new_name, new_credit, new_grade):
    with open(filename,'a') as f:
        fields = [new_name, new_credit, new_grade]
        writer = csv.writer(f)
        writer.writerow(fields)