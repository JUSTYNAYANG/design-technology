from tkinter import *

clicks = 0
def clicked():
    global clicks
    print("you clicked me!")
    clicks += 1
    countClicks.config(text=f"{clicks}")


root = Tk()from tkinter import *

clicks = 0
def clicked():
    global clicks
    print("you clicked me!")
    clicks += 1
    countClicks.config(text=f"{clicks}")
#

root = Tk()
root.title("Alice in Wonderland?")
root.geometry('800x500') #size (width, height)

myLabel = Label(root, text='Welcome to AliCE in WoNdeRLaND. ArE YoU ActUAlly HerE ThO? No OnE KnoWS :D', fg= "#48c9b0")
myLabel.grid()

myButton = Button(root, text='click me!', fg='#16a085', command=clicked, font=('Georgia', 60))
myButton.grid(column=1, row=0)

countClicks = Label(root, text='0', fg='#8e44ad')

countClicks.grid(column=1, row=2)

root.mainloop() #loops it so it shows
root.title("Alice in Wonderland?")
root.geometry('800x500') #size (width, height)

myLabel = Label(root, text='Welcome to AliCE in WoNdeRLaND. ArE YoU ActUAlly HerE ThO? No OnE KnoWS :D', fg= "#48c9b0")
myLabel.grid()

myButton = Button(root, text='click me!', fg='#16a085', command=clicked, font=('Georgia', 60))
myButton.grid(column=1, row=0)

countClicks = Label(root, text='0', fg='#8e44ad')

countClicks.grid(column=1, row=2)

root.mainloop() #loops it so it shows