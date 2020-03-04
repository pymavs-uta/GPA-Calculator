# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:53:52 2020

@author: Kyra
"""
#Focus on lists, loops, if-else, print output(?)
grade_list = []
credit_list = []
name_list = []
x = 1
total_credits = 0
total_points = 0
print('Semester GPA calculator')
num_of_classes = int(input('How many classes did you have?: '))
while x <= num_of_classes:
    name1 = input('Name of class ' + str(x) + ': ')
    name_list.append(name1)
    credit = 0
    while True:
        credit = input('How many credits was the class?: ')
        if credit.isdigit():
            break
        else:
            print('Invalid, enter an integer')
    credit_list.append(int(credit))
    while True: #wth is this
        grade1 = input('What grade did you get? (A,B,C,D,F): ')
        grade1 = grade1.upper()
        if grade1 == 'A':
            grade1 = 4.0
            grade_list.append(grade1)
        elif grade1 == 'B':
            grade1 = 3.0
            grade_list.append(grade1)
        elif grade1 == 'C':
            grade1 = 2.0
            grade_list.append(grade1)
        elif grade1 == 'D':
            grade1 = 1.0
            grade_list.append(grade1)
        elif grade1 == 'F':
            grade1 = 0.0
            grade_list.append(grade1)
        else:
            print('Invalid input, try again')
            continue
        break
    x += 1
i = 0
for i in range(0, len(grade_list)): 
        total_credits = total_credits + credit_list[i]                   
        total_points = total_points + (grade_list[i] * credit_list[i])
print(name_list)
print(grade_list)
print(credit_list)
print('Total points: ',total_points)
print('Total credit hours: ', total_credits)
final_gpa = total_points/total_credits
print('Semester GPA: %0.2f'% (final_gpa))