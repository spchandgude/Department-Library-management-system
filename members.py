import mysql.connector as ms
from db_credentials import setu


def get_memid(mem_name):
    id = setu.cursor()
    query = "SELECT member_id from members where full_name=\'"+mem_name+"\';"
    id.execute(query);

    mem_id = id.fetchall()
    if mem_id == []:
        return -1;
    else:
        return mem_id[0][0]




def add_new_member(m_type, m_mno, email_id,m_fullname):
    add = setu.cursor()
    query = "INSERT into members(member_type,mobile_number,email_id,full_name) values(%s,%s,%s,%s)"
    val = (m_type,m_mno,email_id,m_fullname)
    add.execute(query,val)
    setu.commit()
    print(add.rowcount," Member record inserted")



def display_all_members1():
    arz = setu.cursor()
    arz.execute("SELECT member_type, member_id, full_name, mobile_number, email_id FROM members")
    allMembers = arz.fetchall()
    return allMembers


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

def search_member_by_name1(m_name):
    arz = setu.cursor()
    query = "SELECT member_type, member_id, full_name, mobile_number, email_id FROM members where full_name like\'"+str(m_name)+"%\'"
    print(query)
    arz.execute(query)
    searchMember = arz.fetchall()

    print(searchMember)
    if searchMember == []:
        return -1;
    else:
        return searchMember;
    #return searchMember

def search_member_by_name(m_name):
    arz = setu.cursor()
    query = "SELECT * FROM members where full_name like\'"+str(m_name)+"%\'"
    print(query)
    arz.execute(query)
    searchMember = arz.fetchall()

    print(searchMember)
    if searchMember == []:
        return -1;
    else:
        return searchMember;
    #return searchMember
