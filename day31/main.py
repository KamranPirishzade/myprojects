BACKGROUND_COLOR = "#B1DDC6"
import random
from tkinter import *
import pandas
dict={}
try:
    dk=pandas.read_csv("data/must_learn.csv")
except FileNotFoundError:
    origin_data=pandas.read_csv("data/french_words.csv")
    dict=origin_data.to_dict(orient="records")
else:
    dict=dk.to_dict(orient="records")


current_card={}



def reset():

    global timer,current_card
    current_card=random.choice(dict)
    window.after_cancel(timer)
    canvas.itemconfig(old_side,image=old_image)
    canvas.itemconfig(french_lab, text=current_card["French"],fill="black")
    canvas.itemconfig(language,text="French",fill="black")
    timer=window.after(3000, func=new_side)

def new_side():
    canvas.itemconfig(old_side,image=new_image)
    canvas.itemconfig(french_lab,text=current_card["English"],fill="white")
    canvas.itemconfig(language,text="English",fill="white")



def is_known():
    dict.remove(current_card)
    data=pandas.DataFrame(dict)
    data.to_csv("data/must_learn.csv",index=False)
    reset()









window=Tk()
window.config(pady=50,padx=50,bg="#B1DDC6")
window.title("Flashy")
my_image = PhotoImage(file="images/right.png")
button = Button(image=my_image, highlightthickness=0,bg="#B1DDC6",command=is_known)
button.grid(row=2,column=2)
x_image=PhotoImage(file="images/wrong.png")
buttonx=Button(image=x_image,highlightthickness=0,bg="#B1DDC6",command=reset)
timer=window.after(3000,func=new_side)
buttonx.grid(row=2,column=1)
old_image=PhotoImage(file="images/card_front.png")
new_image=PhotoImage(file="images/card_back.png")
canvas=Canvas(width=800,height=526,highlightthickness=0,bg="#B1DDC6")
old_side=canvas.create_image(400,263,image=old_image)
language=canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
french_lab=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(row=1,column=1,columnspan=2)
reset()




















# label_lan=Label(text="French",font=("Ariel",40,"italic"))
# label_lan.place(x=300,y=150)
# label_word=Label(text="Word",font=("Ariel",60,"bold"))
# label_word.place(x=300,y=263)



































window.mainloop()

