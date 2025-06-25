from tkinter import * 

window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)


text = "great on this is old text from one guardian"

#Labels
label_1 = Label(text="This")
label_1.grid(column=0, row=0, columnspan=3)

label_2 = Label(text="is")
label_2.grid(column=0, row=1)

label_3 = Label(text="old")
label_3.grid(column=1, row=1)

label_4 = Label(text="text")
label_4.grid(column=2, row=1)

label_5 = Label(text="from")
label_5.grid(column=0, row=2, columnspan=2)

label_6 = Label(text="one")
label_6.grid(column=1, row=2, columnspan=2)

label_7 = Label(text="gaurdian")
label_7.grid(column=0, row=3, columnspan=3)

input_text = Entry()
input_text.grid(column=0, row=4, columnspan=3)

def on_key_release(event):
    user_input = input_text.get()
    print("User Input:", user_input)


input_text.bind("<KeyRelease>", on_key_release)


split_text = text.split(" ")
user_text = []

list_label = [label_7, label_6, label_5, label_4, label_3, label_2, label_1] 

for i in range(len(list_label)):
    print(i)
    texts = split_text[:7]
    label = list_label[i]
    label.config(text=texts[i])

window.mainloop()