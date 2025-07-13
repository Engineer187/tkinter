import tkinter
import tkinter.messagebox
import random
screen=tkinter.Tk()
screen.geometry("450x360")
screen.title("adress book")
def f1(userslected):
    if userslected in buttons:
        userslected.config(text="X")
        buttons.remove(userslected)
        check()
        button=random.choice(buttons)
        button.config(text="O")
        buttons.remove(button)
        check()
def check():
    for i in win:
        if i[0]["text"]=="X" and i[1]["text"]=="X" and i[2]["text"]=="X" :
            tkinter.messagebox.showinfo(title="tick tack toe",message="you win")
        if i[0]["text"]=="O" and i[1]["text"]=="O" and i[2]["text"]=="O" :
            tkinter.messagebox.showinfo(title="tick tack toe",message="you lost")
    if len(buttons)==0:
        tkinter.messagebox.showinfo(title="tick tack toe",message="tie")
        
        
buttonRU=tkinter.Button(screen,text="",width=20,height=6,command=lambda:f1(buttonRU))
buttonCU=tkinter.Button(screen,text="",width=20,height=6,command=lambda:f1(buttonCU))
buttonLU=tkinter.Button(screen,text="",width=20,height=6,command=lambda:f1(buttonLU))
buttonRC=tkinter.Button(screen,text="",width=20,height=6,command=lambda:f1(buttonRC))
buttonCC=tkinter.Button(screen,text="",width=20,height=6,command=lambda:f1(buttonCC))
buttonLC=tkinter.Button(screen,text="",width=20,height=6,command=lambda:f1(buttonLC))
buttonRD=tkinter.Button(screen,text="",width=20,height=6,command=lambda:f1(buttonRD))
buttonCD=tkinter.Button(screen,text="",width=20,height=6,command=lambda:f1(buttonCD))
buttonLD=tkinter.Button(screen,text="",width=20,height=6,command=lambda:f1(buttonLD))
win=[[buttonRU,buttonCU,buttonLU],[buttonRC,buttonCC,buttonLC],[buttonRD,buttonCD,buttonLD],[buttonRU,buttonRC,buttonRD],[buttonCU,buttonCC,buttonCD],[buttonLU,buttonLC,buttonLD],[buttonRU,buttonCC,buttonLD],[buttonLU,buttonCC,buttonRD]]

buttonRU.grid(row=1,column=3)
buttonCU.grid(row=1,column=2)
buttonLU.grid(row=1,column=1)
buttonRC.grid(row=2,column=3)
buttonCC.grid(row=2,column=2)
buttonLC.grid(row=2,column=1)
buttonRD.grid(row=3,column=3)
buttonCD.grid(row=3,column=2)
buttonLD.grid(row=3,column=1)
buttons=[buttonRU,buttonCU,buttonLU,buttonRC,buttonCC,buttonLC,buttonRD,buttonCD,buttonLD]

screen.mainloop()