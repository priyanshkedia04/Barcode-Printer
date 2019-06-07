from tkinter import *
from turtle import *
from tkinter import messagebox
from tkinter import ttk

class ean_13(object):
    def __init__ (self,in_manu,in_countrycode,in_productcode):
        self.par={'0':['odd' ,'odd','odd','odd','odd','odd'],
         '1':['odd','odd','even','odd','even','even'],
         '2':['odd','odd','even','even','odd','even'],
         '3':['odd','odd', 'even','even','even','odd'],
         '4':['odd','even', 'odd','odd','even','even'],
         '5':['odd','even','even','odd','odd','even'],
         '6':['odd','even','even','even', 'odd','odd'],
         '7':['odd','even','odd','even','odd','even'],
         '8':['odd','even','odd', 'even','even','odd'],
         '9':['odd','even','even','odd','even','odd']}
        self.right={'0':'1110010',
           '1':'1100110',
           '2':'1101100',
           '3':'1000010',
           '4':'1011100',
           '5':'1001110',
           '6':'1010000',
           '7':'1000100',
           '8':'1001000',
           '9':'1110100'}
        self.barcode_n=None
        self.bar='101'
        self.right_n=None
        self.left_n=None
        self.manufacturer_code=str(in_manu)
        self.product_code=str(in_productcode)
        self.countrycode=str(in_countrycode)

    def combine(self):
        self.barcode_n=self.countrycode+self.manufacturer_code+self.product_code

    def cal_check (self):
        list_bar=list(self.barcode_n)
        even=0
        odd=0

        for i in range(0,len(list_bar),2):
            even+=int(list_bar[i])

        for n in range(1,len(list_bar),2):
            odd+=int(list_bar[n])
        check=odd*3+even

        for i in range(0,10):
            if (check+i)%10==0:
                h=i
        self.barcode_n=self.barcode_n+str(h)

    def seperate(self):
        self.left_n=self.barcode_n[1:7]
        self.right_n=self.barcode_n[7:13]

    def left_parity(self):
        s=''
        l=self.par[self.barcode_n[0]]
        for i in range(len(self.left_n)):
            s=''
            if l[i]=='odd':
                c=self.right[self.left_n[i]]
                for num in c:
                    if num=='1':
                        s+='0'
                    else:
                        s+='1'
                self.bar+=s
            elif l[i]=='even':
                c=self.right[self.left_n[i]]
                s=c[::-1]
                self.bar+=s
            else:
                break

        self.bar+='01010'

    def right_parity(self):
        s=''
        for i in range(len(self.right_n)):
            c=self.right[self.right_n[i]]
            s+=c
        self.bar+=s
        self.bar+='101'

    def return_bar(self):
        msg.config(text=self.barcode_n)

    def check_me(self):
        t.reset()
        t.hideturtle()
        t.speed(0)
        t.penup()
        t.bk(140)
        t.rt(90)
        t.bk(70)
        for i in self.bar:
            if i=='1':
                black_p()
            else:
                white_p()
        t.setx(0)
        t.sety(0)

class ean_8(ean_13):
    def __init__(self,in_irn,in_countrycode8,in_productcode):
        ean_13.__init__(self,in_irn,in_countrycode8,in_productcode)
        self.barcode_n=None
        self.bar='101'
        self.item_reference=in_irn
        self.countrycode8=in_countrycode8

    def combine(self):
         self.barcode_n=str(self.countrycode8)+str(self.item_reference)

    def cal_check8(self):
        list_bar=list(self.barcode_n)
        even=0
        odd=0

        for i in range(0,len(list_bar),2):
            odd+=int(list_bar[i])

        for n in range(1,len(list_bar),2):
            even+=int(list_bar[n])
        check=odd*3+even

        for i in range(0,10):
            if (check+i)%10==0:
                h=i
        self.barcode_n=self.barcode_n+str(h)

    def left_8(self):
        self.left=self.barcode_n[:4]
        s=''
        for i in range(len(self.left)):
            s=''
            c=self.right[self.left[i]]
            for num in c:
                if num=='1':
                    s+='0'
                else:
                    s+='1'
            self.bar+=s
        self.bar+='01010'
    def right_8(self):
        self.right_n=self.barcode_n[4:]
        ean_13.right_parity(self)

    def return_bar(self):
        msg.config(text =self.barcode_n)

def black_p():
    t.pendown()
    t.color('black')
    t.pensize(3)
    t.fd(80)
    t.penup()
    t.bk(80)
    t.lt(90)
    t.fd(3)
    t.rt(90)

def white_p():
    t.pendown()
    t.color('white')
    t.pensize(3)
    t.fd(80)
    t.penup()
    t.bk(80)
    t.lt(90)
    t.fd(3)
    t.rt(90)

def ea8(in_irn,in_countrycode8,in_productcode):
    msg.config(text = "")
    EAN8=ean_8(in_irn,in_countrycode8,in_productcode)
    EAN8.combine()
    EAN8.cal_check8()
    EAN8.left_8()
    EAN8.right_8()
    EAN8.check_me()
    EAN8.return_bar()

def ea13(entry):
    msg.config(text = "")
    try:
        in_productcode = str(dict_items['PRODUCT : '+str(table.curselection()[0])])
        EAN13=ean_13(in_manu,in_countrycode,in_productcode)
        EAN13.combine()
        EAN13.cal_check()
        EAN13.seperate()
        EAN13.left_parity()
        EAN13.right_parity()
        EAN13.check_me()
        EAN13.return_bar()
    except:
        messagebox.showinfo("Input Error", "Select Valid Number" , icon = "warning")

def start_ean_13() :
    msg.config(text = "")
    t.reset()
    t.hideturtle()
    global option
    itemRefeleminput.delete(0, END)
    itemRefeleminput.config(state=DISABLED)
    countryCodeinput.config(state=NORMAL)
    manufCodeinput.config(state = NORMAL)
    noofprodinput.config(state = NORMAL)
    countryCodeinput.delete(0, END)
    option = 13

def start_ean_08() :
    msg.config(text = "")
    t.reset()
    t.hideturtle()
    global option
    try :
        table.destroy()
        instruction.destroy()
        right.destroy()
    except :
        pass

    itemRefeleminput.config(state=NORMAL)
    countryCodeinput.config(state=NORMAL)
    countryCodeinput.delete(0, END)
    manufCodeinput.delete(0, END)
    noofprodinput.delete(0, END)
    manufCodeinput.config(state = DISABLED)
    noofprodinput.config(state = DISABLED)
    option = 8

def start_8():
    choice=5
    while choice==5:

        global in_irn , in_countrycode8 , dict_items
        in_irn=str(itemRefeleminput.get())
        in_countrycode8=str(countryCodeinput.get())

        try:
            for i in in_countrycode8:
                if i not in '1234567890':
                    raise TypeError
        except:
            messagebox.showinfo("Input Error", "Country Code should be an Integer" , icon = "warning")
            break
        try:
            if len(in_countrycode8)!=2:
                raise ValueError
        except:
            messagebox.showinfo("Input Error", "Country Code should be of 2 digit" , icon = "warning")
            break
        try:
            for i in in_irn:
                if i not in '1234567890':
                    raise TypeError
        except:
            messagebox.showinfo("Input Error", "Item reference element should be an Integer" , icon = "warning")
            break
        try:
            if len(in_irn)!=5:
                raise ValueError
        except:
            messagebox.showinfo("Input Error", "Item reference element should be of 5 digit" , icon = "warning")
            break
        choice=6
        in_productcode=None
        ea8(in_irn,in_countrycode8,in_productcode)

def start_13():
    choice=5
    while choice==5:
        global in_manu , in_countrycode , dict_items , table , instruction
        in_manu=str(manufCodeinput.get())
        in_countrycode=str(countryCodeinput.get())
        in_items=str(noofprodinput.get())
        msg.config(text = "")
        t.reset()
        t.hideturtle()
        try:
            for i in in_countrycode:
                if i not in '1234567890':
                    raise TypeError
        except:
            messagebox.showinfo("Input Error", "Country Code should be an Integer" , icon = "warning")
            break
        try:
            if len(in_countrycode)!=2:
                raise ValueError
        except:
            messagebox.showinfo("Input Error", "Country Code should be of 2 digit" , icon = "warning")
            break
        try:
            for i in in_manu:
                if i not in '1234567890':
                    raise TypeError
        except:
            messagebox.showinfo("Input Error", "Manufacturing Code should be an Integer" , icon = "warning")
            break
        try:
            for i in in_items:
                if i not in '1234567890':
                    raise TypeError
        except:
            messagebox.showinfo("Input Error", "Number of Products should be an Integer" , icon = "warning")
            break
        try:
            if int(in_items)>99999:
                raise IOError
        except:
            messagebox.showinfo("Input Error", "No. of Products should be in range 1 to 99999." , icon = "warning")
            break
        try:
            if len(in_manu)!=5:
                raise ValueError
        except:
            messagebox.showinfo("Input Error", "Manufacturing Code should be of 5 digit" , icon = "warning")
            break
        choice=6
        dict_items={}
        global right
        right=Frame(bar_window,bd=0)
        right.place(x=1100,y=150,height=600,width=300)
        scrollbar = Scrollbar(right)
        scrollbar.pack( side = RIGHT, fill = Y )
        table=Listbox(right,font=("Arial",14,"bold"),height=25,justify=CENTER, yscrollcommand = scrollbar.set,selectmode=SINGLE)
        table.pack(fill=BOTH,expand=TRUE)
        table.insert(END, "Product Number")
        instruction = Label(bar_window , text = "Double click on Product no. to Generate Barcode." , font = ("Arial" , 16))
        instruction.place(x=475,y=500)

        for i in range(int(in_items)):
            dict_items['PRODUCT : '+ str(i+1)]= '%05d' %int(i+1)
        lvalues=dict_items.values()
        lkeys=dict_items.keys()
        for i in range(int(in_items)) :
            table.insert(END ,dict_items['PRODUCT : '+ str(i+1)])
        in_countrycode = int(countryCodeinput.get())
        table.bind("<Double-1>", ea13)

def submitfunc() :
    try:
        right.destroy()
    except:
        c=0
    msg.config(text = "")
    t.hideturtle()
    t.reset()
    if option == 13 :
        start_13()
    elif option == 8 :
        start_8()

help_text="""
HELP

-!- This program will help you to generate GTIN.

-!- By clicking on EAN08, enter Country Code and Item Reference Number to produce GTIN8.

-!- By clicking on EAN13, enter Country Code and Manufactruring code and Number of Products.

-!- Click on the desired Product Number (P no.) to generate the following GTIN

-!- Country Code must be of 2 digits only.

-!- Item Reference Number must be of 5 digits only.

-!- Manufacturing Code must be of 5 digits only.

-!- Range of Number of Products must lie from 1 to 99999.
"""


def helpmain():
    top=Tk()
    top.title("Help")
    l=Label(top,text=help_text,font=("Comic Sans MS",10), bg="Black", fg="White")
    l.pack()
    b=Button(top,text="Exit",command=lambda:top.withdraw()).pack()
    top.mainloop

bar_window = Tk()
bar_window.title("Barcogen")
bar_window.state("zoomed")
bar_window.configure(background="#325AD2")

name = Label(bar_window , text = "-!- Barco-Gen -!-" , font = ("Arial" , 50),bg="#325AD2")
name.pack(side = TOP,pady=20)

leftSide = Frame(bar_window , bd = 2,bg="#325AD2",relief=RAISED)
leftSide.place(x = 100 , y = 170)

ean08 = Button(leftSide , text = "EAN - 08" ,font = ("Arial" , 18), command = start_ean_08, height=1,width=15)
ean08.pack(side = TOP , padx = 10 , pady = 17)

ean13 = Button(leftSide , text = "EAN - 13" , command = start_ean_13, height=1,width = 15,font = ("Arial" , 18))
ean13.pack(side = TOP , padx = 10 , pady = 17)

helpLabel = Button(leftSide , text = "Help" , command = helpmain, height=1,width = 15,font=("Arial",18))
helpLabel.pack(side = TOP , padx = 10 , pady = 20)

center = Frame(bar_window , borderwidth = 2,bg="#325AD2",height=400,width=300,relief=SUNKEN)
center.place(x = 450 , y = 150)

h1 = Label(center , text = "Fill Details" , font = ("Arial" , 30),bg="#325AD2",fg="white")
h1.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
countryCode = Label(center , text = "Country Code :",font = ("Arial" , 14),bg="#325AD2",fg="white")
countryCode.grid(row=2,column=1,padx=10,pady=10)

countryCodeinput = Entry(center , state = DISABLED , width = 20,font = ("Arial" , 14),bg="#A9A9A9")
countryCodeinput.grid(row=2,column=2,padx=10,pady=10)

itemRefelem = Label(center , text = "Item Reference Element :",font = ("Arial" , 14),bg="#325AD2",fg="white" )
itemRefelem.grid(row=3,column=1,padx=10,pady=10)

itemRefeleminput = Entry(center , state = DISABLED , width = 20,font = ("Arial" , 14),bg="#A9A9A9")
itemRefeleminput.grid(row=3,column=2,padx=10,pady=10)

manufCode = Label(center , text = "Manufacturing Code :",font = ("Arial" , 14),bg="#325AD2",fg="white")
manufCode.grid(row=4,column=1,padx=10,pady=10)

manufCodeinput = Entry(center, state = DISABLED , width = 20,font = ("Arial" , 14),bg="#A9A9A9")
manufCodeinput.grid(row=4,column=2,padx=10,pady=10)

noofprod = Label(center , text = "No. of Products :",font = ("Arial" , 14),bg="#325AD2",fg="white")
noofprod.grid(row=5,column=1,padx=10,pady=10)

noofprodinput = Entry(center , state = DISABLED , width = 20,font = ("Arial" , 14),bg="#A9A9A9")
noofprodinput.grid(row=5,column=2,padx=10,pady=10)

submit = Button(center , text = "Submit" , command = submitfunc , width = 15,font = ("Arial" , 14))
submit.grid(row=6,column=1,columnspan=2,padx=10,pady=10)

canvas = Canvas(bar_window,width=400,height=150,bg="#325AD2",bd=5)
canvas.place(x = 490 , y = 540)
t = RawTurtle(canvas)
t.hideturtle()

msg = Label(bar_window , text = "", font = ("Arial" , 16))
msg.place(x = 600, y = 640)

bar_window.mainloop()
