# Quiz
There is a Quiz which is based on Networking with database connectivity in Python.
Firstly, the user enters a username and password which is already registered in the Database.
If the login credentials are correct then the system displays the menu and according to the choice, the user can get the result, gives an exam, and see the rules also.

Database ==> project_networking_db

## Tables 
==> quiz and student

## schema of quiz table

Primary key -> id -> int(11) | question -> varchar(255) | op1 -> varchar(50) | op2 -> varchar(50) | op3 -> varchar(50)| op4 -> varchar(50) | answer -> varchar(50)


## schema of student table

Primary key -> id -> int(11) | username -> varchar(20) | password -> varchar(20)| email -> varchar(20) | result -> int(11)
