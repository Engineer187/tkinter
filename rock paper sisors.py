import tkinter
import random
pc=0
player=0
screen=tkinter.Tk()
screen.geometry("500x300")
screen.title("game")
label2=tkinter.Label(screen,text="rock paper scissors",width=12,height=2,fg="black",padx=5,pady=10)
label3=tkinter.Label(screen,text="",width=12,height=2,fg="black",padx=5,pady=10)
label4=tkinter.Label(screen,text="you're options:",width=12,height=2,fg="black",padx=5,pady=10)
label5=tkinter.Label(screen,text="score:",width=12,height=2,fg="black",padx=5,pady=10)
label6=tkinter.Label(screen,text="youre score:",width=12,height=2,fg="black",padx=5,pady=10)
label7=tkinter.Label(screen,text="",width=12,height=2,fg="black",padx=5,pady=10)
label8=tkinter.Label(screen,text="pc score:",width=12,height=2,fg="black",padx=5,pady=10)
label9=tkinter.Label(screen,text="",width=12,height=2,fg="black",padx=5,pady=10)
label10=tkinter.Label(screen,text="you selected :",width=12,height=2,fg="black",padx=5,pady=10)
label11=tkinter.Label(screen,text="",width=12,height=2,fg="black",padx=5,pady=10)
label12=tkinter.Label(screen,text="pc selected :",width=12,height=2,fg="black",padx=5,pady=10)
label13=tkinter.Label(screen,text="",width=12,height=2,fg="black",padx=5,pady=10)
def f1():
    global pc,player
    a=random.randint(1,3)
    if a==1 :
        label11.config(text="rock")
        label13.config(text="rock")
        label3.config(text="tie")
    if a==2 :
            label11.config(text="rock")
            label13.config(text="paper")
            label3.config(text="pc win")
            pc=pc+1
            label9.config(text=pc)
    if a==3 :
            label11.config(text="rock")
            label13.config(text="scissors")
            label3.config(text="you win")
            player=player+1
            label7.config(text=player)
def f2():
    global pc,player
    a=random.randint(1,3)
    if a==1 :
        label11.config(text="paper")
        label13.config(text="rock")
        label3.config(text="you win")
        player=player+1
        label7.config(text=player)
    if a==2 :
            label11.config(text="paper")
            label13.config(text="paper")
            label3.config(text="tie")
    if a==3 :
            label11.config(text="paper")
            label13.config(text="scissors")
            label3.config(text="pc win")
            pc=pc+1
            label9.config(text=pc)
def f3():
    global pc,player
    a=random.randint(1,3)
    if a==1 :
        label11.config(text="scissors")
        label13.config(text="rock")
        label3.config(text="pc win")
        pc=pc+1
        label9.config(text=pc)
    if a==2 :
        label11.config(text="scissors")
        label13.config(text="paper")
        label3.config(text="you win")
        player=player+1
        label7.config(text=player)
    if a==3 :
        label11.config(text="scissors")
        label13.config(text="scissors")
        label3.config(text="tie")
button1=tkinter.Button(screen,text="rock",fg="black",bg="red",command=f1)
button2=tkinter.Button(screen,text="paper",fg="black",bg="grey",command=f2)
button3=tkinter.Button(screen,text="scissors",fg="black",bg="blue",command=f3)
label2.grid(row=1,column=3)
label3.grid(row=2,column=3)
label4.grid(row=3,column=1)
label5.grid(row=4,column=1)
label6.grid(row=4,column=2)
label7.grid(row=4,column=3)
label8.grid(row=4,column=4)
label9.grid(row=4,column=5)
label10.grid(row=5,column=2)
label11.grid(row=5,column=3)
label12.grid(row=5,column=4)
label13.grid(row=5,column=5)
button1.grid(row=3,column=2)
button2.grid(row=3,column=3)
button3.grid(row=3,column=4)
screen.mainloop()