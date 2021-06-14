from tkinter import *
from tkinter import ttk

window = Tk()

window.title("Employee details")

window.geometry('300x300')

window.configure(background = "pink");

Employeename = Label(window ,text = "Employee Name").grid(row = 0,column = 0)
EmployeeId= Label(window ,text = "Employee Id").grid(row = 1,column = 0)

Salary= Label(window ,text = "salary").grid(row = 2,column = 0)

EmployeeCTC=Label(window,text="Employee CTC").grid(row=3,column=0)

MobileNo = Label(window ,text = "Mobile Number").grid(row = 4,column = 0)

Probatitionarytax=Label(window,text="Probatitionary tax").grid(row=5,column=0)

Overtime=Label(window,text="Overtime").grid(row=6,column=0)

Medical=Label(window,text="Medical").grid(row=7,column=0)

Contributions=Label(window,text="Contributions").grid(row=8,column=0)

TA=Label(window,text="TA").grid(row=9,column=0)
HRA=Label(window,text="HRA").grid(row=10,column=0)


EmployeeName= Entry(window).grid(row = 0,column = 1)

EmployeeId = Entry(window).grid(row = 1,column = 1)

Salary= Entry(window).grid(row = 2,column = 1)

EmployeeCTC= Entry(window).grid(row = 3,column = 1)

MobileNo=Entry(window).grid(row=4,column=1)

Probatitionarytax=Entry(window).grid(row=5,column=1)

Overtime=Entry(window).grid(row=6,column=1)

Medical= Entry(window).grid(row = 7,column = 1)

Contributions = Entry(window).grid(row = 8,column = 1)

TA = Entry(window).grid(row = 9,column = 1)

HRA = Entry(window).grid(row = 10,column = 1)

def clicked():
         res = "Welcome to " + txt.get()
         lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=10,column=0)
window.mainloop()
