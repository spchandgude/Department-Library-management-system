import mysql.connector as ms
from db_credentials import setu

def is_book_available(book_acn):
    status = setu.cursor()
    print(book_acn)
    query = "SELECT is_available from books where accession_number =\'"+book_acn+"\';";
    print(query)
    #try

    status.execute(query);
    state = status.fetchall()
    print(state)
    return state[0][0];
    #if state[0][0] ==0:
    #    return 0;
    #else:
    #    return ;



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
    query = "SELECT accession_number, title, author, shelf_no, publisher, price from books where "+searchby+" like \'"+searchfor+"%\';"
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
