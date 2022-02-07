#####################################################
"""Purpose : practicing coding with documentations """
"""Date: 07/02/2022"""
"""author: Sanchaitya"""
"""writing a code for book keeping"""
#####################################################

# Import Module
from tkinter import *
from PIL import Image, ImageTk

# Create Object
root = Tk()

# Set geometry
root.geometry('600x600')
root.minsize(400, 400)
root.maxsize(600, 600)

# trying to add good image
image = Image.open("2114456.jpg")
photo = ImageTk.PhotoImage(image)
img_label = Label(image=photo)

# Set title on the box
root.title("Book List")

# Information List
datas = []


# Add Information
def add():
    global datas
    datas.append([Name_of_Book.get(), Name_of_Employee.get(), Vote.get(1.0, "end-1c")])
    update_book()


# View Information
def view():
    Name_of_Book.set(datas[int(select.curselection()[0])][0])
    Name_of_Employee.set(datas[int(select.curselection()[0])][1])
    Vote.delete(1.0, "end")
    Vote.insert(1.0, datas[int(select.curselection()[0])][2])


# Delete Information
def delete():
    del datas[int(select.curselection()[0])]
    update_book()


def reset():
    Name_of_Book.set('')
    Name_of_Employee.set('')
    Vote.delete(1.0, "end")


# Update Information
def update_book():
    select.delete(0, END)
    for n, p, a in datas:
        select.insert(END, n)


# Add Buttons, Label, ListBox
Name_of_Book = StringVar()
Name_of_Employee = StringVar()

frame = Frame()
frame.pack(pady=10)

frame1 = Frame()
frame1.pack()

frame2 = Frame()
frame2.pack(pady=10)

Label(frame, text='Name_of_Book', font='arial 12 italic').pack(side=LEFT)
Entry(frame, textvariable=Name_of_Book, width=50).pack()

Label(frame1, text='Name_of_Employee', font='arial 12 italic').pack(side=LEFT)
Entry(frame1, textvariable=Name_of_Employee, width=50).pack()

Label(frame2, text='Vote', font='arial 12 italic').pack(side=LEFT)
Vote = Text(frame2, width=50, height=2)
Vote.pack()

Button(root, text="Add", font="arial 12 bold", command=add).place(x=100, y=270)
Button(root, text="View", font="arial 12 bold", command=view).place(x=100, y=310)
Button(root, text="Delete", font="arial 12 bold", command=delete).place(x=100, y=350)
Button(root, text="Reset", font="arial 12 bold", command=reset).place(x=100, y=390)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, width=50, height=12)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200, y=260)

img_label.pack()
# Execute Tkinter
root.mainloop()
