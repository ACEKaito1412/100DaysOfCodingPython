from tkinter import * 

window = Tk()
window.title("Typer Wiser")
window.minsize(width=400, height=300)


text = "Time flies fast, so type with skill. Focus sharp, mind clear. Hands move quick, never miss beats. Train daily, grow strong. Aim high, stay calm. Space, dots, and lines count too. Keep pace, don’t rush. One key wrong could cost more. Practice, repeat, improve each day. Sharp eyes read fast, brain reacts smooth. Click keys like art, rhythm in hand. Beat fear, trust flow. Be cool, stay in sync. Eyes ahead, hands glide. Each tap counts, make it clean. Move left, jump right. Trust your feel, aim true. One slip, fix quick. Stay chill, win more. Keep calm, type on."

CURRENT_N = 0
split_text = text.split(" ")
user_text = []
seconds_elapsed = 60
time_start = False

#Labels
label_1 = Label(text="This", width=20, font=("Courier", 14))
label_1.grid(column=0, row=0, columnspan=3)

label_2 = Label(text="is", width=20, font=("Courier", 14))
label_2.grid(column=0, row=1)

label_3 = Label(text="old", width=20, font=("Courier", 14))
label_3.grid(column=1, row=1)

label_4 = Label(text="text", width=20, font=("Courier", 14))
label_4.grid(column=2, row=1)

label_5 = Label(text="from", width=20, font=("Courier", 14))
label_5.grid(column=0, row=2, columnspan=2)

label_6 = Label(text="one", width=20, font=("Courier", 14))
label_6.grid(column=1, row=2, columnspan=2)

label_7 = Label(text="gaurdian", width=20, font=("Courier", 18, "bold"))
label_7.grid(column=0, row=3, columnspan=3)

input_text = Entry(justify='center', font=("Courier", 18, "bold"))
input_text.grid(column=0, row=4, columnspan=3)

time_label = Label(text=f"Timer: {str(seconds_elapsed)}", font=("Arial", 14))
time_label.grid(column=0, row=5, columnspan=5, pady=4)

wpm_label = Label(text="Word Per Minute", font=("Arial", 12))
wpm_label.grid(column=0, row=6, columnspan=5)

wpm_score = Label(text="0", font=("Arial", 54))
wpm_score.grid(column=0, row=7, columnspan=5)


def on_key_release(event):
    global CURRENT_N, user_text, time_start
    user_input = input_text.get()
    key_name = event.keysym

    if key_name == "space":
        input_text.delete(0, END)
        user_text.append(user_input)
        CURRENT_N += 1
        change_text()

        if time_start == False:
            time_start = True
            update_time()


input_text.bind("<KeyRelease>", on_key_release)


list_label = [label_7, label_6, label_5, label_4, label_3, label_2, label_1] 
list_label_2 = [label_1, label_2, label_3, label_4, label_5, label_6, label_7] 

def change_text():
    global CURRENT_N, list_label
    for i in range(len(list_label)):
        texts = split_text[CURRENT_N: 7 + CURRENT_N]
        label = list_label[i]
        label.config(text=texts[i])

def update_time():
    global seconds_elapsed
    seconds_elapsed -= 1

    time_label.config(text=str(seconds_elapsed))
    if seconds_elapsed != 0:
        window.after(1000, update_time)
    else:
        check_wpm()

def check_wpm():
    global user_text, text, CURRENT_N, time_start

    char_count = len(user_text)
    for item in user_text:
        char_count += len(item)

    for i in range(len(user_text)):
        if user_text[i] != text[i]:
            char_count -= len(text[i])
    
    wpm = round(char_count / 5)
    
    wpm_score.config(text=str(wpm))
    seconds_elapsed = 60
    CURRENT_N = 0
    time_label.config(text=str(seconds_elapsed))
    time_start = False
    change_text()
    pass

change_text()
window.mainloop()