from tkinter import *


def change():
    myLabel.after(1000, myLabel.destroy())
    labbel = Label(root, text="Page Change Success!!!")
    labbel.grid(column=0, row=0)
    labbel = Label(root, text="sin2Θ+cos2Θ=1, tan2Θ+1=sec2Θ ")
    labbel.grid(column=2, row=3)

root = Tk()
root.title("TRiaLLLS")
root.geometry('800x500') #size (width, height)

myLabel = Label(root, text="Does this page changer work? I don't know, I guess I have to try it out", fg="#48c9b0")
myLabel.grid()

myButton = Button(root, text='change page', fg='#16a085', command=change, font=('Georgia', 60))
myButton.grid(column=0, row=1)


root.mainloop() #loops it so it shows