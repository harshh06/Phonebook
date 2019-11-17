import title
from Tkinter import *
from tkMessageBox import *
from edit import *
import sqlite3
con=sqlite3.Connection('phonebook_database')
cur=con.cursor()
cur.execute("create table if not exists table1(contact_id integer PRIMARY KEY AUTOINCREMENT,fname varchar(20),mname varchar(20),lname varchar(20),company varchar(50),address varchar(100),city varchar(30),pin number,website varchar(50),birth_date date)")
cur.execute("create table if not exists table2(contact_id integer,contact_type varchar(15),phone_number number(10),PRIMARY KEY(contact_id,phone_number),FOREIGN KEY(contact_id) REFERENCES TABLE1(contact_id))")
cur.execute("create table if not exists table3(contact_id integer,email_id_type varchar(15),email_id varchar(30),PRIMARY KEY(contact_id,email_id),FOREIGN KEY(contact_id) REFERENCES TABLE1(contact_id))")

root=Tk()
root.config(bg="ghost white")
root.geometry('650x600')

a=PhotoImage(file="img.gif")
Label(root,image=a).grid(row=0,column=1)
Label(root,text='Phonebook',font="times 20 bold",bg="ghost white").grid(row=1,column=0)

global id1


#Entries to be made

Label(root,text='First Name ',bg="ghost white").grid(row=2,column=0)
e1=Entry(root)
e1.grid(row=2,column=2)

Label(root,text='Middle Name ',bg="ghost white").grid(row=3,column=0)
e2=Entry(root)
e2.grid(row=3,column=2)

Label(root,text='Last Name ',bg="ghost white").grid(row=4,column=0)
e3=Entry(root)
e3.grid(row=4,column=2)

Label(root,text='Company Name ',bg="ghost white").grid(row=5,column=0)
e4=Entry(root)
e4.grid(row=5,column=2)

Label(root,text='Address ',bg="ghost white").grid(row=6,column=0)
e5=Entry(root)
e5.grid(row=6,column=2)

Label(root,text='City ',bg="ghost white").grid(row=7,column=0)
e6=Entry(root)
e6.grid(row=7,column=2)

Label(root,text='Pin Code ',bg="ghost white").grid(row=8,column=0)
e7=Entry(root)
e7.grid(row=8,column=2)

Label(root,text='Website URL ',bg="ghost white").grid(row=9,column=0)
e8=Entry(root)
e8.grid(row=9,column=2)

Label(root,text='Date of birth ',bg="ghost white").grid(row=10,column=0)
e9=Entry(root)
e9.grid(row=10,column=2)

#Phone entries

Label(root,text='Select Phone Type : ',font="times 15 bold ",bg="ghost white").grid(row=11,column=0)


v1=IntVar()
r1=Radiobutton(root,text='Office',variable=v1,value=1,bg="ghost white")
r1.grid(row=11,column=1)
r2=Radiobutton(root,text='Home',variable=v1,value=2,bg="ghost white")
r2.grid(row=11,column=2)
r3=Radiobutton(root,text='Mobile',variable=v1,value=3,bg="ghost white")
r3.grid(row=11,column=3)

Label(root,text='Phone Number',bg="ghost white").grid(row=12,column=0)
e10=Entry(root)
e10.grid(row=12,column=1)

def clear():
    e10.delete(0,END)
    
Button(root,text="+",command=clear).grid(row=12,column=2)

Label(root,text='Select Email Type : ',font="times 15  bold ",bg="ghost white").grid(row=13,column=0)

v2=IntVar()
r1=Radiobutton(root,text='Office',variable=v2,value=1,bg="ghost white")
r1.grid(row=13,column=1)
r2=Radiobutton(root,text='Personal',variable=v2,value=2,bg="ghost white")
r2.grid(row=13,column=2)

Label(root,text='Email ID',bg="ghost white").grid(row=14,column=0)
e11=Entry(root)
e11.grid(row=14,column=1)

def clear():
    e11.delete(0,END)
#def fun1():
#    p=[(e10.get(),)]
    
Button(root,text="+",command=clear,).grid(row=14,column=2)

def save():
    cur.execute("insert into table1(fname,mname,lname,company,address,city,pin,website,birth_date) values (?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),))
    global b,c
    if (v1.get()==1):
        b='Office'
    elif(v1.get()==2):
        b='Home'
    elif(v1.get()==3):
        b='Mobile'
    else:
        b=''
    if (v2.get()==1):
        c='Office'
    elif(v2.get()==2):
        c='Personal'
    else:
        c=''    
    cur.execute("select last_insert_rowid()")   
    m=cur.fetchall()
    cur.execute("insert into table2(contact_id,contact_type,phone_number) values (?,?,?)",(m[0][0],b,e10.get(),))
    cur.execute("insert into table3(contact_id,email_id_type,email_id) values (?,?,?)",(m[0][0],c,e11.get(),))
    cur.execute("select * from table1")
    print cur.fetchall()
    cur.execute("select * from table2")
    print cur.fetchall()
    cur.execute("select * from table3")
    print cur.fetchall()
    con.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    
    def fun():
        x=showinfo('Saved','Contact Saved Successfully !!')
    fun()
    
global tcid
tcid=[]


def search():
    stem=Tk()
    stem.geometry("600x400")
    stem.title("Search Box")
    Label(stem,text="Enter the name :").grid(row=0,column=1)
    s1=Entry(stem)
    s1.grid(row=1,column=1)
    lb = Listbox(stem,width=50, height=20)
    lb.grid(row=2,column=1)

    
    
    def key(e=1):
        lb.delete('0','end')
        cur.execute('select * from table1 where fname like ? ',('%'+s1.get()+'%',))
        t=cur.fetchall()
        tcid=[]
        
        for i in (t):
            lb.insert(END,i[1])
            tcid.append(i[0])
        print tcid
        stem.bind('<Button-1>',display)
            
    stem.bind('<Key>',key)

    
        
    def display(e=1):
        t1=lb.curselection()

        cur.execute('select * from table1 where fname like ? ',('%'+s1.get()+'%',))
        t=cur.fetchall()
        tcid=[]
        for i in (t):
            tcid.append(i[0])
        index=t1[0]
        id1=tcid[index]
        
        lb.delete('0','end')
        cur.execute('select * from table1 where contact_id= ? ',(id1,))
        fn1=cur.fetchall()
        cur.execute('select * from table2 where contact_id= ? ',(id1,))
        fn2=cur.fetchall()
        cur.execute('select * from table3 where contact_id= ? ',(id1,))
        fn3=cur.fetchall()
        
        for i in fn1:
            lb.insert(END,("First Name :"+i[1]))
            lb.insert(END,("Middle Name :"+i[2]))
            lb.insert(END,("Last Name :"+i[3]))
            lb.insert(END,("Company :"+i[4]))
            lb.insert(END,("Address :"+i[5]))
            lb.insert(END,("City :"+i[6]))
            lb.insert(END,("Pin :"+str(i[7])))
            lb.insert(END,("Website :"+i[8]))
            lb.insert(END,("Birth date :"+i[9]))

        for j in fn2:
            lb.insert(END,("Contact Type :"+j[1]))
            lb.insert(END,("Phone Number :"+str(j[2])))

        for k in fn3:
            lb.insert(END,("Email Type :"+k[1]))
            lb.insert(END,("Email :"+k[2]))
            
        def delete():
            def fun1():
                x=askyesno('Closing','Do you really want to delete ?')
                if(x==True):
                    cur.execute('delete from table1 where contact_id=?',(id1,))
                    stem.destroy()
            fun1()

            
        Button(stem,text="Delete",command=delete).grid(row=4,column=2)

    def close2():
        def fun1():
            x=askyesno('Closing','Do you really want to close ?')
            if(x==True):
                stem.destroy()
        fun1() 
    Button(stem,text="Close",command=close2).grid(row=4,column=1)
    stem.mainloop()
    

def close():
    def fun1():
        x=askyesno('Closing','Do you really want to close ?')
        if(x==True):
            root.destroy()
    fun1()   
    
    


Button(root,text="Save",command=save,bg="LightCyan2").grid(row=15,column=0)

Button(root,text="Search",command=search,bg="LightCyan2").grid(row=15,column=1)

Button(root,text="Close",command=close,bg="LightCyan2").grid(row=15,column=2)

Button(root,text="Edit",command=edit,bg="LightCyan2").grid(row=15,column=3)

root.mainloop()
