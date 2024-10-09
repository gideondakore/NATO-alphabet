from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=600, height=300)
window.config(padx=20, pady=20)

#Mile Entry
mile_input = Entry()
mile_input.config(width=10)
mile_input.focus()
mile_input.grid(row=0, column=1)

mile_sign = Label(text="Miles")
mile_sign.grid(row=0, column=2)

#Km Label
km_label = Label(text="is equal to")
km_label.grid(row=1, column=0)

# label_value = ""
km_label_val = Label(text="0", width=10)
km_label_val.grid(row=1, column=1)

km_sign = Label(text="Km")
km_sign.grid(row=1, column=2)

#Button
def calculate():
    miles_val = mile_input.get()
    if not miles_val:
        result = "0"
    else:
        result = round(float(miles_val) * 1.609)

    print("Results: ", result)

    km_label_val.config(text=str(result))

btn = Button(text="Calculate", command=calculate)
btn.grid(row=2, column=1)



window.mainloop()

