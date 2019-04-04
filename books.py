import mysql.connector as ms
from db_credentials import setu

def add_new_book(acn, title, price, author, publisher):
    add = setu.cursor()
    query = "INSERT INTO books(accession_number, title, price, author, publisher) values(%s,%s,%s,%s,%s)"
    val = (acn, title, price, author, publisher)
    try:
        add.execute(query,val)

    except ms.IntegrityError as err:
        err_msg="Error: {}".format(err)
        return err_msg
    setu.commit()
    print(str(add.rowcount)+" Book added Successfully");
    return 0;

def search_book(searchby,searchfor):
    arz = setu.cursor()
    query = "SELECT accession_number, title, author, shelf_no, publisher, price from books where " + searchby + "=" + "\'" + searchfor + "\'"
    print(query)
    arz.execute(query)
    book = arz.fetchall()
    if book == []:
        return -1
    else:
        return book;

def list_allbooks(orderby="accession_number"):
    lst = setu.cursor()
    query = "SELECT accession_number, title, author, shelf_no, publisher, price from books order by " +orderby+ " " + "desc;"
    lst.execute(query)
    allBooks = lst.fetchall()
    return allBooks

def get_book_schema():
    sch = setu.cursor()
    sch.execute("desc books")
    bookSchema = sch.fetchall()
    return bookSchema
