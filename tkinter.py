from tkinter import*

root=Tk()
root.title('First GUI!')
root.geometry('1600x800')

text = Label(root, text='Hi! I am a label.', fg='#FF796C')
text.grid()

def clicked():
    print("You clicked me!嘻嘻")

myButton= Button(root, text='Justyna!!! click me', command=clicked)
myButton.grid(column=1, row=0)
root.mainloop()
