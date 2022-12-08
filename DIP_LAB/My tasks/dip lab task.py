from tkinter import *
from PIL import ImageTk, Image


win = Tk()
win.iconbitmap

win.geometry("700x500")
win.title('Image Application')
frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img1 = ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\DIP_Python\Dataset\misc\\4.1.04.tiff"))
img2 = ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\DIP_Python\Dataset\misc\\4.1.06.tiff"))
img3 = ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\DIP_Python\Dataset\misc\\4.2.07.tiff"))
img4 = ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\DIP_Python\Dataset\misc\\4.1.03.tiff"))
img5 = ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\DIP_Python\Dataset\misc\\4.1.01.tiff"))

image_list=[img1,img2,img3,img4,img5]
label = Label(frame, image = img1)
label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()

def back():
    global my_label
    global button_forward
    global button_back
    

button_back = Button(win,text="show prev",command= back)
button_exit = Button(win,text="exit",command=win.destroy)
button_forward = Button(win,text="show next",command= forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)


label.pack()

win.mainloop()
