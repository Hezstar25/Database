import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Gab$sign15',
    database = 'assigment'
)

cursor = mydb.cursor()

cursor.execute(
    'CREATE TABLE if not exists studentid(INT AUTO_INCREMENT PRIMARY KEY student_id, first_name VARCHAR(225) NOT NULL, last_name VARCHAR(255)NOT NULL, gpa INT(4) NOT NULL) VALUES("1", "Chinyere", "Godwin", 4.9)'
)