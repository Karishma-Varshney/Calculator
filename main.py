from tkinter import *


# -------------------------------------EQUATION----------------------------------#
def calculate(action):
    global equation
    equation = equation + str(action)
    entry_text.set(equation)


# -------------------------------------CLEARING ENTRY FIELD----------------------------------#
def clear():
    global equation
    equation = ""
    entry_text.set("")


# -------------------------------------ANSWER----------------------------------#
def ans():
    global equation
    answer = str(eval(equation))
    entry_text.set(answer)


# -------------------------------------DELETION----------------------------------#
def delete():
    global equation
    text = calcy_entry.get()
    edit_text = text[:-1]
    calcy_entry.delete(len(edit_text), END)
    equation = edit_text


# -------------------------------------UI SETUP----------------------------------#
window = Tk()
window.title('CALCULATOR')
window.config(bg='#57375D', padx=50, pady=50)

equation = ""
entry_text = StringVar()

calcy_entry = Entry(width=20, font=('Arial', 30), textvariable=entry_text)
calcy_entry.grid(row=0, column=0, columnspan=4)

clear_button = Button(text='C', bg='#FF9B82', width=4, height=2, font=('Arial', 18), command=lambda: clear())
clear_button.grid(row=1, column=0, pady=10)

cross = Button(text='⌫', bg='#FF9B82', width=4, height=2, font=('Arial', 18), command=lambda: delete())
cross.grid(row=1, column=1)

percent = Button(text='%', bg='#C23373', width=4, height=2, font=('Arial', 18), command=lambda: calculate('%'))
percent.grid(row=1, column=2)

divide = Button(text='/', bg='#C23373', width=4, height=2, font=('Arial', 18), command=lambda: calculate('/'))
divide.grid(row=1, column=3)

num1 = Button(text='1', bg='#FF3FA4', width=4, height=2, font=('Arial', 18), command=lambda: calculate(1))
num1.grid(row=4, column=0, pady=10)

num2 = Button(text='2', bg='#FF3FA4', width=4, height=2, font=('Arial', 18), command=lambda: calculate(2))
num2.grid(row=4, column=1)

num3 = Button(text='3', bg='#FF3FA4', width=4, height=2, font=('Arial', 18), command=lambda: calculate(3))
num3.grid(row=4, column=2)

num4 = Button(text='4', bg='#FF3FA4', width=4, height=2, font=('Arial', 18), command=lambda: calculate(4))
num4.grid(row=3, column=0, pady=10)

num5 = Button(text='5', bg='#FF3FA4', width=4, height=2, font=('Arial', 18), command=lambda: calculate(5))
num5.grid(row=3, column=1)

num6 = Button(text='6', bg='#FF3FA4', width=4, height=2, font=('Arial', 18), command=lambda: calculate(6))
num6.grid(row=3, column=2)

num7 = Button(text='7', bg='#FF3FA4', width=4, height=2, font=('Arial', 18), command=lambda: calculate(7))
num7.grid(row=2, column=0, pady=10)

num8 = Button(text='8', bg='#FF3FA4', width=4, height=2, font=('Arial', 18), command=lambda: calculate(8))
num8.grid(row=2, column=1)

num9 = Button(text='9', bg='#FF3FA4', width=4, height=2, font=('Arial', 18), command=lambda: calculate(9))
num9.grid(row=2, column=2)

num0 = Button(text='0', bg='#FF3FA4', width=4, height=2, font=('Arial', 18), command=lambda: calculate(0))
num0.grid(row=5, column=1)

dot = Button(text='.', bg='#C23373', width=4, height=2, font=('Arial', 18), command=lambda: calculate('.'))
dot.grid(row=5, column=0, pady=10)

multiply = Button(text='*', bg='#C23373', width=4, height=2, font=('Arial', 18), command=lambda: calculate('*'))
multiply.grid(row=2, column=3)

subtract = Button(text='-', bg='#C23373', width=4, height=2, font=('Arial', 18), command=lambda: calculate('-'))
subtract.grid(row=3, column=3)

add = Button(text='+', bg='#C23373', width=4, height=2, font=('Arial', 18), command=lambda: calculate('+'))
add.grid(row=4, column=3)


equal = Button(text='=', bg='#FF9B82', width=12, height=2, font=('Arial', 18), command=lambda: ans())
equal.grid(row=5, column=2, columnspan=3)

window.mainloop()
