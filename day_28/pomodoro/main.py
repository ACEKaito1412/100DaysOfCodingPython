from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
_reps = 1
_sched_id = ""

# ---------------------------- FOCUS TAB ---------------------------------- # 


def bring_to_front():
    window.deiconify()  # Restore if minimized
    window.wm_state("normal")  # Ensure it's not minimized
    window.lift()  # Bring to front
    window.focus_force()  # Force focus
    window.attributes('-topmost', True)  # Make it topmost
    window.attributes('-topmost', False)  # Allow other windows on top later



# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global _reps
    _reps = 1
    window.after_cancel(_sched_id)
    canvas.itemconfig(timer_text, text=f"00:00")
    label_check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global _reps, _sched_id
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if _sched_id != "":
        window.after_cancel(_sched_id)

    timer = 0
    if _reps == 8:
        timer = long_break_sec
        label.config(text="BREAK", fg=RED)
    elif _reps % 2 == 1:
        timer = work_sec
        label.config(text="WORK", fg=GREEN)
    else:
        label.config(text="BREAK", fg=PINK)
        timer = short_break_sec

    countdown_mechanism(timer)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_mechanism(count):
    global _reps, _sched_id

    mins = math.floor(count / 60)
    secs = count  % 60

    if secs >= 0 and secs < 10:
        secs = "0" + str(secs)

    if mins >= 0 and mins < 10:
        mins = "0" + str(mins)

    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        _sched_id = window.after(1000, countdown_mechanism, count - 1)
    elif count <= 0 and _reps < 10:
        _reps += 1
        bring_to_front()
        start_timer()

        mark = ""
        work_sessions = math.floor(_reps / 2)
        for _ in range(work_sessions):
            mark += "✓"
        
        label_check.config(text=mark)

    else:
        reset_timer()
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


btn_start = Button(text="Start", font=(FONT_NAME, 15, "bold"), padx=5, pady=5, border=1, command=start_timer)
btn_start.grid(column=0, row=2)


label_check = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN)
label_check.grid(column=1, row=2)


btn_reset = Button(text="Reset", font=(FONT_NAME, 15, "bold"), padx=5, pady=5, border=1, command=reset_timer)
btn_reset.grid(column=2, row=2)



window.mainloop()