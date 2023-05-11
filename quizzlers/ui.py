THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain






class QuizInterface():
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.title("Quizzler")
        self.score=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score.grid(row=0,column=2)
        self.canvas=Canvas(height=250,width=300)
        self.canvas.grid(row=1,column=1,columnspan=2,padx=20,pady=20)
        self.txt=self.canvas.create_text(150,125,width=280,text="Question",font=("Arial",20,"italic"))
        true_image=PhotoImage(file="images/true.png")
        false_image=PhotoImage(file="images/false.png")
        self.button_t=Button(image=true_image,command=self.true_check)
        self.button_f=Button(image=false_image,command=self.false_check)
        self.button_f.grid(row=2,column=2)
        self.button_t.grid(row=2,column=1)
        self.next()

        self.window.mainloop()

    def next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score:{self.quiz.score}")
            new_question=self.quiz.next_question()
            self.canvas.itemconfig(self.txt,text=new_question)
        else:
            self.canvas.itemconfig(self.txt,text="You have reached enf of quiz.")
            self.button_f.config(state="disabled")
            self.button_t.config(state="disabled")
    def true_check(self):
        is_true=self.quiz.check_answer(user_answer="True")
        self.feedback(is_true)
        self.window.after(1000,self.next)


    def false_check(self):
        is_true=self.quiz.check_answer(user_answer="False")
        self.feedback(is_true)
        self.window.after(1000,self.next)

    def feedback(self,is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")


