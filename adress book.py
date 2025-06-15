import tkinter
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
    print(info)
    uppdatelistbox()
def uppdatelistbox():
    list_box1.delete(0,tkinter.END)
    keys=info.keys()
    for key in keys:
        list_box1.insert(tkinter.END,key)


list_box1=tkinter.Listbox(screen,font=("courier 20 normal"))
button1=tkinter.Button(screen,text="open",command=f1)
button2=tkinter.Button(screen,text="edit",command=f1)
button3=tkinter.Button(screen,text="delete",command=f1)
button4=tkinter.Button(screen,text="save",command=f1)
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