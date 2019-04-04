import tkinter as tk
from tkinter import *
from tkinter import messagebox
from members import add_new_member

def start_reg_win():

    reg_win = Tk()
    reg_win.title("Member Registration")
    v=tk.IntVar()
    reg_win.geometry('900x600')
    member_types_array = ['Student','Faculty']
    def register_user():
        
        fn=reg_win_fname.get() + " " + reg_win_lname.get()
        add_new_member(member_types_array[v.get()], reg_win_mno.get(), reg_win_email.get(),fn)

        #if member added Successfully
        messagebox.showinfo("Successful","Member added Successfully")
        #print("Member" + fn +" Added Successful !!!")



    Label(reg_win, text="Library member Registration Form").grid(row=0,column=4)
    Label(reg_win, text="First Name").grid(row=3,column=3)
    Label(reg_win, text="Last Name").grid(row=4,column=3)
    Label(reg_win, text="Member Type").grid(row=5,column=3)
    Label(reg_win, text="Mobile Number:").grid(row=6,column=3)
    Label(reg_win, text="Email Id:").grid(row=7,column=3)
    reg_win_fname = Entry(reg_win)
    reg_win_lname = Entry(reg_win)
    reg_win_mtype1 = tk.Radiobutton(reg_win, text="Student", padx = 20, variable = v, value=0)
    reg_win_mtype2 = tk.Radiobutton(reg_win, text="Faculty", padx= 20, variable = v, value=1)
    reg_win_mno = Entry(reg_win)
    reg_win_email = Entry(reg_win)

    reg_win_fname.grid(row=3,column=4)
    reg_win_lname.grid(row=4,column=4)
    reg_win_mtype1.grid(row=5,column=4)
    reg_win_mtype2.grid(row=5, column=5)
    reg_win_mno.grid(row=6,column=4)
    reg_win_email.grid(row=7,column=4)
    Button(reg_win, text='Close', command=reg_win.destroy).grid(row=10,column=4, sticky=W, pady=4)
    Button(reg_win, text='Register', command=register_user).grid(row=10,column=5, sticky=W, pady=4)

    mainloop()
