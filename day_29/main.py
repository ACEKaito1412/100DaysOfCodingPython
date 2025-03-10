from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_name = website_entry.get()
    user_email = username_entry.get()
    password = password_entry.get()

    if website_name == "":
        messagebox.showinfo(title="Info", message="Empty field: website")
        return

    if user_email == "":
        messagebox.showinfo(title="Info", message="Empty field: email")
        return
    
    if password == "":
        messagebox.showinfo(title="Info", message="Empty field: password")
        return
    
    ansbtn = messagebox.askyesno(title=website_name, message=f"These are the details entered: \nEmail:{user_email}"
                        f"\nPassword: {password}\nIs it ok to save")
    
    if not ansbtn:
        return

    data = f"{website_name} | {user_email} | {password}\n"

    with open('password.txt', 'a') as f:
        f.write(data)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0, columnspan=2)

label_1 = Label()
label_1.config(text="Website:")
label_1.grid(column=0, row=1)
label_2 = Label()
label_2.config(text="Email/Username:")
label_2.grid(column=0, row=2)
label_3 = Label()
label_3.config(text="Password:")
label_3.grid(column=0,row=3)


website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1)
username_entry.insert(index=END, string="sample@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

generate_btn = Button()
generate_btn.config(text="Generate Password", command=generate_password)
generate_btn.grid(column=3, row=3)
add_btn = Button(width=45)
add_btn.config(text="Add", command=save_password)
add_btn.grid(column=1, row=4, columnspan=3)


window.mainloop()