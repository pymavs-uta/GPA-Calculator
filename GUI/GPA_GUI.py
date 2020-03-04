from tkinter import *
import GPA_functions

master = Tk()
from tkinter.ttk import *

GPA = StringVar()
GPA.set('0.0')
 
master.title("PyMavs GPA Calculator")
master.geometry('300x250')

label1 = Label(master, text="Enter GPA .cvs filename:", font=("Arial Bold", 15))
label1.grid(column=0, row=0)

file_entry = Entry(master,width=50)
file_entry.grid(column=0, row=1)

def calculate_GPA():
    filename = file_entry.get()
    GPA_result = GPA_functions.calculate_GPA(str(filename))
    GPA.set(GPA_result)

gpa_btn = Button(master, text="Calculate GPA", command=calculate_GPA, width=25)
gpa_btn.grid(column=0, row=4)

GPA_label = Label(master, textvariable=GPA, font=("Arial Bold", 15))
GPA_label.grid(column=0, row=5)

label2 = Label(master, text="Add entry", font=("Arial Bold", 15))
label2.grid(column=0, row=7)

new_name = Entry(master,width=20)
new_name.grid(column=0, row=8)

new_credit = Spinbox(master, from_=1, to=5, width=5)
new_credit.grid(column=0, row=9)

new_grade = Combobox(master)
new_grade['values']= ('A', 'B', 'C', 'D', 'F')
new_grade.current(1)
new_grade.grid(column=0, row=10)

def add_entry():
    GPA_functions.add_entry(file_entry.get(), new_name.get(), new_credit.get(), new_grade.get())

entry_btn = Button(master, text="Add class", command=add_entry, width=25)
entry_btn.grid(column=0, row=11)

master.mainloop()