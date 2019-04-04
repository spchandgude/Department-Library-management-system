Framework:
Database, Actions, templates

************************Database****************************

dbname is 'deplib' @ mysql

Entities:

1)Books

mysql> desc books;
+------------------+--------------+------+-----+---------+-------+
| Field            | Type         | Null | Key | Default | Extra |
+------------------+--------------+------+-----+---------+-------+
| accession_number | varchar(30)  | NO   | PRI | NULL    |       |
| shelf_no         | varchar(10)  | YES  |     | NULL    |       |
| title            | varchar(50)  | YES  |     | NULL    |       |
| price            | float        | YES  |     | NULL    |       |
| author           | varchar(200) | YES  |     | NULL    |       |
| quantity         | int(11)      | YES  |     | NULL    |       |
+------------------+--------------+------+-----+---------+-------+
6 rows in set (0.11 sec)

2)Members
mysql> desc members;
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| member_type   | varchar(7)  | YES  |     | NULL    |                |
| member_id     | int(11)     | NO   | PRI | NULL    | auto_increment |
| mobile_number | varchar(12) | YES  |     | NULL    |                |
| email_id      | varchar(45) | YES  |     | NULL    |                |
| full_name     | varchar(70) | YES  | UNI | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

3)borrows

+----------------------+-------------+------+-----+---------+----------------+
| Field                | Type        | Null | Key | Default | Extra          |
+----------------------+-------------+------+-----+---------+----------------+
| transaction_id       | int(11)     | NO   | PRI | NULL    | auto_increment |
| issue_date           | date        | YES  |     | NULL    |                |
| return_date          | date        | YES  |     | NULL    |                |
| issue_time           | time        | YES  |     | NULL    |                |
| return_time          | time        | YES  |     | NULL    |                |
| remarks              | varchar(90) | YES  |     | NULL    |                |
| issuers_member_id    | int(11)     | YES  |     | NULL    |                |
| book_accesion_number | varchar(30) | YES  |     | NULL    |                |
+----------------------+-------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)
