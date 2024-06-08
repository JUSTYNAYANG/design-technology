from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("1000x1000")
root.title("Guide to Trignometry Identities")
widgets = []

def clear():
    for widget in widgets:
        widget.destroy()
    widgets.clear()
def reciprocal():
    #scrollbar
    canvas = Canvas(root, bg="white", scrollregion=(0, 0, 1000, 1700))
    canvas.pack(expand=True, fill=BOTH)
    widgets.append(canvas)

    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)

    #homebutton
    frame = Frame(canvas)
    canvas.create_window(68, 25, window=frame)
    homepagebutton = Button(frame, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.pack()
    widgets.append(homepagebutton and frame)

    # title
    framet = Frame(canvas)
    canvas.create_window(500, 50, window=framet)
    ##text
    t = Label(framet, text="Reciprocal Identities",fg="#ce7e00", font=('Georgia', 40))
    t.pack()
    widgets.append(t and framet)

    #formula
    framef1 = Frame(canvas)
    canvas.create_window(100, 200, window=framef1)
    f = Label(framef1, text="Formula:", fg="#4f192a", font=('Georgia', 30))
    f.pack()
    widgets.append(f and framef1)

    ft = Frame(canvas)
    canvas.create_window(300, 350, window=ft)
    test = ImageTk.PhotoImage(Image.open("formula/Reciprocal identities.png").resize((375,225)))
    im = Label(ft, image=test)
    im.image=test
    im.pack()
    widgets.append(im and ft)

    #description
    fd1 = Frame(canvas)
    canvas.create_window(120, 550, window=fd1)
    d = Label(fd1,text="Description:",fg="#4f192a", font=('Georgia', 30))
    d.pack()
    widgets.append(d and fd1)

    fd2 = Frame(canvas)
    canvas.create_window(500, 600, window=fd2)
    d1 = Label(fd2, text="In trigonometry, a reciprocal identity is the reciprocal of one of the basic trigonometric"
                          " functions. The reciprocal identities are the trig functions\n secant, cosecant, and cotangent.",
               fg="black", font=('Georgia', 14))
    d1.pack()
    widgets.append(d1 and fd2)

    #proof
    fp1 = Frame(canvas)
    canvas.create_window(80, 700, window=fp1)
    p = Label(fp1,text="Proof:",fg="#4f192a", font=('Georgia', 30))
    p.pack()
    widgets.append(p and fp1)

    fp2 = Frame(canvas)
    canvas.create_window(460, 1010, window=fp2)
    t = ImageTk.PhotoImage(Image.open("proof/Copy of Reciprocal identities_.png").resize((700, 550)))
    im1 = Label(fp2, image=t)
    im1.image = t
    im1.pack()
    widgets.append(fp2 and im1)

    #example
    fe1 = Frame(canvas)
    canvas.create_window(120, 1400, window=fe1)
    e = Label(fe1, text="Example:", fg="#4f192a", font=('Georgia', 30))
    e.pack()
    widgets.append(e and fe1)

    fe2 = Frame(canvas)
    canvas.create_window(460, 1560, window=fe2)
    t1 = ImageTk.PhotoImage(Image.open("Examples/Reciprocal identities & Quotient identities.png").resize((850, 250)))
    im2 = Label(fe2, image=t1)
    im2.image = t1
    im2.pack()
    widgets.append(fe2 and im2)

def quotientide():
    # scrollbar
    canvas = Canvas(root, bg="white", scrollregion=(0, 0, 1000, 1700))
    canvas.pack(expand=True, fill=BOTH)
    widgets.append(canvas)

    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)

    # homebutton
    frame = Frame(canvas)
    canvas.create_window(68, 25, window=frame)
    homepagebutton = Button(frame, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.pack()
    widgets.append(homepagebutton and frame)

    # title
    framet = Frame(canvas)
    canvas.create_window(500, 50, window=framet)
    ##text
    t = Label(framet, text="Quotient Identities", fg="#ce7e00", font=('Georgia', 40))
    t.pack()
    widgets.append(t and framet)

    # formula
    framef1 = Frame(canvas)
    canvas.create_window(100, 200, window=framef1)
    f = Label(framef1, text="Formula:", fg="#4f192a", font=('Georgia', 30))
    f.pack()
    widgets.append(f and framef1)

    ft = Frame(canvas)
    canvas.create_window(250, 350, window=ft)
    test = ImageTk.PhotoImage(Image.open("formula/Quotient identities.png").resize((400, 200)))  # (x,y)
    im = Label(ft, image=test)
    im.image = test
    im.pack()
    widgets.append(im and ft)

    # description
    fd1 = Frame(canvas)
    canvas.create_window(120, 525, window=fd1)
    d = Label(fd1, text="Description:", fg="#4f192a", font=('Georgia', 30))
    d.pack()
    widgets.append(d and fd1)

    fd2 = Frame(canvas)
    canvas.create_window(500, 600, window=fd2)
    d1 = Label(fd2, text="The quotient identity defines the relations for tangent and cotangent"
                         " in terms of sine and cosine. Often refer to trig identities that are\n"
                         "divided by each other. Cotangent, if you're unfamiliar with it,"
                         "is the inverse or reciprocal identity of tangent.\n",
               fg="black", font=('Georgia', 15))
    d1.pack()
    widgets.append(d1 and fd2)

    # proof
    fp1 = Frame(canvas)
    canvas.create_window(80, 700, window=fp1)
    p = Label(fp1, text="Proof:", fg="#4f192a", font=('Georgia', 30))
    p.pack()
    widgets.append(p and fp1)

    fp2 = Frame(canvas)
    canvas.create_window(460, 950, window=fp2)
    t = ImageTk.PhotoImage(Image.open("proof/Copy of Quotient Identities_.png").resize((800, 400)))
    im1 = Label(fp2, image=t)
    im1.image = t
    im1.pack()
    widgets.append(fp2 and im1)

    # example
    fe1 = Frame(canvas)
    canvas.create_window(80, 1225, window=fe1)
    e = Label(fe1, text="Example:", fg="#4f192a", font=('Georgia', 30))
    e.pack()
    widgets.append(e and fe1)

    fe2 = Frame(canvas)
    canvas.create_window(460, 1400, window=fe2)
    t1 = ImageTk.PhotoImage(Image.open("Examples/Reciprocal identities & Quotient identities.png").resize((850, 250)))
    im2 = Label(fe2, image=t1)
    im2.image = t1
    im2.pack()
    widgets.append(fe2 and im2)

def pythagorean():
    # scrollbar
    canvas = Canvas(root, bg="white", scrollregion=(0, 0, 1000, 2000))
    canvas.pack(expand=True, fill=BOTH)
    widgets.append(canvas)

    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)

    # homebutton
    frame = Frame(canvas)
    canvas.create_window(68, 25, window=frame)
    homepagebutton = Button(frame, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.pack()
    widgets.append(homepagebutton and frame)

    # title
    framet = Frame(canvas)
    canvas.create_window(500, 50, window=framet)
    ##text
    t = Label(framet, text="Pythagorean Identities", fg="#ce7e00", font=('Georgia', 40))
    t.pack()
    widgets.append(t and framet)

    # formula
    framef1 = Frame(canvas)
    canvas.create_window(100, 200, window=framef1)
    f = Label(framef1, text="Formula:", fg="#4f192a", font=('Georgia', 30))
    f.pack()
    widgets.append(f and framef1)

    ft = Frame(canvas)
    canvas.create_window(320, 340, window=ft)
    test = ImageTk.PhotoImage(Image.open("formula/Pythagorean identities.png").resize((450, 200)))
    im = Label(ft, image=test)
    im.image = test
    im.pack()
    widgets.append(im and ft)

    # description
    fd1 = Frame(canvas)
    canvas.create_window(120, 520, window=fd1)
    d = Label(fd1, text="Description:", fg="#4f192a", font=('Georgia', 30))
    d.pack()
    widgets.append(d and fd1)

    fd2 = Frame(canvas)
    canvas.create_window(500, 570, window=fd2)
    d1 = Label(fd2, text="In trigonometry, the pythagorean identity derives from the pythagorean theorem"
                         "(for right triangles). ",

               fg="black", font=('Georgia', 14))
    d1.pack()
    widgets.append(d1 and fd2)

    fp3 = Frame(canvas)
    canvas.create_window(235, 700, window=fp3)
    t = ImageTk.PhotoImage(Image.open("Visualization/Pythagorean Identities.png").resize((300, 200)))
    im2 = Label(fp3, image=t)
    im2.image = t
    im2.pack()
    widgets.append(fp3 and im2)

    fp4 = Frame(canvas)
    canvas.create_window(665, 700, window=fp4)
    t = ImageTk.PhotoImage(Image.open("Visualization/Pythagorean Identities(1).png").resize((500, 200)))
    im3 = Label(fp4, image=t)
    im3.image = t
    im3.pack()
    widgets.append(fp4 and im3)

    # proof
    fp1 = Frame(canvas)
    canvas.create_window(80, 875, window=fp1)
    p = Label(fp1, text="Proof:", fg="#4f192a", font=('Georgia', 30))
    p.pack()
    widgets.append(p and fp1)

    fp2 = Frame(canvas)
    canvas.create_window(440, 1065, window=fp2)
    t = ImageTk.PhotoImage(Image.open("proof/pythagorean.png").resize((600, 300)))
    im1 = Label(fp2, image=t)
    im1.image = t
    im1.pack()
    widgets.append(fp2 and im1)

    # example
    fe1 = Frame(canvas)
    canvas.create_window(120, 1300, window=fe1)
    e = Label(fe1, text="Example:", fg="#4f192a", font=('Georgia', 30))
    e.pack()
    widgets.append(e and fe1)

    fe2 = Frame(canvas)
    canvas.create_window(460, 1620, window=fe2)
    t1 = ImageTk.PhotoImage(Image.open("Examples/Pythagorean identities.png").resize((800, 550)))
    im2 = Label(fe2, image=t1)
    im2.image = t1
    im2.pack()
    widgets.append(fe2 and im2)

def cofunction():
    # scrollbar
    canvas = Canvas(root, bg="white", scrollregion=(0, 0, 1000, 2000))
    canvas.pack(expand=True, fill=BOTH)
    widgets.append(canvas)

    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)

    # homebutton
    frame = Frame(canvas)
    canvas.create_window(68, 25, window=frame)
    homepagebutton = Button(frame, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.pack()
    widgets.append(homepagebutton and frame)

    # title
    framet = Frame(canvas)
    canvas.create_window(500, 50, window=framet)
    ##text
    t = Label(framet, text="Cofunction Identities", fg="#ce7e00", font=('Georgia', 40))
    t.pack()
    widgets.append(t and framet)

    # formula
    framef1 = Frame(canvas)
    canvas.create_window(100, 200, window=framef1)
    f = Label(framef1, text="Formula:", fg="#4f192a", font=('Georgia', 30))
    f.pack()
    widgets.append(f and framef1)

    ft = Frame(canvas)
    canvas.create_window(400, 400, window=ft)
    test = ImageTk.PhotoImage(Image.open("formula/Cofunction identities.png").resize((580, 370)))
    im = Label(ft, image=test)
    im.image = test
    im.pack()
    widgets.append(im and ft)

    # description
    fd1 = Frame(canvas)
    canvas.create_window(120, 600, window=fd1)
    d = Label(fd1, text="Description:", fg="#4f192a", font=('Georgia', 30))
    d.pack()
    widgets.append(d and fd1)

    fd2 = Frame(canvas)
    canvas.create_window(520, 680, window=fd2)
    d1 = Label(fd2, text="The cofunction identities give a relationship between trigonometric functions sine and cosine, tangent and cotangent, and secant and cosecant. "
                         "\nThe cofunction of an angle is the trigonometric function of the angle's complement that produces an equal value to another trig function of \nthe original angle. "
                         "Complementary angles are angles whose values sum to 90 degrees or pie/2 radians.",
               fg="black", font=('Georgia', 14))
    d1.pack()
    widgets.append(d1 and fd2)

    # proof
    fp1 = Frame(canvas)
    canvas.create_window(80, 730, window=fp1)
    p = Label(fp1, text="Proof:", fg="#4f192a", font=('Georgia', 30))
    p.pack()
    widgets.append(p and fp1)

    fp2 = Frame(canvas)
    canvas.create_window(460, 1100, window=fp2)
    t = ImageTk.PhotoImage(Image.open("proof/Copy of Cofunction Identities_.png").resize((750, 550)))
    im1 = Label(fp2, image=t)
    im1.image = t
    im1.pack()
    widgets.append(fp2 and im1)

    # example
    fe1 = Frame(canvas)
    canvas.create_window(120, 1400, window=fe1)
    e = Label(fe1, text="Example:", fg="#4f192a", font=('Georgia', 30))
    e.pack()
    widgets.append(e and fe1)

    fe2 = Frame(canvas)
    canvas.create_window(460, 1700, window=fe2)
    t1 = ImageTk.PhotoImage(Image.open("Examples/Cofunction identities.png").resize((900, 430)))
    im2 = Label(fe2, image=t1)
    im2.image = t1
    im2.pack()
    widgets.append(fe2 and im2)

def evenodd():
    # scrollbar
    canvas = Canvas(root, bg="white", scrollregion=(0, 0, 1000, 1700))
    canvas.pack(expand=True, fill=BOTH)
    widgets.append(canvas)

    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)

    # homebutton
    frame = Frame(canvas)
    canvas.create_window(68, 25, window=frame)
    homepagebutton = Button(frame, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.pack()
    widgets.append(homepagebutton and frame)

    # title
    framet = Frame(canvas)
    canvas.create_window(500, 50, window=framet)
    ##text
    t = Label(framet, text="Reciprocal Identities", fg="#ce7e00", font=('Georgia', 40))
    t.pack()
    widgets.append(t and framet)

    # formula
    framef1 = Frame(canvas)
    canvas.create_window(100, 200, window=framef1)
    f = Label(framef1, text="Formula:", fg="#4f192a", font=('Georgia', 30))
    f.pack()
    widgets.append(f and framef1)

    ft = Frame(canvas)
    canvas.create_window(300, 375, window=ft)
    test = ImageTk.PhotoImage(Image.open("formula/Even odd identities.png").resize((500, 300)))  # (x,y)
    im = Label(ft, image=test)
    im.image = test
    im.pack()
    widgets.append(im and ft)

    # description
    fd1 = Frame(canvas)
    canvas.create_window(120, 600, window=fd1)
    d = Label(fd1, text="Description:", fg="#4f192a", font=('Georgia', 30))
    d.pack()
    widgets.append(d and fd1)

    fd2 = Frame(canvas)
    canvas.create_window(500, 675, window=fd2)
    d1 = Label(fd2, text="An even function is a function where the value of the function acting on an "
                         "argument is the same as the value of the function when acting on the negative\n "
                         "of the argument. Or, in short: For example, if f(x) is some function that is even,"
                         "then f(x) has the same answer as f(-x). f(-y) has the same answer as -f(y).\n",
               fg="black", font=('Georgia', 14))
    d1.pack()
    widgets.append(d1 and fd2)

    # proof
    fp1 = Frame(canvas)
    canvas.create_window(80, 750, window=fp1)
    p = Label(fp1, text="Proof:", fg="#4f192a", font=('Georgia', 30))
    p.pack()
    widgets.append(p and fp1)

    fp2 = Frame(canvas)
    canvas.create_window(450, 975, window=fp2)
    t = ImageTk.PhotoImage(Image.open("proof/Copy of Even-Odd Identities_.png").resize((900, 250)))
    im1 = Label(fp2, image=t)
    im1.image = t
    im1.pack()
    widgets.append(fp2 and im1)

    # example
    fe1 = Frame(canvas)
    canvas.create_window(80, 1250, window=fe1)
    e = Label(fe1, text="Example:", fg="#4f192a", font=('Georgia', 30))
    e.pack()
    widgets.append(e and fe1)

    fe2 = Frame(canvas)
    canvas.create_window(460, 1425, window=fe2)
    t1 = ImageTk.PhotoImage(Image.open("Examples/Even odd identities.png").resize((850, 250)))
    im2 = Label(fe2, image=t1)
    im2.image = t1
    im2.pack()
    widgets.append(fe2 and im2)
def sum():
    #scrollbar
    canvas = Canvas(root, bg="white", scrollregion=(0, 0, 1000, 2000))
    canvas.pack(expand=True, fill=BOTH)
    widgets.append(canvas)

    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)

    #homebutton
    frame = Frame(canvas)
    canvas.create_window(68, 25, window=frame)
    homepagebutton = Button(frame, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.pack()
    widgets.append(homepagebutton and frame)

    # title
    framet = Frame(canvas)
    canvas.create_window(500, 50, window=framet)
    ##text
    t = Label(framet, text="Sun of Angle Identities",fg="#ce7e00", font=('Georgia', 40))
    t.pack()
    widgets.append(t and framet)

    #formula
    framef1 = Frame(canvas)
    canvas.create_window(100, 200, window=framef1)
    f = Label(framef1, text="Formula:", fg="#4f192a", font=('Georgia', 30))
    f.pack()
    widgets.append(f and framef1)

    ft = Frame(canvas)
    canvas.create_window(380, 350, window=ft)
    test = ImageTk.PhotoImage(Image.open("formula/Sum of angle identities.png").resize((500,270)))
    im = Label(ft, image=test)
    im.image=test
    im.pack()
    widgets.append(im and ft)

    #description
    fd1 = Frame(canvas)
    canvas.create_window(120, 550, window=fd1)
    d = Label(fd1,text="Description:",fg="#4f192a", font=('Georgia', 30))
    d.pack()
    widgets.append(d and fd1)

    fd2 = Frame(canvas)
    canvas.create_window(500, 600, window=fd2)
    d1 = Label(fd2, text="You can use the angle-sum identities to find the function values of any angles.\n "
                         "Suppose, for example, that you want to find the exact value of the sine of 75 degrees.\n "
                         "To minimize fuss, you can use the sum of 30 degrees and 45 degrees and the appropriate identity;\n "
                         "this uses angles whose functions have nice, exact values.",
               fg="black", font=('Georgia', 14))
    d1.pack()
    widgets.append(d1 and fd2)

    #proof
    fp1 = Frame(canvas)
    canvas.create_window(80, 700, window=fp1)
    p = Label(fp1,text="Proof:",fg="#4f192a", font=('Georgia', 30))
    p.pack()
    widgets.append(p and fp1)

    fp2 = Frame(canvas)
    canvas.create_window(460, 1030, window=fp2)
    t = ImageTk.PhotoImage(Image.open("proof/Copy of The sum of Angle Identities_.png").resize((900, 600)))
    im1 = Label(fp2, image=t)
    im1.image = t
    im1.pack()
    widgets.append(fp2 and im1)

    #example
    fe1 = Frame(canvas)
    canvas.create_window(120, 1400, window=fe1)
    e = Label(fe1, text="Example:", fg="#4f192a", font=('Georgia', 30))
    e.pack()
    widgets.append(e and fe1)

    fe2 = Frame(canvas)
    canvas.create_window(600, 1700, window=fe2)
    t1 = ImageTk.PhotoImage(Image.open("Examples/Sum of angle identities.png").resize((1000, 500)))
    im2 = Label(fe2, image=t1)
    im2.image = t1
    im2.pack()
    widgets.append(fe2 and im2)
    pass

def difference():
    # scrollbar
    canvas = Canvas(root, bg="white", scrollregion=(0, 0, 1000, 1700))
    canvas.pack(expand=True, fill=BOTH)
    widgets.append(canvas)

    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)

    # homebutton
    frame = Frame(canvas)
    canvas.create_window(68, 25, window=frame)
    homepagebutton = Button(frame, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.pack()
    widgets.append(homepagebutton and frame)

    # title
    framet = Frame(canvas)
    canvas.create_window(500, 50, window=framet)
    ##text
    t = Label(framet, text="Difference of Angle Identities", fg="#ce7e00", font=('Georgia', 40))
    t.pack()
    widgets.append(t and framet)

    # formula
    framef1 = Frame(canvas)
    canvas.create_window(100, 200, window=framef1)
    f = Label(framef1, text="Formula:", fg="#4f192a", font=('Georgia', 30))
    f.pack()
    widgets.append(f and framef1)

    ft = Frame(canvas)
    canvas.create_window(350, 350, window=ft)
    test = ImageTk.PhotoImage(Image.open("formula/Difference of Angle identities.png").resize((500, 225)))  # (x,y)
    im = Label(ft, image=test)
    im.image = test
    im.pack()
    widgets.append(im and ft)

    # description
    fd1 = Frame(canvas)
    canvas.create_window(120, 550, window=fd1)
    d = Label(fd1, text="Description:", fg="#4f192a", font=('Georgia', 30))
    d.pack()
    widgets.append(d and fd1)

    fd2 = Frame(canvas)
    canvas.create_window(500, 600, window=fd2)
    d1 = Label(fd2,
               text="Consider two angles, α and β, the trigonometric sum and difference identities are as follows: \nsin(α+β)=sin(α).cos(β)+cos(α).sin(β) sin(α–β)=sinα.cosβ–cosα.sinβ cos(α+β)=cosα.cosβ–sinα.sinβ. \nUsed when one special angle can be subtracted from another, and the result is the given non-special angle.",
               fg="black", font=('Georgia', 14))
    d1.pack()
    widgets.append(d1 and fd2)

    # proof
    fp1 = Frame(canvas)
    canvas.create_window(80, 700, window=fp1)
    p = Label(fp1, text="Proof:", fg="#4f192a", font=('Georgia', 30))
    p.pack()
    widgets.append(p and fp1)

    fp2 = Frame(canvas)
    canvas.create_window(500, 1010, window=fp2)
    t = ImageTk.PhotoImage(Image.open("proof/Copy of Difference of Angle Identities_.png").resize((900, 550)))
    im1 = Label(fp2, image=t)
    im1.image = t
    im1.pack()
    widgets.append(fp2 and im1)

    # example
    fe1 = Frame(canvas)
    canvas.create_window(80, 1400, window=fe1)
    e = Label(fe1, text="Example:", fg="#4f192a", font=('Georgia', 30))
    e.pack()
    widgets.append(e and fe1)

    fe2 = Frame(canvas)
    canvas.create_window(460, 1560, window=fe2)
    t1 = ImageTk.PhotoImage(Image.open("Examples/Difference of angle identities.png").resize((850, 250)))
    im2 = Label(fe2, image=t1)
    im2.image = t1
    im2.pack()
    widgets.append(fe2 and im2)
def doubleangle():
    # scrollbar
    canvas = Canvas(root, bg="white", scrollregion=(0, 0, 1000, 2050))
    canvas.pack(expand=True, fill=BOTH)
    widgets.append(canvas)

    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)

    # homebutton
    frame = Frame(canvas)
    canvas.create_window(68, 25, window=frame)
    homepagebutton = Button(frame, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.pack()
    widgets.append(homepagebutton and frame)

    # title
    framet = Frame(canvas)
    canvas.create_window(500, 50, window=framet)
    ##text
    t = Label(framet, text="Double Angle Identities", fg="#ce7e00", font=('Georgia', 40))
    t.pack()
    widgets.append(t and framet)

    # formula
    framef1 = Frame(canvas)
    canvas.create_window(100, 200, window=framef1)
    f = Label(framef1, text="Formula:", fg="#4f192a", font=('Georgia', 30))
    f.pack()
    widgets.append(f and framef1)

    ft = Frame(canvas)
    canvas.create_window(320, 340, window=ft)
    test = ImageTk.PhotoImage(Image.open("formula/Double angle identities.png").resize((450, 220)))
    im = Label(ft, image=test)
    im.image = test
    im.pack()
    widgets.append(im and ft)

    # description
    fd1 = Frame(canvas)
    canvas.create_window(120, 520, window=fd1)
    d = Label(fd1, text="Description:", fg="#4f192a", font=('Georgia', 30))
    d.pack()
    widgets.append(d and fd1)

    fd2 = Frame(canvas)
    canvas.create_window(500, 570, window=fd2)
    d1 = Label(fd2, text="A double angle formula is a trigonometric identity that expresses a trigonometric function "
                         "of 2θ in terms of \ntrigonometric functions of θ.  ",

               fg="black", font=('Georgia', 14))
    d1.pack()
    widgets.append(d1 and fd2)

    fp3 = Frame(canvas)
    canvas.create_window(500, 720, window=fp3)
    t = ImageTk.PhotoImage(Image.open("Visualization/Double angle identities.jpg").resize((300, 250)))
    im2 = Label(fp3, image=t)
    im2.image = t
    im2.pack()
    widgets.append(fp3 and im2)

    # proof
    fp1 = Frame(canvas)
    canvas.create_window(80, 875, window=fp1)
    p = Label(fp1, text="Proof:", fg="#4f192a", font=('Georgia', 30))
    p.pack()
    widgets.append(p and fp1)

    fp2 = Frame(canvas)
    canvas.create_window(440, 1210, window=fp2)
    t = ImageTk.PhotoImage(Image.open("proof/double angle identity_.png").resize((500, 600)))
    im1 = Label(fp2, image=t)
    im1.image = t
    im1.pack()
    widgets.append(fp2 and im1)

    # example
    fe1 = Frame(canvas)
    canvas.create_window(120, 1570, window=fe1)
    e = Label(fe1, text="Example:", fg="#4f192a", font=('Georgia', 30))
    e.pack()
    widgets.append(e and fe1)

    fe2 = Frame(canvas)
    canvas.create_window(460, 1800, window=fe2)
    t1 = ImageTk.PhotoImage(Image.open("Examples/Double angle identities.png").resize((600, 290)))
    im2 = Label(fe2, image=t1)
    im2.image = t1
    im2.pack()
    widgets.append(fe2 and im2)
def halfangle():
    # scrollbar
    canvas = Canvas(root, bg="white", scrollregion=(0, 0, 1000, 1900))
    canvas.pack(expand=True, fill=BOTH)
    widgets.append(canvas)

    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)

    # homebutton
    frame = Frame(canvas)
    canvas.create_window(68, 25, window=frame)
    homepagebutton = Button(frame, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.pack()
    widgets.append(homepagebutton and frame)

    # title
    framet = Frame(canvas)
    canvas.create_window(500, 50, window=framet)
    ##text
    t = Label(framet, text="Half Angle Identities", fg="#ce7e00", font=('Georgia', 40))
    t.pack()
    widgets.append(t and framet)

    # formula
    framef1 = Frame(canvas)
    canvas.create_window(100, 200, window=framef1)
    f = Label(framef1, text="Formula:", fg="#4f192a", font=('Georgia', 30))
    f.pack()
    widgets.append(f and framef1)

    ft = Frame(canvas)
    canvas.create_window(320, 340, window=ft)
    test = ImageTk.PhotoImage(Image.open("formula/Half angle identities.png").resize((450, 220)))
    im = Label(ft, image=test)
    im.image = test
    im.pack()
    widgets.append(im and ft)

    # description
    fd1 = Frame(canvas)
    canvas.create_window(120, 520, window=fd1)
    d = Label(fd1, text="Description:", fg="#4f192a", font=('Georgia', 30))
    d.pack()
    widgets.append(d and fd1)

    fd2 = Frame(canvas)
    canvas.create_window(500, 590, window=fd2)
    d1 = Label(fd2, text="We study half angle formulas (or half-angle identities) in Trigonometry. Half angle formulas can be derived "
                         "using the double angle formulas. \n Half-angles in half angle formulas are usually denoted by θ/2, x/2, A/2, etc and the half-angle is a "
                         "sub-multiple angle. The half angle formulas \nare used to find the exact values of the trigonometric ratios of the angles like 22.5° "
                         "(which is half of the standard angle 45°)\n, 15° (which is half of the standard angle 30°), etc.",

               fg="black", font=('Georgia', 14))
    d1.pack()
    widgets.append(d1 and fd2)

    fp3 = Frame(canvas)
    canvas.create_window(500, 760, window=fp3)
    t = ImageTk.PhotoImage(Image.open("Visualization/Half angle identities.jpg").resize((300, 250)))
    im2 = Label(fp3, image=t)
    im2.image = t
    im2.pack()
    widgets.append(fp3 and im2)

    # proof
    fp1 = Frame(canvas)
    canvas.create_window(80, 945, window=fp1)
    p = Label(fp1, text="Proof:", fg="#4f192a", font=('Georgia', 30))
    p.pack()
    widgets.append(p and fp1)

    fp2 = Frame(canvas)
    canvas.create_window(440, 1160, window=fp2)
    t = ImageTk.PhotoImage(Image.open("proof/Copy of Half-Angle Identities_.png").resize((520, 350)))
    im1 = Label(fp2, image=t)
    im1.image = t
    im1.pack()
    widgets.append(fp2 and im1)

    # example
    fe1 = Frame(canvas)
    canvas.create_window(120, 1430, window=fe1)
    e = Label(fe1, text="Example:", fg="#4f192a", font=('Georgia', 30))
    e.pack()
    widgets.append(e and fe1)

    fe2 = Frame(canvas)
    canvas.create_window(460, 1650, window=fe2)
    t1 = ImageTk.PhotoImage(Image.open("Examples/Half angle identities.png").resize((650, 350)))
    im2 = Label(fe2, image=t1)
    im2.image = t1
    im2.pack()
    widgets.append(fe2 and im2)
def power():
    # scrollbar
    canvas = Canvas(root, bg="white", scrollregion=(0, 0, 1000, 1700))
    canvas.pack(expand=True, fill=BOTH)
    widgets.append(canvas)

    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)

    # homebutton
    frame = Frame(canvas)
    canvas.create_window(68, 25, window=frame)
    homepagebutton = Button(frame, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.pack()
    widgets.append(homepagebutton and frame)

    # title
    framet = Frame(canvas)
    canvas.create_window(500, 50, window=framet)
    ##text
    t = Label(framet, text="Power Reducing Identities", fg="#ce7e00", font=('Georgia', 40))
    t.pack()
    widgets.append(t and framet)

    # formula
    framef1 = Frame(canvas)
    canvas.create_window(100, 200, window=framef1)
    f = Label(framef1, text="Formula:", fg="#4f192a", font=('Georgia', 30))
    f.pack()
    widgets.append(f and framef1)

    ft = Frame(canvas)
    canvas.create_window(350, 350, window=ft)
    test = ImageTk.PhotoImage(Image.open("formula/Power reducing identities.png").resize((500, 225)))  # (x,y)
    im = Label(ft, image=test)
    im.image = test
    im.pack()
    widgets.append(im and ft)

    # description
    fd1 = Frame(canvas)
    canvas.create_window(120, 550, window=fd1)
    d = Label(fd1, text="Description:", fg="#4f192a", font=('Georgia', 30))
    d.pack()
    widgets.append(d and fd1)

    fd2 = Frame(canvas)
    canvas.create_window(500, 600, window=fd2)
    d1 = Label(fd2,
               text="Power-reduction identities allow us to rewrite expressions involving \ntrigonometric terms with trigonometric terms of smaller powers. \nExpress the product of trigonometric functions sine and cosine as the sum or difference of sine or cosine.",
               fg="black", font=('Georgia', 14))
    d1.pack()
    widgets.append(d1 and fd2)

    # proof
    fp1 = Frame(canvas)
    canvas.create_window(80, 700, window=fp1)
    p = Label(fp1, text="Proof:", fg="#4f192a", font=('Georgia', 30))
    p.pack()
    widgets.append(p and fp1)

    fp2 = Frame(canvas)
    canvas.create_window(500, 1010, window=fp2)
    t = ImageTk.PhotoImage(Image.open("proof/Copy of Power-reducing Identities_.png").resize((900, 400)))
    im1 = Label(fp2, image=t)
    im1.image = t
    im1.pack()
    widgets.append(fp2 and im1)

    # example
    fe1 = Frame(canvas)
    canvas.create_window(80, 1300, window=fe1)
    e = Label(fe1, text="Example:", fg="#4f192a", font=('Georgia', 30))
    e.pack()
    widgets.append(e and fe1)

    fe2 = Frame(canvas)
    canvas.create_window(460, 1500, window=fe2)
    t1 = ImageTk.PhotoImage(Image.open("Examples/Power reducing identities.png").resize((850, 250)))
    im2 = Label(fe2, image=t1)
    im2.image = t1
    im2.pack()
    widgets.append(fe2 and im2)
def productsum():
    # scrollbar
    canvas = Canvas(root, bg="white", scrollregion=(0, 0, 1000, 1700))
    canvas.pack(expand=True, fill=BOTH)
    widgets.append(canvas)

    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)

    # homebutton
    frame = Frame(canvas)
    canvas.create_window(68, 25, window=frame)
    homepagebutton = Button(frame, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.pack()
    widgets.append(homepagebutton and frame)

    # title
    framet = Frame(canvas)
    canvas.create_window(500, 50, window=framet)
    ##text
    t = Label(framet, text="Product to Sum", fg="#ce7e00", font=('Georgia', 40))
    t.pack()
    widgets.append(t and framet)

    # formula
    framef1 = Frame(canvas)
    canvas.create_window(100, 200, window=framef1)
    f = Label(framef1, text="Formula:", fg="#4f192a", font=('Georgia', 30))
    f.pack()
    widgets.append(f and framef1)

    ft = Frame(canvas)
    canvas.create_window(300, 350, window=ft)
    test = ImageTk.PhotoImage(Image.open("formula/Product to sum identities.png").resize((400, 225)))  # (x,y)
    im = Label(ft, image=test)
    im.image = test
    im.pack()
    widgets.append(im and ft)

    # description
    fd1 = Frame(canvas)
    canvas.create_window(120, 525, window=fd1)
    d = Label(fd1, text="Description:", fg="#4f192a", font=('Georgia', 30))
    d.pack()
    widgets.append(d and fd1)

    fd2 = Frame(canvas)
    canvas.create_window(500, 600, window=fd2)
    d1 = Label(fd2, text="The process of converting sums into products or products into sums can make "
                         "a difference between an easy solution to a problem and no solution at all.\n "
                         "Two sets of identities can be derived from the sum and difference identities"
                         " that help in this conversion.\n",
               fg="black", font=('Georgia', 14))
    d1.pack()
    widgets.append(d1 and fd2)

    # proof
    fp1 = Frame(canvas)
    canvas.create_window(80, 700, window=fp1)
    p = Label(fp1, text="Proof:", fg="#4f192a", font=('Georgia', 30))
    p.pack()
    widgets.append(p and fp1)

    fp2 = Frame(canvas)
    canvas.create_window(460, 1000, window=fp2)
    t = ImageTk.PhotoImage(Image.open("proof/Copy of Product-to-Sum Identities_.png").resize((750, 550)))
    im1 = Label(fp2, image=t)
    im1.image = t
    im1.pack()
    widgets.append(fp2 and im1)

    # example
    fe1 = Frame(canvas)
    canvas.create_window(80, 1400, window=fe1)
    e = Label(fe1, text="Example:", fg="#4f192a", font=('Georgia', 30))
    e.pack()
    widgets.append(e and fe1)

    fe2 = Frame(canvas)
    canvas.create_window(460, 1550, window=fe2)
    t1 = ImageTk.PhotoImage(Image.open("Examples/Product to Sum identities.png").resize((850, 250)))
    im2 = Label(fe2, image=t1)
    im2.image = t1
    im2.pack()
    widgets.append(fe2 and im2)
def sumproduct():
    # scrollbar
    canvas = Canvas(root, bg="white", scrollregion=(0, 0, 1000, 1700))
    canvas.pack(expand=True, fill=BOTH)
    widgets.append(canvas)

    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)

    # homebutton
    frame = Frame(canvas)
    canvas.create_window(68, 25, window=frame)
    homepagebutton = Button(frame, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.pack()
    widgets.append(homepagebutton and frame)

    # title
    framet = Frame(canvas)
    canvas.create_window(500, 50, window=framet)
    ##text
    t = Label(framet, text="Sum to Product", fg="#ce7e00", font=('Georgia', 40))
    t.pack()
    widgets.append(t and framet)

    # formula
    framef1 = Frame(canvas)
    canvas.create_window(100, 200, window=framef1)
    f = Label(framef1, text="Formula:", fg="#4f192a", font=('Georgia', 30))
    f.pack()
    widgets.append(f and framef1)

    ft = Frame(canvas)
    canvas.create_window(300, 350, window=ft)
    test = ImageTk.PhotoImage(Image.open("formula/Sum to product identities.png").resize((375, 225)))  # (x,y)
    im = Label(ft, image=test)
    im.image = test
    im.pack()
    widgets.append(im and ft)

    # description
    fd1 = Frame(canvas)
    canvas.create_window(120, 550, window=fd1)
    d = Label(fd1, text="Description:", fg="#4f192a", font=('Georgia', 30))
    d.pack()
    widgets.append(d and fd1)

    fd2 = Frame(canvas)
    canvas.create_window(500, 625, window=fd2)
    d1 = Label(fd2, text="The sum to product formula in trigonometry area formulas that are used to express "
                         "the sum and difference of sines and cosines as products of sine and cosine\n "
                         "functions. The sum to product formulas can be derived using the product to "
                         "sum formulas in trigonometry using substitutions of the variables.\n",
               fg="black", font=('Georgia', 14))
    d1.pack()
    widgets.append(d1 and fd2)

    # proof
    fp1 = Frame(canvas)
    canvas.create_window(80, 750, window=fp1)
    p = Label(fp1, text="Proof:", fg="#4f192a", font=('Georgia', 30))
    p.pack()
    widgets.append(p and fp1)

    fp2 = Frame(canvas)
    canvas.create_window(460, 1050, window=fp2)
    t = ImageTk.PhotoImage(Image.open("proof/Copy of Sum-to-Product Identities_.png").resize((800, 500)))
    im1 = Label(fp2, image=t)
    im1.image = t
    im1.pack()
    widgets.append(fp2 and im1)

    # example
    fe1 = Frame(canvas)
    canvas.create_window(80, 1400, window=fe1)
    e = Label(fe1, text="Example:", fg="#4f192a", font=('Georgia', 30))
    e.pack()
    widgets.append(e and fe1)

    fe2 = Frame(canvas)
    canvas.create_window(460, 1560, window=fe2)
    t1 = ImageTk.PhotoImage(Image.open("Examples/Sum to product identities.png").resize((850, 250)))
    im2 = Label(fe2, image=t1)
    im2.image = t1
    im2.pack()
    widgets.append(fe2 and im2)

def homepage():
    homepagebutton = Button(root, text='HOME', fg='#023b5e', command=lambda: [clear(), homepage()],
                            font=('Georgia', 40))
    homepagebutton.grid(column=0, row=0)
    widgets.append(homepagebutton)

    #reciprocal
    r = Button(root, text='Reciprocal\nIdentities', fg='#1985a1', command=lambda: [clear(), reciprocal()], font=('Georgia', 30))
    r.grid(column=1, row=2)
    widgets.append(r)

    #quotient
    q = Button(root, text='Quotient\nIdentities', fg='#1985a1', command=lambda: [clear(), quotientide()], font=('Georgia', 30))
    q.grid(column=3, row=2)
    widgets.append(q)
    #pythagorean
    p = Button(root, text='Pythagorean\nIdentities', fg='#1985a1', command=lambda: [clear(), pythagorean()], font=('Georgia', 30))
    p.grid(column=5, row=2)
    widgets.append(p)
    #cofunction
    cf = Button(root, text='Cofunction\nIdentities', fg='#1985a1', command=lambda: [clear(), cofunction()], font=('Georgia', 30))
    cf.grid(column=1, row=4)
    widgets.append(cf)
    #evenodd
    eo = Button(root, text='Even-Odd\nIdentities', fg='#1985a1', command=lambda: [clear(), evenodd()], font=('Georgia', 30))
    eo.grid(column=3, row=4)
    widgets.append(eo)
    #sum
    s = Button(root, text='Sum of Angle\nIdentities', fg='#1985a1', command=lambda: [clear(), sum()], font=('Georgia', 30))
    s.grid(column=5, row=4)
    widgets.append(s)
    #difference
    d = Button(root, text='Difference\nof Angle\nIdentities', fg='#1985a1', command=lambda: [clear(), difference()], font=('Georgia', 30))
    d.grid(column=1, row=6)
    widgets.append(d)
    #double angle
    da = Button(root, text='Double Angle\nIdentities', fg='#1985a1', command=lambda: [clear(), doubleangle()], font=('Georgia', 30))
    da.grid(column=3, row=6)
    widgets.append(da)
    #half angle
    ha = Button(root, text='Half Angle\nIdentities', fg='#1985a1', command=lambda: [clear(), halfangle()], font=('Georgia', 30))
    ha.grid(column=5, row=6)
    widgets.append(ha)
    #power reducing
    pr = Button(root, text='Power\nReducing\nIdentities', fg='#1985a1', command=lambda: [clear(), power()], font=('Georgia', 30))
    pr.grid(column=1, row=8)
    widgets.append(pr)
    #product to sum
    ps = Button(root, text='Product\nto Sum\nIdentities', fg='#1985a1', command=lambda: [clear(), productsum()], font=('Georgia', 30))
    ps.grid(column=3, row=8)
    widgets.append(ps)
    #sum to product
    sp = Button(root, text='Sum to\nProduct\nIdentites', fg='#1985a1', command=lambda: [clear(), sumproduct()], font=('Georgia', 30))
    sp.grid(column=5, row=8)
    widgets.append(sp)
    lb1 = Label(root, text=" \n \n ")
    lb1.grid(column=2, row=7)
    widgets.append(lb1)
    lb2 = Label(root, text=" \n \n ")
    lb2.grid(column=2, row=5)
    widgets.append(lb2)
    lb3 = Label(root, text=" \n \n ")
    lb3.grid(column=2, row=3)
    widgets.append(lb3)
    lb4 = Label(root, text=" \n\n\n\n\n ")
    lb4.grid(column=2, row=1)
    widgets.append(lb4)
    lb5 = Label(root, text="                     ")
    lb5.grid(column=2, row=6)
    widgets.append(lb5)
    lb6 = Label(root, text="                     ")
    lb6.grid(column=4, row=6)
    widgets.append(lb6)


homepage()

root.mainloop()