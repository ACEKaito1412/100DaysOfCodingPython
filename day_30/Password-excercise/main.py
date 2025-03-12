from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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

    new_data = {
        website_name.lower() : {
            "email" : user_email,
            "password" : password
        }
    }

    try:
        with open('password.json', 'r') as f:
            data = json.load(f)
            data.update(new_data)
    except:
        with open('password.json', 'w') as f:
            json.dump(new_data, f, indent=5)
    else:
        with open('password.json', 'w') as f:
            json.dump(data, f, indent=5)


    website_entry.delete(0, END)
    password_entry.delete(0, END)
    pyperclip.copy(password)


# ---------------------------- Search ------------------------------- #

def search_website():
     website = website_entry.get()
     if website == "":
         messagebox.showinfo("Empty", message="Empty search term")
         return
     
     with open('password.json', 'r') as f:
            data = json.load(f)
            try:
                saved_data = data[website.lower()]
                messagebox.showinfo(website.capitalize(), message=f"User Email: {saved_data['email']}\nPassword:{saved_data['password']}" )
            except:
                messagebox.showinfo(website.capitalize, message="No password save for this website.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0, columnspan=2)

label_1 = Label()
label_1.config(text="Website:", justify="right")
label_1.grid(column=0, row=1)
label_2 = Label()
label_2.config(text="Email/Username:", justify="right")
label_2.grid(column=0, row=2)
label_3 = Label()
label_3.config(text="Password:", justify="right")
label_3.grid(column=0,row=3)


website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1)
username_entry.insert(index=END, string="sample@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)


search_btn = Button(width=15)
search_btn.config(text="Search Website", command=search_website)
search_btn.grid(column=3, row=1)

generate_btn = Button(width=15)
generate_btn.config(text="Generate Password", command=generate_password)
generate_btn.grid(column=3, row=3)
add_btn = Button(width=46)
add_btn.config(text="Add", command=save_password)
add_btn.grid(column=1, row=4, columnspan=3)


window.mainloop()