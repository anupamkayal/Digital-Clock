from tkinter import *
import  time

root=Tk()
root.title("digital clock")
root.geometry("630x190")
def clock():
    current_time=time.strftime("%I:%M:%S")
    display["text"]=current_time
    display.after(100,clock)
display=Label(root,font=("arial",  38,"bold"),fg="red",bg="black")

display.pack()
clock()
root.mainloop()