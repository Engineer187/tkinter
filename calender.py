import tkinter
import calendar
screen=tkinter.Tk()
screen.geometry("400x400")
screen.title("calender")
label1=tkinter.Label(screen,text="calender",width=10,height=2,bg="red",fg="black",padx=100,pady=10)
label2=tkinter.Label(screen,text="enter year")
entry1=tkinter.Entry(screen)
def f1():
    screen1=tkinter.Tk()
    screen1.geometry("800x800")
    screen1.title("calender")
    text1=tkinter.Text(screen1)
    text1.pack()
    year=int(entry1.get())
    calendartext=calendar.calendar(year)
    text1.insert(tkinter.END,calendartext)




    screen1.mainloop()
button1=tkinter.Button(screen,text="hi",command=f1)
label1.pack()
entry1.pack()
button1.pack()
screen.mainloop()