from tkinter import *
import pymysql
from tkinter import ttk
import re
from PIL import ImageTk,Image
import webbrowser
from datetime import date
f1=open('username1.txt','a')
f2=open('password1.txt','a')
win=Tk()
win.title('login page')
win.geometry('800x500+300+60')
win.config(bg="light blue")
win.resizable(0,0)
image5=ImageTk.PhotoImage(Image.open(r"C:\backupfolder\Cyber-Security.jpg"))
lbl=Label(win,image=image5)
lbl.pack(fill=BOTH)

# This function will update the record of the books returned 
def returned():
    win13=Toplevel()
    win13.state("zoomed")
    win13.resizable(0,0)
    win13.config(bg="light blue")
    scr=Scrollbar(win13)
    cols=("col1","col2","col3","col4","col5","col6")
    tree=ttk.Treeview(win13,column=cols,show="headings",height=10000,xscrollcommand=scr.set,yscrollcommand=scr.set)
    tree.place(x=200,y=200)
    ttk.Style().theme_use("classic")
    scr.pack(side=RIGHT,fill=Y)
    scr.config(command=tree.yview)
    tree.heading('#1',text='srno')
    tree.heading('#2',text='bookid')
    tree.heading('#3',text='bookname')
    tree.heading('#4',text='studentid')
    tree.heading('#5',text='studentname')
    tree.heading('#6',text='Date')
    py=pymysql.connect("localhost","root","root","book1")
    cur=py.cursor()
    cur.execute("select * from return2")
    data3=cur.fetchall()
    for data2 in data3:
        tree.insert("",END,values=data2)
    for line in range(10000):
        tree.insert("",END,""+str(line))
    tree.pack(side=RIGHT,fill=BOTH)



#This is the function that will return the books
def return2():
    etn1=str(etrn1.get())
    etn2=str(etrn2.get())
    etn3=str(etrn3.get())
    etn4=str(etrn4.get())
    yes1="yes"
    date6=date5
    py=pymysql.connect("localhost","root","root","book1")
    cur=py.cursor()
    cur.execute("create table IF NOT EXISTS return2(srno int(10) NOT NULL AUTO_INCREMENT,bookid int NOT NULL ,booknm varchar(50),studentid varchar(20),studnm varchar(20),date varchar(15),PRIMARY KEY(srno))")
    cur.execute("select bookid from issue2")
    data=cur.fetchall()
    data2=str(data)
    if re.search(etn1,data2):
        if etn1!="" and etn2!="" and etn3!="" and etn4!=""  and date6!="":
            cur.execute("insert into return2 values(NULL,'"+ etn1 +"','"+ etn2 +"','"+ etn3 +"','"+ etn4 +"','"+ date6 +"')")
            py.commit
            cur.execute("update books2 set avail='"+ yes1 + "' where bookid='"+ etn1 +"'")
            py.commit()
            cur.execute("delete from issue2 where bookid='"+ etn1 +"'")
            py.commit()
            etrn1.delete(0,END)
            etrn2.delete(0,END)
            etrn3.delete(0,END)
            etrn4.delete(0,END)
            lb9=Label(win11,text="Record updated",width=25,bg="#00FF00",border=2,relief="raised",font=("calibri",12))
            lb9.place(x=150,y=350)
        else:
            lb9=Label(win11,text="All fields are required",width=25,bg="#FF1493",border=2,relief="raised",font=("calibri",12))
            lb9.place(x=150,y=350)
    else:
        lb9=Label(win11,text="Book is not is use",width=25,bg="#FF1493",border=2,relief="raised",font=("calibri",12))
        lb9.place(x=150,y=350)        
        
    
# This is the window of the books returned function
def return1():
    global win11
    global etrn1
    global etrn2
    global etrn3
    global etrn4
    global date4
    global date5
    date4=date.today()
    date5=str(date4)
    
    print(date4)
    win11=Toplevel()
    win11.geometry('800x500+300+60')
    win11.config(bg="light blue")
    win11.resizable(0,0)
    mylb=Label(win11,text="Bookid",bg="#00FFFF",width=12,border=2,relief="raised",font=("calibri",12))
    mylb1=Label(win11,text="Bookname",bg="#00FFFF",width=12,border=2,relief="raised",font=("calibri",12))
    mylb2=Label(win11,text="Studentid",bg="#00FFFF",width=12,border=2,relief="raised",font=("calibri",12))
    mylb3=Label(win11,text="Studentname",bg="#00FFFF",width=12,border=2,relief="raised",font=("calibri",12))
    etrn1=Entry(win11,width=27)
    etrn2=Entry(win11,width=27)
    etrn3=Entry(win11,width=27)
    etrn4=Entry(win11,width=27)
    mylb.place(x=50,y=20)
    mylb1.place(x=50,y=90)
    mylb2.place(x=50,y=160)
    mylb3.place(x=50,y=220)
    etrn1.place(x=190,y=20)
    etrn2.place(x=190,y=90)
    etrn3.place(x=190,y=160)
    etrn4.place(x=190,y=220)
    bt=Button(win11,text="Return",bg="yellow",activebackground="#DAA520",font=("calibri",11),command=return2)
    bt.place(x=200,y=400)
    bt1=Button(win11,text="Books Returned",bg="yellow",activebackground="#DAA520",font=("calibri",11),command=returned)
    bt1.place(x=400,y=400)
    

#This is a function that will show the books that are already issued 
def inuse():
    win10=Toplevel()
    win10.state("zoomed")
    win10.resizable(0,0)
    win10.config(bg="light blue")
    scr=Scrollbar(win10)
    cols=("col1","col2","col3","col4","col5","col6","col7")
    tree=ttk.Treeview(win10,column=cols,show="headings",height=10000,xscrollcommand=scr.set,yscrollcommand=scr.set)
    tree.place(x=200,y=200)
    ttk.Style().theme_use("classic")
    scr.pack(side=RIGHT,fill=Y)
    scr.config(command=tree.yview)
    tree.heading('#1',text='srno')
    tree.heading('#2',text='bookid')
    tree.heading('#3',text='bookname')
    tree.heading('#4',text='studentid')
    tree.heading('#5',text='studentname')
    tree.heading('#6',text='studentno')
    tree.heading('#7',text='Date')
    py=pymysql.connect("localhost","root","root","book1")
    cur=py.cursor()
    cur.execute("select * from issue2")
    data3=cur.fetchall()
    for data2 in data3:
        tree.insert("",END,values=data2)
    for line in range(10000):
        tree.insert("",END,""+str(line))
    tree.pack(side=RIGHT,fill=BOTH)

    
#This is the main function that will insert records of the books issued
def issue2():
    et1=str(etr1.get())
    et2=str(etr2.get())
    et3=str(etr3.get())
    et4=str(etr4.get())
    et5=str(etr5.get())
    no1="no"
    date3=date2
    py=pymysql.connect("localhost","root","root","book1")
    cur=py.cursor()
    cur.execute("create table IF NOT EXISTS issue2(srno int NOT NULL AUTO_INCREMENT,bookid int NOT NULL ,booknm varchar(50),studentid varchar(20),studnm varchar(20),studno varchar(10),date varchar(15),PRIMARY KEY(srno))")
    cur.execute("select bookid from issue2")
    data=cur.fetchall()
    x=re.search(et1,str(data))
    if et1!="" and et2!="" and et3!="" and et4!="" and et5!="" and date3!="":
        cur.execute("insert into issue2 values(NULL,'"+ et1 +"','"+ et2 +"','"+ et3 +"','"+ et4 +"','"+ et5 +"','"+ date3 +"')")
        py.commit
        cur.execute("update books2 set avail='"+ no1 + "' where bookid='"+ et1 +"'")
        py.commit()
        etr1.delete(0,END)
        etr2.delete(0,END)
        etr3.delete(0,END)
        etr4.delete(0,END)
        etr5.delete(0,END)
        lb9=Label(win9,text="Issued successfully",width=25,bg="#00FF00",border=2,relief="raised",font=("calibri",12))
        lb9.place(x=150,y=350)
    else:
        lb9=Label(win9,text="All fields are required",width=25,bg="#FF1493",border=2,relief="raised",font=("calibri",12))
        lb9.place(x=150,y=350)
        
        

#This is the window to issue book
def issue1():
    global win9
    global etr1
    global etr2
    global etr3
    global etr4
    global etr5
    global date1
    global date2
    date1=date.today()
    date2=str(date1)
    win9=Toplevel()
    win9.geometry('800x500+300+60')
    win9.config(bg="light blue")
    win9.resizable(0,0)
    mylb=Label(win9,text="Bookid",bg="#00FFFF",width=12,border=2,relief="raised",font=("calibri",12))
    mylb1=Label(win9,text="Bookname",bg="#00FFFF",width=12,border=2,relief="raised",font=("calibri",12))
    mylb2=Label(win9,text="Studentid",bg="#00FFFF",width=12,border=2,relief="raised",font=("calibri",12))
    mylb3=Label(win9,text="Studentname",bg="#00FFFF",width=12,border=2,relief="raised",font=("calibri",12))
    mylb4=Label(win9,text="Phoneno",bg="#00FFFF",border=2,width=12,relief="raised",font=("calibri",12))    
    etr1=Entry(win9,width=27)
    etr2=Entry(win9,width=27)
    etr3=Entry(win9,width=27)
    etr4=Entry(win9,width=27)
    etr5=Entry(win9,width=27)
    mylb.place(x=50,y=20)
    mylb1.place(x=50,y=90)
    mylb2.place(x=50,y=160)
    mylb3.place(x=50,y=220)
    mylb4.place(x=50,y=280)
    etr1.place(x=190,y=20)
    etr2.place(x=190,y=90)
    etr3.place(x=190,y=160)
    etr4.place(x=190,y=220)
    etr5.place(x=190,y=280)
    bt=Button(win9,text="Issue",bg="yellow",activebackground="#DAA520",font=("calibri",11),command=issue2)
    bt.place(x=200,y=400)
    bt1=Button(win9,text="Books in use",bg="yellow",activebackground="#DAA520",font=("calibri",11),command=inuse)
    bt1.place(x=400,y=400)
    
# This is the function that will add new book record to the table
def addbk1():
    m=str(en1.get())
    n=str(en2.get())
    o=str(en3.get())
    yes1="yes"
    if m!="" and n!="" and o!="":
        py=pymysql.connect("localhost","root","root","book1")
        cur=py.cursor()
        cur.execute("create table IF NOT EXISTS books2(srno int NOT NULL AUTO_INCREMENT,bookid varchar(10) ,book varchar(50),author varchar(30),avail varchar(10),PRIMARY KEY(srno))")
        s="insert into books2 values(NULL,'"+ m +"','"+ n +"','"+ o +"','"+ yes1 +"')"
        cur.execute(s)
        py.commit()
        en1.delete(0,END)
        en2.delete(0,END)
        en3.delete(0,END)
        mlb=Label(win8,text="Record added successfully",bg="#00FF00",width=30,border=3,relief="raised",font=("calibri",16))
        mlb.place(x=180,y=378)
    else:
        mlb=Label(win8,text="All fields are required",bg="#FF1493",width=30,border=3,relief="raised",font=("calibri",16))
        mlb.place(x=180,y=278)
        
# This is the window of the addbook function

def addbk():
    global en1
    global en2
    global en3
    global win8
    win8=Toplevel()
    win8.geometry('800x500+300+60')
    win8.config(bg="light blue")
    win8.resizable(0,0)
    mlb=Label(win8,text="Enter Bookid",bg="yellow",width=13,relief="sunken",font=("calibri",14))
    mlb1=Label(win8,text="Enter Bookname",bg="yellow",width=13,relief="sunken",font=("calibri",14))
    mlb2=Label(win8,text="Enter Authorname",bg="yellow",width=15,relief="sunken",font=("calibri",14))
    btn=Button(win8,text="submit",bg="yellow",activebackground="#DAA520",font=("calibri",14),command=addbk1)
    btn.place(x=340,y=310)    
    en1=Entry(win8,width=27)
    en2=Entry(win8,width=27)
    en3=Entry(win8,width=27)
    mlb.place(x=300,y=50)
    mlb1.place(x=300,y=140)
    mlb2.place(x=300,y=230)
    en1.place(x=275,y=85)
    en2.place(x=275,y=175)
    en3.place(x=275,y=265)
    
# This is a function whick will delete the previous tree and the scroll bar
def clr():
    but1=Button(win7,text="Clear",border=3,bg="yellow",width=10,activebackground="#DAA520",font=("calibri",9),command=tree1.destroy(),state=DISABLED)
    but1.place(x=200,y=45)
    but1=Button(win7,text="Clear",border=3,bg="yellow",width=10,activebackground="#DAA520",font=("calibri",9),command=scr1.destroy(),state=DISABLED)
    but1.place(x=200,y=45)
    but=Button(win7,text="Search book",border=3,bg="yellow",activebackground="#DAA520",font=("calibri",9),command=check1,state=NORMAL)
    but.place(x=200,y=10)
    
# This is the main function which will check the availability of the book in the libraray system
def check1():
    global scr1
    global tree1
    entr2=str(entr1.get())
    scr1=Scrollbar(win7)
    cols=("col1","col2","col3","col4","col5")
    tree1=ttk.Treeview(win7,column=cols,show="headings",height=10000,xscrollcommand=scr1.set,yscrollcommand=scr1.set)
    tree1.place(x=200,y=200)
    ttk.Style().theme_use("classic")
    scr1.pack(side=RIGHT,fill=Y)
    scr1.config(command=tree1.yview)
    tree1.heading('#1',text='SRno')
    tree1.heading('#2',text='Bookid')
    tree1.heading('#3',text='Book')
    tree1.heading('#4',text='Author')
    tree1.heading('#5',text='Availability')
    py=pymysql.connect("localhost","root","root","book1")
    cur=py.cursor()
    cur.execute("create table IF NOT EXISTS books2(srno int NOT NULL AUTO_INCREMENT,bookid varchar(10) ,book varchar(50),author varchar(30),avail varchar(10),PRIMARY KEY(srno))")
    cur.execute("select * from books2")
    data3=cur.fetchall()
    for data2 in data3:
        if re.search(entr2,str(data2)):
            tree1.insert("",END,values=(data2))
        else:
            pass
    for line in range(10000):
        tree1.insert("",END,"" +str(line))
    tree1.pack(side=RIGHT,fill=BOTH)
    but=Button(win7,text="Search book",border=3,bg="yellow",activebackground="#DAA520",command=check1,font=("calibri",9),state=DISABLED)
    but.place(x=200,y=10)
    but1=Button(win7,text="Clear",border=3,bg="yellow",width=10,activebackground="#DAA520",command=clr,font=("calibri",9),state=NORMAL)
    but1.place(x=200,y=45)


# This is window of the function to check the availability of the book

def checkavailability():
    global win7
    global entr1
    win7=Toplevel()
    win7.state("zoomed")
    win7.resizable(0,0)
    win7.config(bg="light blue")
    entr1=Entry(win7,width=30)
    entr1.place(x=10,y=10)
    but=Button(win7,text="Search book",border=3,bg="yellow",activebackground="#DAA520",font=("calibri",9),command=check1)
    but.place(x=200,y=10)
    but1=Button(win7,text="Clear",border=3,bg="yellow",width=10,activebackground="#DAA520",font=("calibri",9),command=clr,state=DISABLED)
    but1.place(x=200,y=45)

#This function will open the webpage of the users choice
    
def learn():
    val2=val.get()
    #print(val2)
    if val2=="Python":
        new=2;
        url="file:///C:/Users/user/Desktop/new%20Html%20and%20css%20programs/new%20website.html";
        webbrowser.open(url,new=new);
    elif val2=="Linux":
        new=2;
        url="file:///C:/Users/user/Desktop/new%20Html%20and%20css%20programs/new%20website.html";
        webbrowser.open(url,new=new);
    elif val2=="C/C++":
        new=2;
        url="file:///C:/Users/user/Desktop/new%20Html%20and%20css%20programs/new%20website.html";
        webbrowser.open(url,new=new);
    elif val2=="HTML-CSS-JAVASCRIPT":
        new=2;
        url="file:///C:/Users/user/Desktop/new%20Html%20and%20css%20programs/new%20website.html";
        webbrowser.open(url,new=new);
    elif val2=="Core Java":
        new=2;
        url="file:///C:/Users/user/Desktop/new%20Html%20and%20css%20programs/new%20website.html";
        webbrowser.open(url,new=new);
    elif val2=="Advanced Java":
        new=2;
        url="file:///C:/Users/user/Desktop/new%20Html%20and%20css%20programs/new%20website.html";
        webbrowser.open(url,new=new);
    else:
        pass
    

# This is the window in the user will select which sysytem he/she wants to activate
def confirm1():
    global a4
    global image
    global val
    n=m.get()
    if n==1:
        a4=Toplevel()
        a4.resizable(0,0)
        image=ImageTk.PhotoImage(Image.open(r"C:\backupfolder\resized2.jpg"))
        lbl=Label(a4,image=image)
        lbl.pack(fill=BOTH)
        a4.geometry('800x500+300+60')
        a4.config(bg="light blue")
        lb1=Label(a4,text="WELLCOME TO OUR LEARNING PLATFORM",bg="yellow",relief="raised",font=("calibri",14))
        lb1.place(x=200,y=50)
        lb2=Label(a4,text="Select your course",bg="yellow",relief="raised",font=("calibri",14))
        lb2.place(x=300,y=180)
        val=StringVar()
        val.set("select option please")
        options=["Python","Linux","C/C++","HTML-CSS-JAVASCRIPT","Core Java","Advanced Java"]
        drop=OptionMenu(a4,val,*options)
        drop.config(bg="yellow")
        drop.place(x=300,y=240)
        btn1=Button(a4,text="Search",bg="yellow",width=15,activebackground="#DAA520",font=("calibri",14),command=learn)
        btn1.place(x=300,y=350)
        btn2=Button(a4,text="Take a break",bg="light blue",width=15,activebackground="#DAA520",font=("calibri",14))
        btn2.place(x=300,y=410)
    elif n==2:
        a4=Toplevel()
        a4.resizable(0,0)
        image=ImageTk.PhotoImage(Image.open(r"C:\Users\user\Desktop\html images\resized3.jpg"))
        lbl=Label(a4,image=image)
        lbl.pack(fill=BOTH)
        a4.geometry('800x500+300+60')
        a4.config(bg="light blue")
        btn=Button(a4,text="Check Availability",bg="yellow",activebackground="#DAA520",font=("calibri",14),command=checkavailability)
        btn.place(x=273,y=50)
        btn1=Button(a4,text="Issue Book",bg="yellow",activebackground="#DAA520",font=("calibri",14),command=issue1)
        btn1.place(x=293,y=140)
        btn2=Button(a4,text="Return Book",bg="yellow",activebackground="#DAA520",font=("calibri",14),command=return1)
        btn2.place(x=293,y=230)
        btn2=Button(a4,text="Add new Book",bg="yellow",activebackground="#DAA520",font=("calibri",14),command=addbk)
        btn2.place(x=288,y=320)
    else:
        pass

        

#This is the function to login
def login():
    global a3
    global bt1
    global lb
    global m
    global x
    e5=str(e3.get())
    e6=str(e4.get())
    if e5!="" and e6!="":
        f=open('password1.txt','r')
        data=f.readlines(100)
        data1=str(data)
        f1=open('username1.txt','r')
        data2=f1.readlines(100)
        data3=str(data2)
        zipped=dict(zip(data2,data))
        try:
            x=zipped[e5]
        except:
            lb=Label(a2,text="Wrong username or password",bg="red",width=30,relief="raised",border=3,font=("calibri",16))
            lb.place(x=170,y=318)
        if re.search(e5,data3) and e6==x:
            f.close()
            f1.close()
            e3.delete(0,END)
            e4.delete(0,END)
            a3=Toplevel()
            a3.geometry('800x500+300+60')
            a3.config(bg="light blue")
            #image3=ImageTk.PhotoImage(Image.open(r"C:\backupfolder\Cyber-Security.jpg"))
            #lbl=Label(a3,image=image3)
            #lbl.pack(fill=BOTH)
            a3.resizable(0,0)
            m=IntVar()
            m.set(1)
            lb=Label(a3,text="You are logged in",width=70,bg="#00FF00",relief="raised",border=3,font=("calibri",14))
            lb.place(x=0,y=0)
            lb=Label(a3,text="Make your selection",width=70,bg="orange",relief="raised",border=3,font=("calibri",14))
            lb.place(x=0,y=50)
            rd=Radiobutton(a3,text="Do courses",variable=m,value=1,bg="light blue",activebackground="light blue",font=("calibri",14))
            rd.place(x=320,y=170)
            rd2=Radiobutton(a3,text="Library system",variable=m,value=2,bg="light blue",activebackground="light blue",font=("calibri",14))
            rd2.place(x=320,y=210)
            bt1=Button(a3,text="Confirm",bg="Yellow",width=10,border=3,activebackground="#DAA520",font=("calibri",14),command=confirm1)
            bt1.place(x=340,y=330)

        else:
            e4.delete(0,END)
            lb=Label(a2,text="Wrong username or password",width=30,bg="#FF1493",relief="raised",border=3,font=("calibri",16))
            lb.place(x=170,y=318)
    else:
        lb=Label(a2,text="All fields are required",width=30,bg="#FF1493",relief="raised",border=3,font=("calibri",16))
        lb.place(x=170,y=318)


# This is the window of the login page   
def signin():
    global a2
    global image4
    a2=Toplevel()
    a2.resizable(0,0)
    image4=ImageTk.PhotoImage(Image.open(r"C:\backupfolder\Cyber-Security.jpg"))
    lbl=Label(a2,image=image4)
    lbl.pack(fill=BOTH)
    a2.geometry('800x500+300+60')
    #a2.config(bg="light blue")
    global e3
    global e4
    lb=Label(a2,text="Enter username",bg="#00FFFF",border=3,relief="raised",font=("calibri",16))
    lb.place(x=290,y=100)
    e3=Entry(a2,width=28)
    e3.place(x=270,y=140)
    lb1=Label(a2,text="Enter password",bg="#00FFFF",border=3,relief="raised",font=("calibri",16))
    lb1.place(x=290,y=180)
    e4=Entry(a2,show="*",width=28)
    e4.place(x=270,y=220)
    bt2=Button(a2,text="Login",bg="yellow",activebackground="#DAA520",border=5,font=("calibri",12),command=login)
    bt2.place(x=350,y=260)


#This is the function to save the password and username
def submit():
    
    e3=e1.get()
    e5=str(e3)
    e4=e2.get()
    e6=str(e4)
    global data2
    global data4
    if e3!="" and e4!="":
        f1=open('username1.txt','r')
        data3=f1.readlines(100)
        data4=str(data3)
        s=len(data3)
        f=open('password1.txt','r')
        data=f.readlines(100)
        data2=str(data)
        d=len(data)
        if re.search(e5,data4) or re.search(e6,data2) or d>0 or s>0:
            e1.delete(0,END)
            e2.delete(0,END)
            lb2=Label(a1,text="Username or Password already taken",width=30,bg="#FF1493",relief="raised",border=3,font=("calibri",16))
            lb2.place(x=170,y=318)
           
        else:
            f1=open('username1.txt','a+')
            f1.write("\n")
            f1.write(e3)
            f1.close()
            f=open('password1.txt','a+')
            f.write("\n")
            f.write(e4)
            f.close()
            print("record added")
            e1.delete(0,END)
            e2.delete(0,END)
            lb2=Label(a1,text="Account created successfully",width=30,bg="#00FF00",relief="raised",border=3,font=("calibri",16))
            lb2.place(x=170,y=318)
            
            
    else:
        lb1=Label(a1,text="All fields are required",bg="#FF1493",width=30,border=3,relief="raised",font=("calibri",16))
        lb1.place(x=170,y=318)

# window to create username and password    
def signup():
    global a1
    global bt1
    global image2
    global e1
    global e2
    a1=Toplevel()
    a1.resizable(0,0)
    #a1.config(bg="light blue")
    image2=ImageTk.PhotoImage(Image.open(r"C:\backupfolder\Cyber-Security.jpg"))
    lbl=Label(a1,image=image2)
    lbl.pack(fill=BOTH)
    a1.geometry('800x500+300+60')
    lb=Label(a1,text="Create username",bg="#00FFFF",border=3,relief="raised",font=("calibri",16))
    lb.place(x=270,y=100)
    e1=Entry(a1,width=28)
    e1.place(x=250,y=140)
    lb1=Label(a1,text="Create password",bg="#00FFFF",border=3,relief="raised",font=("calibri",16))
    lb1.place(x=270,y=180)
    e2=Entry(a1,show="*",width=28)
    e2.place(x=250,y=220)
    bt2=Button(a1,text="Submit",bg="yellow",activebackground="#DAA520",border=5,font=("calibri",12),command=submit)
    bt2.place(x=330,y=260)
bt1=Button(win,text='Sign up',bg="Yellow",width=15,border=4,activebackground="#DAA520",font=("calibri",15),command=signup)
bt1.place(x=270,y=130)
bt2=Button(win,text='Sign in',bg="Yellow",width=15,border=4,activebackground="#DAA520",font=("calibri",15),command=signin)
bt2.place(x=270,y=250)

