import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from books import *


#book_schema = get_book_schema()


#Clears the table records from the scree... Used while refreshing the table for new query
def clearTable(tree):
    x = tree.get_children()
    for item in x:
        tree.delete(item)


def start_searchBook_win():
    book_win = tk.Tk()
    #book_win.overrideredirect(1)
    book_win.title("Search Book")
    book_win.geometry("960x600")
    v=IntVar()

    def selectItem(a):
        CurItem = tree.focus()
        print(tree.item(CurItem))

    def searchit():
        clearTable(tree)
        print(tkvar.get())
        searchedBook = search_book(tkvar.get(), searchField.get())
        if searchedBook == -1:
            messagebox.showinfo("","Book Not Found")
        else:
            for book in searchedBook:
                tree.insert('',0, text='', value = book)




    tkvar = StringVar(book_win)
    Label(book_win, text="Search Book By :").pack()
    searchField = Entry(book_win)
    searchBy = ['title', 'accession_number', 'author', 'publisher']
    tkvar.set('title')

    popupMenu = OptionMenu(book_win, tkvar, *searchBy)
    searchField.pack()
    popupMenu.pack()
    #   Button(book_win, text='Search',command=searchit).grid(row=5, column=3, sticky = W, pady=4)
    Button(book_win, text='Search',command=searchit).pack()
    Button(book_win, text='Exit', command = book_win.destroy)
    #Book table
    tree = ttk.Treeview(book_win)
    tree["column"] = ("acn", "title", "author", "shlfno.", "publisher", "price")
    tree.column("acn", width=100)
    tree.column("title", width=150)
    tree.column("author", width=100)
    tree.column("shlfno.", width=80)
    tree.column("publisher", width=100)
    tree.column("price", width=100)
    tree.heading("acn", text="Accession No.")
    tree.heading("title", text="Title")
    tree.heading("author", text="Author")
    tree.heading("shlfno.", text="Shelf no")
    tree.heading("publisher", text="Publisher")
    tree.heading("price", text="Price")
    tree.bind('<ButtonRelease-1>', selectItem)
    tree.pack()
    mainloop()





#def start_upd8Book_win():
#    book_win = tk.Tk()
    #book_win.overrideredirect(1)
#    book_win.title("Search Book")
#    book_win.geometry("960x600")
#    v=IntVar()
#
#    def selectItem(a):
#        CurItem = tree.focus()
#        print(tree.item(CurItem))
#
#        Label(book_win,text="Title:").pack(side=LEFT)
#        new_title = Entry(book_win)
#
#        new_title.pack(side=LEFT)
#        #return tree.item(CurItem)
#
#    def searchit():
#        clearTable(tree)
#        print(tkvar.get())
#        searchedBook = search_book(tkvar.get(), searchField.get())
#        if searchedBook == -1:
#            messagebox.showinfo("","Book Not Found")
#        else:
#            for book in searchedBook:
#                tree.insert('',0, text='', value = book
#
#    tkvar = StringVar(book_win)
#    Label(book_win, text="Search Book By :").pack()
#    searchField = Entry(book_win)
#    searchBy = ['title', 'accession_number', 'author', 'publisher']
#    tkvar.set('title')
#
#    popupMenu = OptionMenu(book_win, tkvar, *searchBy)
#    searchField.pack()
#    popupMenu.pack()
#
#
#    #Button(book_win, text='Search',command=searchit).grid(row=5, column=3, sticky = W, pady=4)
#    Button(book_win, text='Search',command=searchit).pack()
#    Button(book_win, text='Exit', command = book_win.destroy)
#    #Book table
#    tree = ttk.Treeview(book_win)
#    tree["column"] = ("acn", "title", "author", "shlfno.", "publisher", "price")
#    tree.column("acn", width=100)
#    tree.column("title", width=150)
#    tree.column("author", width=100)
#    tree.column("shlfno.", width=80)
#    tree.column("publisher", width=100)
#    tree.column("price", width=100)
#    tree.heading("acn", text="Accession No.")
#    tree.heading("title", text="Title")
#    tree.heading("author", text="Author")
#    tree.heading("shlfno.", text="Shelf no")
#    tree.heading("publisher", text="Publisher")
##    tree.bind('<ButtonRelease-1>', selectItem)
#    tree.pack()
#    mainloop()




def start_listAllbooks_win():
    book_win = tk.Tk()
    book_win.title("List All books")
    book_win.geometry("960x600")

    allBooks = list_allbooks()

    #print(book_schema)


    tree = ttk.Treeview(book_win)

    tree["columns"]=("acn", "title", "author", "shlfno.", "publisher", "price")

    tree.column("acn", width=100)
    tree.column("title", width=150)
    tree.column("author", width=100)
    tree.column("shlfno.", width=80)
    tree.column("publisher", width=100)
    tree.column("price", width=100)
    tree.heading("acn", text="Accession No.")
    tree.heading("title", text="Title")
    tree.heading("author", text="Author")
    tree.heading("shlfno.", text="Shelf no")
    tree.heading("publisher", text="Publisher")
    tree.heading("price", text="Price")

    for book in allBooks:
        tree.insert('',0, text='', value = book)
    #tree.insert("" , 1, text="Line 1", values=("1A","1b"))
    tree.pack()
    book_win.mainloop()





def start_addbook_win():
    book_win = tk.Tk()
    book_win.title("Add New Book")
    book_win.geometry("900x600+300+300")
    #book_win.overrideredirect(1)  ## removes the title bar and min/max/close default options
    def addBook():
        status = add_new_book(book_win_acno.get(), book_win_title.get(), book_win_price.get(), book_win_author.get(), book_win_pub.get())
        if status!=0:
            messagebox.showinfo('Error','Accession Number already exist')


    Label(book_win, text="Accession Number:").grid(row=1,column=4)
    Label(book_win, text="Title:").grid(row=2,column=4)
    Label(book_win, text="Price:").grid(row=3,column=4)
    Label(book_win, text="Author:").grid(row=4, column=4)
    Label(book_win, text="Publisher:").grid(row=5, column=4)

    book_win_acno = Entry(book_win)
    book_win_title = Entry(book_win)
    book_win_price = Entry(book_win)
    book_win_author = Entry(book_win)
    book_win_pub = Entry(book_win)

    book_win_acno.grid(row=1,column=5)
    book_win_title.grid(row=2,column=5)
    book_win_price.grid(row=3,column=5)
    book_win_author.grid(row=4,column=5)
    book_win_pub.grid(row=5,column=5)

    Button(book_win, text='Add Book', command = addBook).grid(row=7,column=4,sticky=W, pady=4)
    Button(book_win, text='Close', command = book_win.destroy).grid(row=7,column=5,sticky=W, pady=4)
