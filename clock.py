import tkinter
import time
screen=tkinter.Tk()
screen.geometry("300x100")
screen.title("clock")
def timechecker():
    timetext=time.strftime("%H:%M:%S:%p")
    label1.config(text=timetext)
    label1.after(1000,timechecker)
label1=tkinter.Label(screen,text="",width=10,height=2,bg="red",fg="black",font=["arial",40,"normal"])
label1.pack()
timechecker()








screen.mainloop()