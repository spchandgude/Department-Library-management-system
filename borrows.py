import mysql.connector as ms
from db_credentials import setu
from datetime import datetime


#checking is book is already issued or not
def is_book_available(book_acn):
    status = setu.cursor()

    query = "Select return_date from borrows where book_accession_number = \'"+book_acn+"\';"

    status.execute(query)

    temp = status.fetchall()
    if temp == []:
        return 0;
    else:
        return 1;


# if the book is issued,,then its issued by whom ----->
def book_borrowed_by(book_acn):
#    print(is_book_available(book_acn))
    if (is_book_available(book_acn)):

        name = setu.cursor()
        query = "SELECT member_id, full_name from members inner join borrows on borrows.issuers_member_id = members.member_id where book_accession_number =\'"+book_acn+"\';"

        name.execute(query);
        print(str(name.fetchall())


print(book_borrowed_by('4'));

def issue_book(mem_id, book_acn):
    issue.cursor()

    if is_book_available(book_acn):

        query = "insert into borrows (issue_date, issue_time, issuers_member_id, book_accession_number,remarks) values(CURDATE(), CURTIME(), %s, %s)"
        val = (mem_id, book_acn)

        #exceptions
        issue.execute(query,val)
        setu.commit()
        print("Book issued")

#    elsif (is_book_available(book_acn)) == 0:
