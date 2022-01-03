from tkinter import *
from tkinter import ttk
import random

win= Tk()

win.geometry("750x450")

win.title("Rock Paper Scissors...")

computer_options = {
   "0":"Rock",
   "1":"Paper",
   "2":"Scissor"
}

def button_disable():
   b1.config(state= "disabled")
   b2.config(state= "disabled")
   b3.config(state= "disabled")

def isrock():
   value = computer_options[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "Match Draw"
   elif value=="Scissor":
      match_result = "SHEEEEEEESH"
   else:
      match_result = "Computer Win"
   label.config(text = match_result)
   l1.config(text = "Rock")
   l3.config(text =value)
   button_disable()

def ispaper():
   value = computer_options[str(random.randint(0, 2))]
   if value == "Paper":
      match_result = "Match Draw"
   elif value=="Scissor":
      match_result = "Computer Win"
   else:
      match_result = "You won, no cap!"
   label.config(text = match_result)
   l1.config(text = "Paper")
   l3.config(text = value)
   button_disable()

def isscissor():
   value = computer_options[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "Computer Win"
   elif value == "Scissor":
      match_result = "Match Draw"
   else:
      match_result = "Booooooom!"
   label.config(text = match_result)
   l1.config(text = "Scissor")
   l3.config(text = value)
   button_disable()

def reset():
   b1.config(state= "active")
   b2.config(state= "active")
   b3.config(state= "active")
   l1.config(text = "Player")
   l3.config(text = "Computer")
   label.config(text = "")

labelframe= LabelFrame(win, text= "Rock Paper Scissor", font= ('Century 20 bold'),labelanchor= "n",bd=5,bg= "skyblue",width= 600, height= 450, cursor= "target")
labelframe.pack(expand= True, fill= BOTH)

l1= Label(labelframe, text="Player", font= ('Calibri'))
l1.place(relx= .18, rely= .1)

l2= Label(labelframe, text="VS", font= ('Calibri'), bg="pink")
l2.place(relx= .45, rely= .1)

l3= Label(labelframe, text="Computer", font= ('Calibri'))
l3.place(relx= .65, rely= .1)

label= Label(labelframe, text="", font=('Coveat', 25,'bold'), bg= "skyblue")
label.pack(pady=150)

b1= Button(labelframe, text= "Rock", font= 10, width= 7, command= isrock)
b1.place(relx=.25, rely= .62)
b2= Button(labelframe, text= "Paper", font= 10, width= 7 ,command= ispaper)
b2.place(relx= .41,rely= .62)
b3= Button(labelframe, text= "Scissor", font= 10, width= 7, command= isscissor)
b3.place(relx= .58, rely= .62)

reset= Button(labelframe, text= "Reset",bg= "Orange", fg= "white",width= 7, font= 10, command= reset)
reset.place(relx= .8, rely= .62)
win.mainloop()
