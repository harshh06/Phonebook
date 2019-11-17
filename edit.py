from Tkinter import *
from tkMessageBox import *
from edit import *
import sqlite3
con=sqlite3.Connection('phonebook_database')
cur=con.cursor()



def edit():

    stem3=Tk()
    stem3.geometry("600x400")
    stem3.title("Search Box")
    Label(stem3,text="Enter the name :").grid(row=0,column=1)
    s1=Entry(stem3)
    s1.grid(row=1,column=1)
    lb = Listbox(stem3,width=50, height=20)
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
        stem3.bind('<Button-1>',display)
            
    stem3.bind('<Key>',key)

    
        
    def display(e=1):
        t1=lb.curselection()

        cur.execute('select * from table1 where fname like ? ',('%'+s1.get()+'%',))
        t=cur.fetchall()
        tcid=[]
        for i in (t):
            tcid.append(i[0])
        index=t1[0]
        id1=tcid[index]
        
        
        stem3.destroy()
        
        stem2=Toplevel()
        stem2.geometry('550x400')
        Label(stem2,text='Phonebook',font="times 20 bold").grid(row=0,column=0)
        
        cur.execute('select * from table1 where contact_id=?',(id1,))
        edt=cur.fetchall()
        cur.execute('select * from table2 where contact_id=?',(id1,))
        edt2=cur.fetchall()
        cur.execute('select * from table3 where contact_id=?',(id1,))
        edt3=cur.fetchall()
        
        Label(stem2,text='First Name ').grid(row=1,column=0)
        e1=Entry(stem2)
        e1.insert(0,edt[0][1])
        e1.grid(row=1,column=2)
        
        Label(stem2,text='Middle Name ').grid(row=2,column=0)
        e2=Entry(stem2)
        e2.insert(0,edt[0][2])
        e2.grid(row=2,column=2)

        Label(stem2,text='Last Name ').grid(row=3,column=0)
        e3=Entry(stem2)
        e3.insert(0,edt[0][3])
        e3.grid(row=3,column=2)

        Label(stem2,text='Company Name ').grid(row=4,column=0)
        e4=Entry(stem2)
        e4.insert(0,edt[0][4])
        e4.grid(row=4,column=2)

        Label(stem2,text='Address ').grid(row=5,column=0)
        e5=Entry(stem2)
        e5.insert(0,edt[0][5])
        e5.grid(row=5,column=2)

        Label(stem2,text='City ').grid(row=6,column=0)
        e6=Entry(stem2)
        e6.insert(0,edt[0][6])
        e6.grid(row=6,column=2)

        Label(stem2,text='Pin Code ').grid(row=7,column=0)
        e7=Entry(stem2)
        e7.insert(0,edt[0][7])
        e7.grid(row=7,column=2)

        Label(stem2,text='Website URL ').grid(row=8,column=0)
        e8=Entry(stem2)
        e8.insert(0,edt[0][9])
        e8.grid(row=8,column=2)

        Label(stem2,text='Date of birth ').grid(row=9,column=0)
        e9=Entry(stem2)
        e9.insert(0,edt[0][9])
        e9.grid(row=9,column=2)

        #Phone entries

        Label(stem2,text='Select Phone Type : ',font="times 15 bold ").grid(row=10,column=0)


        v1=IntVar()
        
        r1=Radiobutton(stem2,text='Office',variable=v1,value=1)
        r1.grid(row=10,column=1)
        
        r2=Radiobutton(stem2,text='Home',variable=v1,value=2)
        r2.grid(row=10,column=2)

        r3=Radiobutton(stem2,text='Mobile',variable=v1,value=3)
        r3.grid(row=10,column=3)

       
        
        if edt2[0][1]=='Office':
            v1.set(1)
        elif edt2[0][1]=='Home':
            v1.set(2)
        else :
            v1.set(3)
        print v1
        
        Label(stem2,text='Phone Number').grid(row=11,column=0)
        e10=Entry(stem2)
        e10.insert(0,edt2[0][2])
        e10.grid(row=11,column=1)

        def clear():
            e10.delete(0,END)
            
        Button(stem2,text="+",command=clear).grid(row=11,column=2)

        Label(stem2,text='Select Email Type : ',font="times 15  bold ").grid(row=12,column=0)

        v2=IntVar()
        r1=Radiobutton(stem2,text='Office',variable=v2,value=1)
        r1.grid(row=12,column=1)
        r2=Radiobutton(stem2,text='Personal',variable=v2,value=2)
        r2.grid(row=12,column=2)

        
        if edt3[0][1]=='Office':
            v2.set(1)
        elif edt3[0][1]=='Personal':
            v2.set(2)
     
        
        

        Label(stem2,text='Email ID').grid(row=13,column=0)
        e11=Entry(stem2)
        e11.insert(0,edt3[0][2])
        e11.grid(row=13,column=1)

        def clear():
            e11.delete(0,END)
        #def fun1():
        #    p=[(e10.get(),)]

        def update1():
            tup=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(), id1)
            cur.execute('update table1 set fname=? ,mname=? , lname=? ,company=?, address=? , city=? ,pin=? ,website=?, birth_date=? where contact_id=? ',tup )
            con.commit()
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
            tup1=(b,e10.get(),id1)
            cur.execute('update table2 set contact_type=?, phone_number=? where contact_id=? ',tup1 )
            con.commit()
            tup2=(c,e11.get(),id1)
            cur.execute('update table3 set email_id_type=?, email_id=? where contact_id=? ',tup2 )
            con.commit()
            def fun():
                x=showinfo('Updated','Contact Updated Successfully !!')
            fun()
        

        def close1():
            def fun1():
                x=askyesno('Closing','Do you really want to close ?')
                if(x==True):
                    stem2.destroy()
            fun1()   

            
        Button(stem2,text="+",command=clear).grid(row=13,column=2)

        Button(stem2,text="Update",command=update1).grid(row=14,column=1)
        Button(stem2,text="Close",command=close1).grid(row=14,column=3)
        
        stem2.mainloop()
        


        
    stem3.mainloop()
    


 ##         new window         ##


    


   



