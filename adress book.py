import tkinter
import tkinter.filedialog
import tkinter.messagebox
screen=tkinter.Tk()
screen.geometry("600x500")
screen.title("adress book")
info={}
def f1():
    name=entery1.get()
    adress=entery2.get()
    mobile=entery3.get()
    email=entery4.get()
    birthday=entery5.get()
    info[name]=[adress,mobile,email,birthday]
    entery1.delete(0,tkinter.END)
    entery2.delete(0,tkinter.END)
    entery3.delete(0,tkinter.END)
    entery4.delete(0,tkinter.END)
    entery5.delete(0,tkinter.END)
    print(info)
    uppdatelistbox()
def uppdatelistbox():
    list_box1.delete(0,tkinter.END)
    keys=info.keys()
    for key in keys:
        list_box1.insert(tkinter.END,key)
def f2():
    b=list_box1.curselection()
    name=list_box1.get(b)
    del info [name]
    uppdatelistbox()
def f3():
    file1=tkinter.filedialog.asksaveasfile()
    if file1 is not None :
        print(info,file=file1)
def f4():
    global info
    file1=tkinter.filedialog.askopenfile()
    if file1 is not None :
        a=file1.read()
        info=eval(a)
        uppdatelistbox()
def f5():
    q=list_box1.curselection()
    name=list_box1.get(q)
    values=info[name]
    entery1.insert(tkinter.END,name)
    entery2.insert(tkinter.END,values[0])
    entery3.insert(tkinter.END,values[1])
    entery4.insert(tkinter.END,values[2])
    entery5.insert(tkinter.END,values[3])
def display(event):
    q=list_box1.curselection()
    name=list_box1.get(q)
    values=info[name]
    
    mesege="name:"+name+"\nadress:"+values[0]+"\nmobile:"+values[1]+"\ne maill:"+values[2]+"\nbirthday:"+values[3]
    tkinter.messagebox.showinfo(title="adress book",message=mesege)
list_box1=tkinter.Listbox(screen,font=("courier 20 normal"))
button1=tkinter.Button(screen,text="open",command=f4)
button2=tkinter.Button(screen,text="edit",command=f5)
button3=tkinter.Button(screen,text="delete",command=f2)
button4=tkinter.Button(screen,text="save",command=f3)
button5=tkinter.Button(screen,text="uppdate/add",command=f1)
label1=tkinter.Label(screen,text="adress book")
label2=tkinter.Label(screen,text="name:")
label3=tkinter.Label(screen,text="adress:")
label4=tkinter.Label(screen,text="mobile:")
label5=tkinter.Label(screen,text="email:")
label6=tkinter.Label(screen,text="birth day:")
entery1=tkinter.Entry(screen)
entery2=tkinter.Entry(screen)
entery3=tkinter.Entry(screen)
entery4=tkinter.Entry(screen)
entery5=tkinter.Entry(screen)
list_box1.bind("<<ListboxSelect>>",display)
label1.grid(row=1,column=2)
label2.grid(row=2,column=3)
label3.grid(row=3,column=3)
label4.grid(row=4,column=3)
label5.grid(row=5,column=3)
label6.grid(row=6,column=3)
entery1.grid(row=2,column=4)
entery2.grid(row=3,column=4)
entery3.grid(row=4,column=4)
entery4.grid(row=5,column=4)
entery5.grid(row=6,column=4)
button1.grid(row=1,column=3)
button2.grid(row=8,column=1)
button3.grid(row=8,column=2)
button4.grid(row=8,column=4)
button5.grid(row=8,column=3)
list_box1.grid(row=2,column=1,columnspan=2,rowspan=6)

screen.mainloop()



# Make a app, where the Listbox is populated with various colours. The user can select one of them and depending upon the colour selected the background of the window should change. You should be able to add more colours or remove from the list.