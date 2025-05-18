import tkinter
import tkinter.messagebox
import random
screen=tkinter.Tk()
screen.geometry("400x400")
screen.title("number game")
a=random.randint(1,10)
def f1():
    global a
    b=int(entry1.get())
    if a>b :
        tkinter.messagebox.showerror(title="game",message="higher")
    if a<b :
        tkinter.messagebox.showerror(title="game",message="lower")
    if a==b :
        tkinter.messagebox.showinfo(title="game",message="you win")

label2=tkinter.Label(screen,text="welcome to number gessing game",width=28,height=2,fg="black",padx=1,pady=1)
label3=tkinter.Label(screen,text="put youre geuse",width=12,height=2,fg="black",padx=1,pady=1)
entry1=tkinter.Entry(screen)
button1=tkinter.Button(screen,text="comfirm",command=f1)
label3.grid(row=2,column=1)
entry1.grid(row=2,column=2)
button1.grid(row=2,column=3)
label2.grid(row=1,column=1,columnspan=3)

screen.mainloop()