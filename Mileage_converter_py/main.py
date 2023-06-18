# miles to km = multiply by 1.609

# import the library that we will use for our GUI (Graphical User Interface)
import tkinter as tk

# window set-up
window = tk.Tk()
window.title("Mileage Converter")
window.minsize(width=300, height=200)
window.config(padx=30, pady=40)


# labels & input box
mile_input = tk.Entry(width=8)
mile_input.focus()
mile_input.grid(column=1, row=0)

mile_label = tk.Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

result_label = tk.Label()
result_label.grid(column=1, row=1)

calculate = tk.Button(text="Calculate")
calculate.grid(column=1, row=2)

window.mainloop()
