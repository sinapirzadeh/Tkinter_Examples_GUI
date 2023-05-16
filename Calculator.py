import tkinter.messagebox
from tkinter import *

# =============== Settings ==================
root = Tk()
root.configure(bg='yellow')
root.geometry('200x142')
root.resizable(width=False, height=False)

num1 = IntVar()
num2 = IntVar()
num_res = IntVar()

# =============== Frames ==================
top_first = Frame(root, width=200, height=50, bg='red')
top_first.pack(side=TOP)

top_second = Frame(root, width=200, height=50, bg='green')
top_second.pack(side=TOP)

top_third = Frame(root, width=200, height=50, bg='black')
top_third.pack(side=TOP)

top_forth = Frame(root, width=200, height=50, bg='red')
top_forth.pack(side=TOP)


# =============== Functions ==================

def errorMsg(text_msg):
    if text_msg == 'error':
        tkinter.messagebox.showerror('Error', 'something went wrong')
    else:
        tkinter.messagebox.showerror('Division Error', 'Can Not Divide By 0')


def plus():
    try:
        value = num1.get() + num2.get()
        num_res.set(value)
    except:
        errorMsg('error')


def mai():
    try:
        value = num1.get() - num2.get()
        num_res.set(value)
    except:
        errorMsg('error')


def mul():
    try:
        value = num1.get() * num2.get()
        num_res.set(value)
    except:
        errorMsg('error')


def div():
    if num2.get() == 0:
        errorMsg('division error Zero')
    else:
        try:
            value = num1.get() / num2.get()
            num_res.set(value)
        except:
            errorMsg('error')


# =============== Buttons ==================

btn_plus = Button(top_third, text='+', width=2, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=11, pady=12)

btn_min = Button(top_third, text='-', width=2, command=lambda: mai())
btn_min.pack(side=LEFT, padx=11, pady=12)

btn_mal = Button(top_third, text='*', width=2, command=lambda: mul())
btn_mal.pack(side=LEFT, padx=11, pady=12)

btn_dev = Button(top_third, text='/', width=2, command=lambda: div())
btn_dev.pack(side=LEFT, padx=11, pady=12)

# =============== Labels and Entry ==================
label_first_num = Label(top_first, text='Number 1: ')
label_first_num.pack(side=LEFT, padx=5, pady=5)

first_num = Entry(top_first, textvariable=num1)
first_num.pack(side=LEFT)

label_second_num = Label(top_second, text='Number 2: ')
label_second_num.pack(side=LEFT, padx=5, pady=5)

second_num = Entry(top_second, textvariable=num2)
second_num.pack(side=LEFT)

label_res = Label(top_forth, text='Result is :')
label_res.pack(side=LEFT, padx=10, pady=5)

res_num = Entry(top_forth, textvariable=num_res)
res_num.pack(side=LEFT)

root.mainloop()
