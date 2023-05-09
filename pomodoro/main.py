from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    global reps
    reps=0
    check_mark.config(text="")
    label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_txt,text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break)
        label.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_break)
        label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work",fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    min=count//60
    sec=count%60
    if sec<10 :
        sec=(f"0{sec}")



    if count >= 0:
        canvas.itemconfig(timer_txt,text=f"{min}:{sec}")
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        cor=reps//2
        check_mark.config(text="✔"*cor)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(pady=200,padx=200,bg=YELLOW)


label=Label(text="Timer",font=("Courier",40,"bold"),fg=GREEN,bg=YELLOW)
label.grid(column=2,row=2)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
pomodoro_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=pomodoro_img)
canvas.grid(column=2,row=3)
timer_txt=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,20,"bold"))

button_start=Button(text="Start",highlightthickness=0,command=start_timer)
button_start.grid(column=1,row=4)
button_reset=Button(text="Reset",highlightthickness=0,command=reset)
button_reset.grid(column=3,row=4)
check_mark=Label(fg=GREEN,font=(FONT_NAME,10,"bold"),bg=YELLOW)
check_mark.grid(column=2,row=5)














window.mainloop()