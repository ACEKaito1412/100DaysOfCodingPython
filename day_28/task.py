import tkinter

window = tkinter.Tk()


window.title("My First GUI Program")
window.minsize(width=500, height=300)


# label
my_label  = tkinter.Label(text="My Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# buttton

def button_click():
    print("i got clicked")
    val = input.get()
    my_label.config(text=val)

btn = tkinter.Button(text="click me" , command=button_click)
btn.grid(column=1, row=1)


btn_2 = tkinter.Button(text="click me" , command=button_click)
btn_2.grid(column=2, row=0)

# entry / input

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)





window.mainloop()