from tkinter import *

window = Tk()
window.title("Mile to km Converter")
window.minsize(width=250, height=100)
window.config(padx=40, pady=20)


# Entry and Labels
mile_entry = Entry(width=10)
mile_entry.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="Is Equal to ")
is_equal_label.grid(column=0, row=1)

km_label = Label(text="0")
km_label.grid(column=1, row=1)

km_word = Label(text="Km")
km_word.grid(column=2, row=1)


# Button
def calc():
    number = float(mile_entry.get())
    km = round(number * 1.6)
    km_label.config(text=km)


calc_btn = Button(text="Calculate", command=calc)
calc_btn.grid(column=1, row=2)


window.mainloop()