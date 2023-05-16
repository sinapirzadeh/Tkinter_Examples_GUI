from tkinter import *
import sqlite3

# backend codes in this class :
class backend:
    
    def connect():
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text, year INTEGER, isbn INTEGER )")
        conn.commit()
        conn.close()


    def insert(title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        conn.commit()
        conn.close()


    def view():
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows


    def search(title="", author="", year="", isbn=""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows


    def delete(id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()
        conn.close()


    def update(id, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?", (title, author, year, isbn, id))
        conn.commit()
        conn.close()


    connect()


def clear_list():
    list1.delete(0, END)


def fill_list(books):
    for book in books:
        list1.insert(END, book)


window = Tk()
window.title("Book Store")

# ===================== Labels ========================
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# ===================== Entries ========================

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, width=35, height=6)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


def get_selected_row(event):
    global selected_book
    selected_book = list1.get(index)


list1.bind("<<ListboxSelect>>", get_selected_row)


def view_command():
    clear_list()
    books = backend.view()
    fill_list(books)


b1 = Button(window, text="View All", width=12, command=lambda: view_command())
b1.grid(row=2, column=3)


def search_command():
    clear_list()
    books = backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    fill_list(books)


b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()


b3 = Button(window, text="Add Entry", width=12, command=lambda: add_command())
b3.grid(row=4, column=3)


def update_command():
    backend.update(selected_book[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()


b4 = Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)


def delete_command():
    backend.delete(selected_book[0])
    view_command()


b5 = Button(window, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

view_command()
window.mainloop()
