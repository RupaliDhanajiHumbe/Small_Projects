from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql
import mysql.connector as sql


def clear():
    emailEntry.delete(0,END)
    UserNameEntry.delete(0,END)
    PaswordEntry.delete(0,END)
    ConfirmEntry.delete(0,END)
    check.set(0)
def connect_database():
    if emailEntry.get()=="" or UserNameEntry.get()=="" or PaswordEntry.get()=="":
        messagebox.showerror('Error','All Fields Are Required')
    elif PaswordEntry.get()!= ConfirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms and Conditions')
    else:
        try:
            con=sql.connect(host='localhost',user='root',password='root')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity issue, Please Try Again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table udata(id int auto_increment primary key not null, email varchar(50),username varchar(100),' \
                  'password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query='select * from udata where username=%s'
        mycursor.execute(query,(UserNameEntry.get(),))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Username Already exists')
        else:
            query='insert into udata(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),UserNameEntry.get(),PaswordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is Successful')
            clear()
            signup_window.destroy()
            import userlogin

def login_page():
    signup_window.destroy()
    import userlogin

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(0,0)
background=ImageTk.PhotoImage(file='bg (1).jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()
frame=Frame(signup_window,bg='white')
frame.place(x=565,y=100)

heading=Label(frame,text='CRATE AN ACCOUNT',font=('microsoft Yahei UI Light',18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email_Id',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

UserNameLabel=Label(frame,text='User Name',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
UserNameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

UserNameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
UserNameEntry.grid(row=4,column=0,sticky='w',padx=25)

PaswordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
PaswordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

PaswordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
PaswordEntry.grid(row=6,column=0,sticky='w',padx=25)

ConfirmLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
ConfirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

ConfirmEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
ConfirmEntry.grid(row=8,column=0,sticky='w',padx=25)
check=IntVar()
termsandcondition=Checkbutton(frame,text='I agree to Terms & Conditions',font=('Microsoft Yahei UI Light',9,'bold'),
                              bg='white',fg='firebrick1',variable=check, activebackground='white',activeforeground='firebrick1',cursor='hand2')
termsandcondition.grid(row=9,column=0,pady=10,padx=10)

signupButton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,command=connect_database,
                              bg='firebrick1',fg='white', activebackground='firebrick1',activeforeground='white',cursor='hand2',width=16)
signupButton.grid(row=10,column=0,padx=10)

alreadyaccount=Label(frame,text='Don`t have an account?',font=('Open Sans',9,'bold'), bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),bd=0,
                              bg='white',fg='blue', activebackground='white',activeforeground='blue',
                   cursor='hand2',width=16,command=login_page)
loginButton.place(x=160,y=385)

signup_window.mainloop()