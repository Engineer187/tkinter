import tkinter
import tkinter.ttk
screen=tkinter.Tk()
screen.geometry("400x400")
screen.title("number game")
c=0
def f1():
    global c
    tabele=""
    n=int(combo_box1.get())
    m=int(mutiples.get())
    for i in range(m):
        c=c+1
        a=n*c
        tabele=tabele+str(n)+"x"+str(c)+"="+str(a)+"\n"
    label3.config(text=tabele)
label1=tkinter.Label(screen,text="welcome to time tabel solver",width=28,height=2,fg="black",padx=1,pady=1)
label2=tkinter.Label(screen,text="put youre number",width=12,height=2,fg="black",padx=1,pady=1)
label3=tkinter.Label(screen,text="",fg="black",padx=1,pady=1)
mutiples=tkinter.IntVar()
mutiples.set(0)
raidobotton1=tkinter.Radiobutton(screen,text="10",variable=mutiples,value=10)
raidobotton2=tkinter.Radiobutton(screen,text="20",variable=mutiples,value=20)
raidobotton3=tkinter.Radiobutton(screen,text="30",variable=mutiples,value=30)
combo_box1=tkinter.ttk.Combobox(screen)
number=[]
for i in range (1,51,1):
    number.append(i)
combo_box1["values"]=number
button1=tkinter.Button(screen,text="comfirm",command=f1)
label2.grid(row=2,column=1)
label3.grid(row=3,column=2)
combo_box1.grid(row=2,column=2)
button1.grid(row=2,column=3)
raidobotton1.grid(row=2,column=4)
raidobotton2.grid(row=3,column=4)
raidobotton3.grid(row=4,column=4)
button1.grid(row=2,column=3)
label1.grid(row=1,column=1,columnspan=3)

screen.mainloop()