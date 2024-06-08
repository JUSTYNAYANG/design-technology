#python3 -m pip install pillow
from tkinter import *
from PIL import ImageTk, Image

#create window
root = Tk()
# can add words around it
Label1 = Label(root, text="hellow")
Label1.grid()
image1 = Image.open("xmaq.jpg")
test = ImageTk.PhotoImage(image1)
LabelOne = Label(root, image=test)
LabelOne.grid()

#loop window
root.mainloop()
