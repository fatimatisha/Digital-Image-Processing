from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

window = Tk()
window.resizable()
window.geometry("800x800")
window.title('DIP Application')
Label(window,text="Image Viewer Application after and before using filter",font=('bold',20)).pack(pady=20)


frame=Frame(window, width=230, height=200, bg='white')
frame.pack(pady=20)


image1=ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\DIP_Python\Dataset\misc\\4.1.04.tiff"))
image2=ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\DIP_Python\Dataset\misc\\4.1.01.tiff"))
image3=ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\picture\\3-c3.png"))
image4=ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\picture\\3-e2.png"))
image5=ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\picture\\3-g2.png"))
image6=ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\picture\\2-c.png"))
image7=ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\picture\\2-c2.png"))


lst=[image1,image2,image3,image4,image5,image6,image7]
i = 0
image_label = Label(frame, image=lst[i])
image_label.pack()

def Back():
    global i
    i = i - 1
    try:
        image_label.config(image=lst[i])
    except:
        i = 0
        Back()
def Next():
    global i
    i = i + 1
    try:
        image_label.config(image=lst[i])
    except:
        i = -1
        Next()

#creating buttons
Button(window,text='Back',command=Back,bg='light blue').place(x=230,y=200)
Button(window,text='Next',command=Next,bg='light blue').place(x=1000,y=200)
button_exit = Button(window,text="exit",command=window.destroy).place(x=500,y=600)

window.mainloop()
