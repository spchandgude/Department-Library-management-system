import mysql.connector as ms
from db_credentials import setu


def add_new_member(m_type, m_mno, email_id,m_fullname):
    add = setu.cursor()
    query = "INSERT into members(member_type,mobile_number,email_id,full_name) values(%s,%s,%s,%s)"
    val = (m_type,m_mno,email_id,m_fullname)
    add.execute(query,val)
    setu.commit()
    print(add.rowcount," Member record inserted")


def display_all_members():
    arz = setu.cursor()
    arz.execute("SELECT * FROM members")
    allMembers = arz.fetchall()
    return allMembers

def search_member_by_id(m_id):
    arz = setu.cursor()
    query = "SELECT * FROM members where member_id="+str(m_id)
    arz.execute(query)
    searchMember = arz.fetchall()
    return searchMember

def search_member_by_name(m_name):
    arz = setu.cursor()
    query = "SELECT * FROM members where full_name="+str(m_name)
    arz.execute(query)
    searchMember = arz.fetchall()
    return searchMember
