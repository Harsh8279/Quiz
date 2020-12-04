# Quiz
There is a Quiz which is based on Networking with database connectivity in Python.
Firstly, the user enters a username and password which is already registered in the Database.
If the login credentials are correct then the system displays the menu and according to the choice, the user can get the result, gives an exam, and see the rules also.

Database ==> project_networking_db

## Tables 

+---------------------------------+
| Tables_in_project_networking_db |
+---------------------------------+
| quiz                            |
| student                         |
+---------------------------------+

## schema of quiz table

+----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| id       | int(11)      | NO   | PRI | NULL    |       |
| question | varchar(255) | NO   |     | NULL    |       |
| op1      | varchar(50)  | NO   |     | NULL    |       |
| op2      | varchar(50)  | NO   |     | NULL    |       |
| op3      | varchar(50)  | NO   |     | NULL    |       |
| op4      | varchar(50)  | NO   |     | NULL    |       |
| answer   | varchar(50)  | NO   |     | NULL    |       |
+----------+--------------+------+-----+---------+-------+


