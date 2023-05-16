from tkinter import *

# ========= Setting ===========
root = Tk()
root.title("Profit Calculator")
root.resizable(width=False, height=False)
root.geometry('250x300')
root.configure(bg='Tan')

equity = StringVar()
percentage = StringVar()
goal = StringVar()
list_Result = []

# ========== Forms ============
top_1 = Frame(root, width=250, height=100)
top_1.pack(side=TOP)

top_2 = Frame(root, width=250, height=150)
top_2.pack(side=TOP)

top_3 = Frame(root, width=250, height=50)
top_3.pack(side=TOP)

# ========= Inputs ===========
lbl_1 = Label(top_1,text='Your Equity')
lbl_1.grid(row=0, column=0)
lbl_1.configure(bg='white')
num_1 = Entry(top_1, textvariable=equity, font=('Arial', 10))
num_1.grid(row=0, column=1)

lbl_2 = Label(top_1,text='Your Percentage')
lbl_2.grid(row=1, column=0)
lbl_2.configure(bg='white')
num_2 = Entry(top_1, textvariable=percentage, font=('Arial', 10))
num_2.grid(row=1, column=1)

lbl_3 = Label(top_1,text='Your Goal')
lbl_3.grid(row=2, column=0)
lbl_3.configure(bg='white')
num_3 = Entry(top_1, textvariable=goal, font=('Arial', 10))
num_3.grid(row=2, column=1)

# ========= Buttons ===========

btn_result = Button(top_3, text='Show Result', command=lambda: opertion(equity.get(), percentage.get(), goal.get()))
btn_result.grid(row=4, column=0)

# ========= List_Result ===========
lBox = Listbox(top_2, width=35, height=12, font=('Arial', 10))
lBox.grid(row=3, column=0)

sb1 = Scrollbar(top_2)
sb1.grid(row=3, column=1)

lBox.configure(yscrollcommand=sb1.set)
sb1.configure(command=lBox.yview)


# ========= BackEnd ===========


def opertion(a, b, d):

    a = float(a)
    b = float(b)
    d = float(d)

    list_Result.clear()
    lBox.delete(0, END)
    c = 0
    while a <= d:
        c += 1
        e = a
        a = a * b + a
        f = a - e
        list_Result.append(f'D : {c} - {int(a)} -+- {int(f)}')

    for i in list_Result:
        lBox.insert(END, i)


root.mainloop()
