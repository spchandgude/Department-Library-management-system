import mysql.connector as ms
from db_credentials import setu
from datetime import datetime
from books import is_book_available
from members import get_memid



def getAllUnreturnedBooks():
    arz = setu.cursor()
    query = "select borrows.book_accession_number, books.title, members.full_name, borrows.issue_date, members.mobile_number from((borrows inner join members on borrows.issuers_member_id = members.member_id and return_date is null) inner join books on borrows.book_accession_number = books.accession_number) order by borrows.issue_date desc;"
    print(query)
    arz.execute(query)
    books = arz.fetchall()
    print(books)
    if books==[] :
        return -1;
    else:
        return books;


def getUnreturnedBooks(searchBy,searchFor):
    arz = setu.cursor()
    query = """select borrows.book_accession_number, books.title, members.full_name, borrows.issue_date, members.mobile_number
    from((borrows inner join members on borrows.issuers_member_id = members.member_id and return_date is null)
    inner join books on borrows.book_accession_number = books.accession_number)
    where """+searchBy+""" like \'"""+searchFor+"""%\'
    order by borrows.issue_date desc ;"""
    print(query)
    arz.execute(query)
    books = arz.fetchall()
    print(books)
    if books == []:
        return -1;
    else:
        return books;


def issue_book(mem_name, book_acn):
    issue = setu.cursor()
    print("@issue book:")
    print(book_acn)
    print()
    status= is_book_available(book_acn)
    print(status)
    if status:

        mem_id = get_memid(mem_name);
        print(mem_id)
        if mem_id == -1:
            print('member dont exists')
            return -1;      # wrong member id

        else:
            query = "insert into borrows (issue_date, issue_time, issuers_member_id, book_accession_number) values(CURDATE(), CURTIME(), %s, %s)"
            query2 = "update books set is_available = 0 where accession_number=\'"+book_acn+"\';"
            val = (mem_id, book_acn)

            #exceptions
            issue.execute(query,val)
            setu.commit()
            issue.execute(query2)
            setu.commit()

            print("Book issued")
    else:
        return -2;      #book is not available



def return_book(mem_id, book_acn, remarks=""):
    wapas = setu.cursor()
    query = "update borrows set return_date = CURDATE(), return_time=CURTIME(), remarks=%s where issuers_member_id=%s and book_accession_number=%s;";
    val = (remarks, mem_id, book_acn)

    wapas.execute(query,val)
    setu.commit()
    print(wapas)
    print(wapas.fetchall)
    print("Book returned");



def all_issued_books():
    listall = setu.cursor()
    query = "select * from borrows where return_date is null;"
    listall.execute(query)
    return listall.fetchall()
