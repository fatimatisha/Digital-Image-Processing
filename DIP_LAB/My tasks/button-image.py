# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("400x400")


# function to open a new window
# on a button click
def openNewWindow():
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("New Window")

	# sets the geometry of toplevel
	newWindow.geometry("700x500")
	canvas = Canvas(master, width = 300, height = 300)
	canvas.pack()
	img =ImageTk.PhotoImage(Image.open("D:\Fourth Year First Semester\DIP Lab\DIP_Python\Dataset\misc\\4.1.04.tiff"))
	canvas.create_image(20,20, anchor=NW, image=img)      

	


label = Label(master,
			text ="This is the main window")

label.pack(pady = 10)

# a button widget which will open a
# new window on button click
btn = Button(master,
			text ="Click to open a new window",
			command = openNewWindow)
btn.pack(pady = 10)

# mainloop, runs infinitely
mainloop()

