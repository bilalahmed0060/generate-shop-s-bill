from tkinter import*
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import font
import tkinter.ttk as ttk
import mysql.connector
import time
from fpdf import FPDF

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database = "mydatabase"
)

root1 = 0
root2 = 0
screen = 0
root = 0
el1 = 0
el2 = 0
el3 = 0
el4 = 0
el5 = 0
filename = 0
t = 0
enm = 0
lname = []
lpassword = []
lemail = []
lphone = []
myresult = 0
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM registration")
myresult = mycursor.fetchall()
for x in range(len(myresult)):
     lname.append(myresult[x][1].lower())
     lemail.append(myresult[x][2].lower())
     lphone.append(myresult[x][4])
     lpassword.append(myresult[x][3])


def MainScreen():
    global screen
    screen = Tk()
    if root != 0:
        screen.withdraw()
    if root != 0:
        root.withdraw()

    screen.geometry("450x200+400+200")
    load = Image.open('background1.jpg')
    photo = ImageTk.PhotoImage(load)
    img = Label(screen, image=photo)
    img.place(x=0, y=0)

    Button(screen,text = "Registration",command = Registration).place(x = 100,y = 80,width = 100,height = 30)
    Button(screen,text = "Login",command = Login).place(x = 250,y = 80,width = 100,height = 30)
    screen.mainloop()


def Registration():
    global root,name,email,phone,password,r,path
    global el1, el2, el3, el4, el5,enm,eem
    root = Toplevel(screen)
    if screen != 0:
        screen.withdraw()
    if root1 != 0:
        root1.withdraw()
    screen.withdraw()
    root.title("Registration Form")
    root.geometry("450x600+400+20")
    load = Image.open('background1.jpg')
    photo = ImageTk.PhotoImage(load)
    img1 = Label(root,image = photo)
    img1.place(x = 0,y = 0)

    el1 = Label(root, text="email ends with @gmail.com !")
    el2 = Label(root, text="Number start with 0 and length must be 11 !")
    el3 = Label(root, text="Password length must be greater than 7 !")
    el4 = Label(root, text="Please select the image!")
    enm = Label(root, text="Name aleady registered!")
    eem = Label(root, text="Email aleady registered!")

    Label(root,text = "User Name:",bg = "#4099c4",font = ("",10)).place(x = 50,y = 150)
    name = Entry(root)
    name.place(x = 200,y = 145,width = 200,height = 30)
    Label(root,text = "Email:",bg = "#428ec0",font = ("",10)).place(x = 50,y = 205)
    email = Entry(root)
    email.place(x = 200,y = 200,width = 200,height = 30)
    Label(root,text = "Phone No:",bg = "#4b8ec3",font = ("",10)).place(x = 50,y = 260)
    phone = Entry(root)
    phone.place(x = 200,y = 255,width = 200,height = 30)
    Label(root,text = "Password:  ",bg = "#5b8ecd",font = ("",10)).place(x = 50,y = 315)
    password  = Entry(root)
    password.place(x = 200,y = 310,width = 200,height = 30)
    Label(root,text = "Gender:  ",bg = "#5c81c7",font = ("",10)).place(x = 50,y = 370)

    r=StringVar()
    r.set("Male")
    Radiobutton(root,text="Male",variable=r,value="Male").place(x = 200,y = 365,width = 70,height = 30)
    Radiobutton(root,text="Female",variable=r,value="Female").place(x = 280,y = 365,width = 70,height = 30)

    Label(root,text = "Profile pic:",bg = "#6381c9",font = ("",10)).place(x = 50,y = 425)
    Button(root, text="Open File",command = open,bg = "blue").place(x = 200,y = 420,width = 150,height = 30)
    Button(root, text="Submit", bg="blue",command = submit).place(x=200, y=475, width=200, height=30)
    Button(root, text="Login", command=Login,bg = "blue").place(x=300, y=525, width=100, height=30)

    root.mainloop()

def Login():
    global root1,name1,password1
    if screen != 0:
        screen.withdraw()
    if root != 0:
        root.withdraw()

    root1 = Toplevel(screen)
    root1.title("Login")
    root1.geometry("360x330+400+170")
    load = Image.open('background1.jpg')
    photo = ImageTk.PhotoImage(load)
    img1 = Label(root1,image = photo)
    img1.place(x = 0,y = 0)
    Label(root1,text = "User Name:",bg="#248fb1",font = ("",10)).place(x = 70,y = 30)
    name1 = Entry(root1)
    name1.place(x = 70,y = 50,width = 220,height = 30)
    Label(root1,text = "Password:",bg="#399bc2",font = ("",10)).place(x = 70,y = 110)
    password1  = Entry(root1)
    password1.place(x = 70,y = 130,width = 220,height = 30)
    Button(root1, text="Login", bg="blue",command = check).place(x=70, y=190, width=220, height=35)
    Label(root1, text="Do not have an account?",bg = "#4b8cc2",font = ("",10)).place(x=70, y=250)
    Button(root1, text="Create Account", bg="blue",command = Registration).place(x=70, y=280)
    root1.mainloop()


def Main():
    global canvas,t,root2,fruit,quantity,amount,rname,l11,l1,subamount
    if root1 != 0:
        root1.withdraw()
    labelfont = font.Font(family = "helvetica",underline = 1)
    root2 = Toplevel(screen)
    root2.title("SHOP'S NAME")
    root2.geometry("800x600+200+20")
    load = Image.open('blue1.jpg')
    photo = ImageTk.PhotoImage(load)
    img3 = Label(root2, image=photo)
    img3.place(x=0, y=0)


    font1 = font.Font(family="Courier Bold", underline=1, size=12)
    d = Label(root2,text = "",font=font1,fg = "white",bg = "#0e4c79")
    d.place(x = 250,y = 80)

    #t = Label(root2,text = "",font=font1,fg = "blue",bg = "#e6e6e6")
    #t.place(x = 380 , y = 80,)
    def update():
        global datenow
        datenow = time.strftime("Date: %a_%d:%m:%Y    Time: %H:%M:%S")
        d.configure(text=datenow)
        root2.after(1000,update)
    update()

    #Canvas(root2,width=100, height=70).place(x=60, y=30)
    font2 = font.Font(family = "Courier Bold",underline = 1,size = 20)
    Label(root2, text="SHOP'S NAME",font=font2,fg = "white",bg = "#0e4c79").place(x=300, y=20)



    Label(root2, text= name1.get().capitalize(),font=("Courier Bold", 12),bg = "#054d7e",fg = "white").place(x=695, y=30,width = 80,height = 40)

    Button(root2, text="Logout", bg="white",fg = "blue",command = disp).place(x = 695, y = 75,width = 80,height = 30)


    Label(root2, text="Select Item:",fg = "white",font = ("",10),bg = "#0e4c79").place(x=30, y=150)

    # listbox = Listbox(root2, height=10,
    #                   width=190,
    #                   bg="blue",
    #                   activestyle='dotbox',
    #                   font="Helvetica",
    #                   fg="yellow")
    #
    # listbox.place(x=150, y=147.5, width=190, height=25)
    #item = Entry(root1).place(x=150, y=147.5, width=190, height=25)
    mycursor = mydb.cursor()
    itemlist = []
    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()
    for x in myresult:
        itemlist.append(x[0])
    global item
    item = StringVar()
    item.set("")
    global l2
    l2 = 0
    def OptionMenu_SelectionEvent(event):
        global myresult2,l2
        if l2 != 0:
            l2.place_forget()
        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT amount FROM customers Where name = %s ", (item.get(),))
        myresult2 = mycursor1.fetchone()
        new = str(myresult2[0])+" Rupees"
        l2 = Label(root2, text=new, fg="white", font=("", 10),bg = "#0e4c79")
        l2.place(x=320, y=147.5)
    menu = ttk.OptionMenu(root2, item, *itemlist,command = OptionMenu_SelectionEvent)
    menu.place(x=130, y=147.5, width=190, height=25)
    #menu.bind('<Return>',m)




    Label(root2, text="Enter Quantity:",bg = "#0e4c79",fg = "white",font = ("",10)).place(x=30, y=210)
    quantity= Entry(root2)
    l1 = 0
    l11=0
    def q(event):
        global l1,l11,paidamount1,myresult2
        if l11 != 0:
            l11.place_forget()

        try:
            paidamount1 = myresult2[0]*int(quantity.get())
            paidamount = str(paidamount1)+" Rupees"
            l11 = Label(root2, text=paidamount, bg="#0e4c79", fg="white", font=("", 10))
            l11.place(x=320, y=207.5)
            if l1 != 0:
                l1.place_forget()
        except:
            l1 = Label(root2, text="please select a Number", bg="#0e4c79", fg="white", font=("", 10))
            l1.place(x=130, y=237.5)

    quantity.place(x=130, y=207.5, width=190, height=25)
    quantity.bind('<Return>',q)

    Label(root2, text="Enter Amount:",bg = "#0e4c79",fg = "white",font = ("",10)).place(x=30, y=270)
    global l3
    l3 = 0
    def a(event):
        global l3,paidamount1,subamount
        if l3 != 0 :
            l3.place_forget()
        try:
            if int(amount.get()) < paidamount1:
                l3 = Label(root2, text="You Can't Buy!", bg="#0e4c79", fg="white", font=("", 10))
                l3.place(x=320, y=267.5)
            else:
                subamount = paidamount1-int(amount.get())
        except:
            l3 = Label(root2, text="Enter a Currect Number!", bg="#0e4c79", fg="white", font=("", 10))
            l3.place(x=130, y=297.5)

    amount = Entry(root2)
    amount.place(x=130, y=267.5, width=190, height=25)
    amount.bind('<Return>',a)

    Label(root2, text="Enter Name:",bg = "#0e4c79",fg = "white",font = ("",10)).place(x=30, y=320)
    def rn(event):
        Label(root2, text=rname.get(), bg="#0e4c79", fg="white", font=("", 10)).place(x=320, y=317.5)
    rname = Entry(root2)
    rname.place(x=130, y=317.5, width=190, height=25)
    rname.bind('<Return>',rn)

    gr = Button(root2, text="Generate receipt", command = show ,bg="blue",fg = "white")
    gr.place(x=130, y=367.5)

    save = Button(root2, text="Save", bg="blue",fg = "white")
    save.place(x=240, y=367.5,width = 80)

    canvas = Canvas(root2,width=320, height=470)
    load1 = Image.open('images2.png')
    photo1 = ImageTk.PhotoImage(load1)
    canvas.create_image(0, 0, image=photo1, anchor=NW)
    widget = Label(canvas, text="SHOP'S NAME",font=font2,fg = "white", bg='#224f81')
    widget.place(x = 60,y = 10)
    font3 = font.Font(family="Courier Bold", underline=1, size=11)
    datenow1 = time.strftime("Date: %a_%d.%m.%Y    Time: %H:%M:%S")
    e = Label(canvas, text=datenow1, font=font3, fg="white", bg="#224f81")
    e.place(x=25, y=60,width = 270)
    font4 = font.Font(family="Courier ", size=8)
    Label(canvas, text="Seller Name:", font=font4, bg="#ffffff").place(x = 30,y = 130)
    canvas.create_line(120, 140, 300, 140)
    Label(canvas, text="Buyer Name:", font=font4, bg="#ffffff").place(x=30, y=170)
    canvas.create_line(120, 180, 300, 180)

    Label(canvas, text="Selected Item:", font=font4, bg="#ffffff").place(x=30, y=210)
    canvas.create_line(120, 220, 300, 220)

    Label(canvas, text="Item Price:", font=font4, bg="#ffffff").place(x=30, y=250)
    canvas.create_line(120, 260, 300, 260)

    Label(canvas, text="Quantity:", font=font4, bg="#ffffff").place(x=30, y=290)
    canvas.create_line(120, 300, 300, 300)

    Label(canvas, text="Total Price:", font=font4, bg="#ffffff").place(x=30, y=330)
    canvas.create_line(120, 340, 300, 340)

    Label(canvas, text="Entered Amount:", font=font4, bg="#ffffff").place(x=30, y=370)
    canvas.create_line(120, 380, 300, 380)

    Label(canvas, text="Return Amount:", font=font4, bg="#ffffff",).place(x=30, y=410)





    # t = Label(root2,text = "",font=font1,fg = "blue",bg = "#e6e6e6")
    # t.place(x = 380 , y = 80,)


    root2.mainloop()


sname = None
semail = None
spassword = None
sphone = None
path = None
def submit():
    global lname,lemail,lphone,lpassword
    if name.get().lower() in lname:
        enm.place(x=200, y=175)
    else:
        if enm != 0:
            enm.place_forget()
            sname = name.get()



    if email.get().endswith("@gmail.com"):
        if email.get().lower() in lemail:
            eem.place(x=200, y=230)
        else:
            if el1 != 0:
                el1.place_forget()
            semail = email.get()
    else:
        el1.place(x=200, y=230)


    if phone.get().startswith("0") and len(phone.get()) == 11:
        if el2 != 0:
            el2.place_forget()
        sphone = phone.get()
    else:
        el2.place(x=200, y=285)

    if len(password.get()) > 7:
        if el3 !=0:
            el3.place_forget()
        spassword = password.get()
    else:
        el3.place(x = 200,y = 340)

    if filename !=0:
        if el4 !=0:
            el4.place_forget()
        spath = filename
    else:
        el4.place(x=200, y=450)

    if sname is not None and semail is not None and spassword is not None and sphone is not None and spath is not None:
        mycursor = mydb.cursor()

        sql = "INSERT INTO registration (name, email,password,phone_no,gender) VALUES (%s, %s, %s, %s, %s)"
        val = (sname,semail,spassword,sphone,r.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT * FROM registration")
        myresult1 = mycursor.fetchall()
        lname = []
        lemail = []
        lphone = []
        lpassword = []
        for x in range(len(myresult1)):
            lname.append(myresult1[x][1].lower())
            lemail.append(myresult1[x][2].lower())
            lphone.append(myresult1[x][4])
            lpassword.append(myresult1[x][3])



def disp():
    root2.withdraw()
    screen.deiconify()
def check():
    mycursor.execute("SELECT * FROM registration")
    myresult = mycursor.fetchall()
    for x in range(len(myresult)):
        if name1.get().lower() == lname[x] and password1.get() == lpassword[x]:
            Main()
        else:
            if x == len(myresult)-1:
                Label(root1, text="Invalid Name or Password",fg = "black",bg = "#4d8ec5",font = ("",10)).place(x=70, y=160)


def open():
    global filename
    filename = filedialog.askopenfilename(initialdir="C:/Users/CCS LAPTOP HYD/Pictures", title="Select A File",
                                               filetypes=(("jpg file", ".jpg"),("png file", ".png"),("all files", "*.*")))

global subamount,name1,rname,item,myresult2,quantity,paidamount,amount,datenow
def show():
    global subamount,name1,rname,item,myresult2,quantity,paidamount,amount,datenow
    Label(canvas, text=item.get(), bg="#ffffff").place(x=140, y=200,height = 12)
    Label(canvas, text=str(myresult2[0]) + " Rupees", bg="#ffffff").place(x=140, y=240,height = 12)
    Label(canvas, text=quantity.get(), bg="#ffffff").place(x=140, y=280,height = 12)
    Label(canvas, text=str(paidamount1) + " Rupees", bg="#ffffff").place(x=140, y=320,height = 12)
    Label(canvas, text=str(amount.get()) + " Rupees", bg="#ffffff").place(x=140, y=360,height = 12)
    Label(canvas, text=rname.get().capitalize(), bg="#ffffff").place(x=140, y=160,height = 12)
    Label(canvas, text=name1.get().capitalize(), bg="#ffffff").place(x=140, y=120,height = 12)
    Label(canvas, text=abs(subamount), bg="#ffffff").place(x=140, y=410)
    canvas.place(x=470, y=110)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("arial", size=20)
    pdf.cell(200, 10, txt="SHOP'S NAME", ln=1, align="C")
    pdf.set_font("arial", size=12)
    pdf.cell(200, 10, txt=datenow, ln=1, align="R")

    pdf.cell(0, 10, f'Seller Name         {name1.get().capitalize()}', ln=1, )
    pdf.cell(0, 10, f'Buyer Name          {rname.get().capitalize()}', ln=1)
    pdf.cell(0, 10, f'Selected Item       {item.get()}', ln=1)
    pdf.cell(0, 10, f'Item Price          {str(myresult2[0]) + " Rupees"}', ln=1)
    pdf.cell(0, 10, f'Quantity            {quantity.get()}', ln=1)
    pdf.cell(0, 10, f'Total Price         {str(paidamount1) + " Rupees"}', ln=1)
    pdf.output(f'{rname.get()}.pdf')

def hide():
    canvas.place_forget()

MainScreen()