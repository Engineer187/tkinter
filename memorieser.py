import tkinter
import tkinter.filedialog
screen=tkinter.Tk()
screen.geometry("400x500")
screen.title("notes")
def f1 ():
    pass
def f2 ():
    b=list_box1.curselection()
    list_box1.delete(b)
def f3 ():
    file1=tkinter.filedialog.asksaveasfile()
    if file1 is not None:
        for item in list_box1.get(0,tkinter.END):
            print(item.strip(),file=file1)
def f4 ():
    a=Entrey1.get()
    list_box1.insert(tkinter.END,a)
    Entrey1.delete(0,tkinter.END)
Entrey1=tkinter.Entry(screen,font=("courier 17 normal"))
button1=tkinter.Button(screen,text="open",command=f1,font=("courier 25 normal"))
button2=tkinter.Button(screen,text="delete",command=f2,font=("courier 25 normal"))
button3=tkinter.Button(screen,text="save",command=f3,font=("courier 25 normal"))
button4=tkinter.Button(screen,text="add",command=f4,font=("courier 25 normal"))
list_box1=tkinter.Listbox(screen,font=("courier 20 normal"))
Entrey1.grid(row=2,column=1,columnspan=2)
button1.grid(row=1,column=1)
button2.grid(row=1,column=2)
button3.grid(row=1,column=3)
button4.grid(row=2,column=3)
list_box1.grid(row=3,column=1,columnspan=3)




screen.mainloop()