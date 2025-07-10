from tkinter import * 

seconds_elapsed = 0
time_start = False

window = Tk()
window.title("Dangerous Notes")
window.maxsize(width=500, height=300)


text_area = Text(height=200, width=300, padx=10, pady=10)


time_label = Label(text="0", width=20, font=("Courier", 14))

def on_key_release(event):
    global CURRENT_N, seconds_elapsed, time_start

    seconds_elapsed = 10
    if not time_start:
        time_start = True
        update_time()



def update_time():
    global seconds_elapsed
    seconds_elapsed -= 1

    time_label.config(text=str(seconds_elapsed))
    if seconds_elapsed != 0:
        window.after(1000, update_time)
    else:
        text_content = text_area.get("1.0", END).strip()  # get all text, without last newline
        text_area.delete("1.0", END)
        time_start = False
        window.clipboard_clear()
        window.clipboard_append(text_content)
        window.update()
    
    
text_area.bind("<KeyRelease>", on_key_release)

time_label.pack()
text_area.pack()
window.mainloop()