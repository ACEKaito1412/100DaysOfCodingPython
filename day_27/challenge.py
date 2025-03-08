# mile to km converter
import tkinter


win = tkinter.Tk()
win.minsize(width=120, height=40)

labe1_1 = tkinter.Label(text="is equal to")
labe1_1.grid(column=0, row=1)
labe1_2 = tkinter.Label(text="Miles")
labe1_2.grid(column=2, row=0)
labe1_3 = tkinter.Label(text="Km")
labe1_3.grid(column=2, row=1)

converted_label = tkinter.Label(text=0)
converted_label.grid(column=1, row=1)

mile_input = tkinter.Entry(width=20)
mile_input.grid(column=1, row=0)

def calculate():
    base = 1.6
    mile =int(mile_input.get())
    km = mile * base
    converted_label.config(text = round(km, 3))



btn_calculate = tkinter.Button(text="Calculate", command=calculate)
btn_calculate.grid(column=1, row=2)
win.mainloop()


