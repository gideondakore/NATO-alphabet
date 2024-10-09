from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

txt_label = "Label"

#Label
my_label = Label(text=txt_label, font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)


#Button
new_btn = Button(text="New Button")
new_btn.grid(column=2, row=0)


def btn_clicked():
    my_label.config(text=input.get())
button = Button(text="Button", command=btn_clicked)
button.grid(column=1, row=1)

#Entry
input_ = Entry(width=10)
input_.grid(column=3, row=3)
input_.insert(END, "Entry")
















window.mainloop()