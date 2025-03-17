from tkinter import *
THEME_COLOR = "#375362"

class QuestInterface():
    def __init__(self, quiz_brain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title = "Quiz App"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label()
        self.score.config(text="Score: 0", bg=THEME_COLOR, font=("Arial", 13, 'bold'), fg='white')
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.content = self.canvas.create_text(150, 125, text="Kanye Quote Goes HERE", width=290, font=("Arial", 15, "bold"), fill="black")
        self.canvas.grid(row=1,column=0, columnspan=2, pady=20)

        self.image_check = PhotoImage(file ="./images/true.png")
        self.image_wrong = PhotoImage(file ="./images/false.png")

        self.btn_check = Button(image=self.image_check, pady=20, padx=20, command=self.btn_check_click)
        self.btn_check.grid(row=2, column=0)
        self.btn_wrong = Button(image=self.image_wrong, pady=20, padx=20, command=self.btn_wrong_click)
        self.btn_wrong.grid(row=2, column=1)

        self.ask_question()

        self.window.mainloop()

    def ask_question(self):
        q_n = self.quiz_brain.get_question_number()
        if(q_n >= 10):
            self.canvas.itemconfig(self.content, text="Youve answered all the questions.")
            return

        self.canvas.config(bg='white')
        text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.content, text=text)
        self.score.config(text=f"Score : {self.quiz_brain.get_score()}")

    def btn_check_click(self):
        if self.quiz_brain.check_answer("true"):
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.ask_question)


    def btn_wrong_click(self):
        if self.quiz_brain.check_answer("false"):
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.ask_question)