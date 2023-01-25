import tkinter
from tkinter import *
from tkinter import messagebox

def ok():
    uname=e1.get()
    password=e2.get()
    if (uname==" "and password==" "):
        messagebox.showinfo("error","cannot be blank")
    elif(uname=="admin" and password=="123"):
        messagebox.showinfo("success","login successfull") 
        root.destroy()   
    else:
        messagebox.showinfo("incorrect","incorrect username or password")    
    

root=tkinter.Tk()
root.title("Login")
root.geometry("300x200")
global e1
global e2

Label(root,text="Username").place(x=10,y=10)
Label(root,text="Password").place(x=10,y=40)

e1=Entry(root,width=20)
e1.place(x=140,y=10)

e2=Entry(root,width=20)
e2.place(x=140,y=40)

Button(root,text="Login",height=1,width=7,command=ok).place(x=120,y=100)

root.mainloop()