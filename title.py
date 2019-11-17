from Tkinter import *
item=Tk()
item.geometry('800x400')
Label(item,text='Project title PhoneBook',font=("Helvetica", 20),fg="blue").grid(row=0,column=2)
Label(item,text='Developed By :',font=("Helvetica", 15)).grid(row=2,column=1)
Label(item,text='Harsh Soni',font=("Helvetica", 15)).grid(row=2,column=2)
Label(item,text='Enrollment Number :',font=("Helvetica", 15)).grid(row=3,column=1)
Label(item,text='181B096',font=("Helvetica", 15)).grid(row=3,column=2)
Label(item,text='Batch :',font=("Helvetica", 15)).grid(row=4,column=1)
Label(item,text='B3',font=("Helvetica", 15)).grid(row=4,column=2)
def c(e=1):
    item.destroy()
item.bind('<Motion>',c)
item.mainloop()
