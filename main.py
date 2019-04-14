import datetime
from tkinter import *
import time
from datetime import datetime 
from tkinter import messagebox
import os
import mysql.connector as ms

from db_credentials import setu
from members import *
from books import *
from reg_window import *
from book_window import *



"""Setting up the geometry and the title"""
root = Tk()
root.title("Library management system")
root.geometry('1350x650+0+0')
"""set"""


Topframe = Frame(root, width =    1350, height = 50,borderwidth=60,  bd = 8, relief ="sunken")
Topframe.pack(side = TOP)

frameone = Frame(root, width = 600, height = 600,borderwidth=60,bg="lightgreen",  bd = 8, relief = "sunken")
frameone.pack(side = LEFT)


frametwo = Frame(root, width = 300, height = 700,borderwidth=60, bd = 8, relief = "sunken")
frametwo.pack(side = RIGHT)

fla = Frame(frameone,width = 600, height = 200, bd = 20,bg="lightgrey", relief = "raise")
fla.pack(side = TOP)

flb = Frame(frameone,width = 600, height = 600, bd = 20,bg="lightgrey", relief = "raise")
flb.pack(side = TOP)




dateoforder = StringVar()
timeoforder = StringVar()


dateoforder.set(time.strftime("%d/%m/%Y"))
timeoforder.set(time.strftime("%H:%M"))

lblName = Label(fla, text = "BOOKS",bg="lightgrey",fg = "red", font = ('arial',30,'bold'),bd = 20)
lblName.grid(row = 0, column = 0)

lbladdress = Label(fla, text = "MEMBERS",bg="lightgrey",fg = "red", font = ('arial',30,'bold'),bd = 20)
lbladdress.grid(row = 0, column = 2)

addbook = Button(fla,text = 'Add book', padx = 16, pady = 16, bd =8, fg = "black",bg = "lightyellow", font = ('arial',16,'bold'), width = 15, height = 1,command = start_addbook_win).grid(row = 1, column = 1)

searchbook = Button(fla,text = 'Search book', padx = 16, pady = 16, bd =8, fg = "black",bg = "lightyellow", font = ('arial',16,'bold'), width = 15, height = 1,command = start_searchBook_win).grid(row = 2, column = 1)

allbooks = Button(fla,text = 'All books', padx = 16, pady = 16, bd =8, fg = "black",bg = "lightyellow", font = ('arial',16,'bold'), width = 15, height = 1,command = start_listAllbooks_win).grid(row = 3, column = 1)

updatebooks = Button(fla,text = 'Update book', padx = 16, pady = 16, bd =8, fg = "black",bg = "lightyellow", font = ('arial',16,'bold'), width = 15, height = 1).grid(row = 4, column = 1)

registermember = Button(fla,text = 'Register member', padx = 16, pady = 16, bd =8, fg = "black",bg = "lightyellow", font = ('arial',16,'bold'), width = 15, height = 1,command = start_reg_win).grid(row = 1, column = 3)

exitl = Button(flb,text = 'Exit', padx = 16, pady = 16, bd =8, fg = "black",bg = "red", font = ('arial',16,'bold'), width = 20, height = 1).grid(row = 0, column = 1)







lbldate = Label(frametwo,textvariable = dateoforder, font = ('arial',21,'bold')).grid(row = 0, column = 0)
lbltime = Label(frametwo,textvariable = timeoforder, font = ('arial',21,'bold')).grid(row = 1, column = 0)
txtsalary = Text(frametwo, height = 22, width = 34, bd = 16, font=('arial',12,'bold'))
txtsalary.grid(row = 2, column = 0)


lblinfo = Label(Topframe, font =('arial', 60, 'bold'), bg = "lightblue",fg = "Blue", text = "   MIT Academy of Engineering     ", bd = 10,)
lblinfo.grid(row = 0, column = 0)

lblmin = Label(Topframe, font = ('arial',15),fg="Blue", text = "(An Autonomous institute affiliated to SPPU)")
lblmin.grid(row = 1,column = 0)
lblmin = Label(Topframe, font = ('arial',15), text = "Department of Computer Science")
lblmin.grid(row = 2,column = 0)



root.mainloop()
