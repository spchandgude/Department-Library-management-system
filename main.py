import mysql.connector as ms
import tkinter as tk
from db_credentials import setu
from members import *
from books import *
from reg_window import *
from book_window import *


mukhya = tk.Tk()
mukhya.title("School of Computer Engineering : Library")
mukhya.geometry("900x600")
act_reg_win = tk.Button(mukhya, text="Register Member", command = start_reg_win)
act_addbook_win = tk.Button(mukhya, text="Add Books", command = start_addbook_win)
act_listAllbooks_win = tk.Button(mukhya, text="All books", command = start_listAllbooks_win)
act_searchBook_win = tk.Button(mukhya, text="Search Book", command = start_searchBook_win)

act_reg_win.pack()
act_addbook_win.pack()
act_listAllbooks_win.pack()
act_searchBook_win.pack()
mukhya.mainloop()


#book = search_book('title','')
#print(book)
