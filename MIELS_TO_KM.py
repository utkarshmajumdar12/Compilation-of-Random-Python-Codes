from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.config(padx=20, pady=20)

def MILES_CONV():
    miles =  float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")

#widget1
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

#is equal label

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)


#km result label

km_result = Label(text="0")
km_result.grid(column=1,row=1)

#km label

km_label = Label(text = "km")
km_label.grid(column=2,row=1)

#calculate button

calculate_button = Button(text="Calculate", command=MILES_CONV)
calculate_button.grid(column=1,row=2)

window.mainloop()