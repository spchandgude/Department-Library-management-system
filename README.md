# deplib
Library Management System for Departmental Library of my College

Library Management System for Departmental Library of my College // Comming soon.

ysql> show tables -> ; +------------------+ | Tables_in_deplib | +------------------+ | books | | borrows | | librarian | | members | +------------------+ 4 rows in set (0.00 sec)

mysql> desc books; +------------------+--------------+------+-----+---------+----------------+ | Field | Type | Null | Key | Default | Extra | +------------------+--------------+------+-----+---------+----------------+ | accession_number | varchar(30) | NO | PRI | NULL | | | shelf_no | varchar(10) | YES | | NULL | | | title | varchar(120) | YES | | NULL | | | price | float | YES | | NULL | | | author | varchar(200) | YES | | NULL | | | sno | int(11) | NO | UNI | NULL | auto_increment | | publisher | varchar(50) | YES | | NULL | | | is_available | tinyint(4) | YES | | NULL | | +------------------+--------------+------+-----+---------+----------------+ 8 rows in set (0.00 sec)

mysql> desc members; +---------------+-------------+------+-----+---------+----------------+ | Field | Type | Null | Key | Default | Extra | +---------------+-------------+------+-----+---------+----------------+ | member_type | varchar(7) | YES | | NULL | | | member_id | int(11) | NO | PRI | NULL | auto_increment | | mobile_number | varchar(12) | YES | | NULL | | | email_id | varchar(45) | YES | | NULL | | | full_name | varchar(70) | YES | UNI | NULL | | +---------------+-------------+------+-----+---------+----------------+ 5 rows in set (0.00 sec)

mysql> desc borrows; +-----------------------+-------------+------+-----+---------+----------------+ | Field | Type | Null | Key | Default | Extra | +-----------------------+-------------+------+-----+---------+----------------+ | transaction_id | int(11) | NO | PRI | NULL | auto_increment | | issue_date | date | YES | | NULL | | | return_date | date | YES | | NULL | | | issue_time | time | YES | | NULL | | | return_time | time | YES | | NULL | | | remarks | varchar(90) | YES | | NULL | | | issuers_member_id | int(11) | YES | | NULL | | | book_accession_number | varchar(30) | YES | | NULL | | +-----------------------+-------------+------+-----+---------+----------------+ 8 rows in set (0.00 sec)

mysql> desc librarian; +-----------+-------------+------+-----+---------+-------+ | Field | Type | Null | Key | Default | Extra | +-----------+-------------+------+-----+---------+-------+ | full_name | varchar(60) | NO | PRI | NULL | | | username | varchar(30) | YES | | NULL | | | password | varchar(25) | YES | | NULL | | +-----------+-------------+------+-----+---------+-------+ 3 rows in set (0.14 sec)

mysql>
