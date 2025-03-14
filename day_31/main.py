from tkinter import *
import json
import random
BACKGROUND_COLOR = "#B1DDC6"

_learned_data = []
_sched_id = 0
_current_key = ""
_saved = False

# GET DATA AND CHANGED DATA

try: 
    with open("user.txt", mode="r", encoding="utf8") as f:
        content = f.readlines()

        for item in content:
            _learned_data.append(item.strip())

except:
    _learned_data = []


try:
    with open("data.json", mode="r", encoding="utf8") as f:
        content = json.load(f)

        data = {}
        for item in content:
            if item not in _learned_data:
                data[item] = {"translation" : content[item]["translation"]}

except:
    data = {}


# SAVE DATA

def saved_data():
    global _learned_data
    print("save")

    with open("user.txt", mode="a", encoding="utf8") as f:
        for item in _learned_data:
            f.write(item + "\n")

    windows.destroy()

# SET START

def reset_view():
    global _current_key, _saved, _learned_data

    if _saved:
        _learned_data.append(_current_key)

    if not _saved:
        _saved = True
    
    listKeys = list(data.keys())
    _current_key = random.choice(listKeys)

    canvas.itemconfig(top_text, text="Japanese")
    canvas.itemconfig(bottom_text, text=f"{_current_key}")
    canvas.itemconfig(view_image, image=resize_f)

# BUTTON CLICK


def wrong_btn_click():
    global _sched_id, _current_key, _saved

    translate = data[_current_key]['translation']
    canvas.itemconfig(top_text, text="Translation")
    canvas.itemconfig(bottom_text, text=f"{translate}")
    canvas.itemconfig(view_image, image=resize_b)

    _saved = False
    _sched_id = windows.after(3000, reset_view)


# UI 

windows = Tk()
windows.title("Flash Card Japanese")
windows.config(padx=20, pady=20, bg=BACKGROUND_COLOR)


canvas = Canvas(width=400, height=263, bg=BACKGROUND_COLOR, highlightthickness=0)


front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
check_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

resize_f = front_img.subsample(2, 2)
resize_b = back_img.subsample(2, 2)
resize_check = check_img.subsample(2, 2)
resize_wrong = wrong_img.subsample(2, 2)

view_image = canvas.create_image(200, 131, image=resize_f)
top_text = canvas.create_text(200, 90, text="Start Learning", font=('Arial', 20, 'italic'))
bottom_text = canvas.create_text(200, 140, text="Japanese", font=('Arial', 20, 'italic'))
canvas.grid(row=0, column=0, columnspan=2)

btn_check = Button(image=resize_check, bg=BACKGROUND_COLOR, borderwidth=1, command=reset_view)
btn_check.grid(row=1, column=0)
btn_wrong = Button(image=resize_wrong, bg=BACKGROUND_COLOR, borderwidth=1, command=wrong_btn_click)
btn_wrong.grid(row=1, column=1)


windows.protocol("WM_DELETE_WINDOW", saved_data)
windows.mainloop()