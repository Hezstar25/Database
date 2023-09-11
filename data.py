import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Gab$sign15',
    database = 'mydatabase'
)

cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE mydatabase")
cursor.execute('CREATE TABLE teacher(id INT PRIMARY KEY AUTO_INCREMENT, name VACHAAR(25), course TEXT, age INT )')

print(mydb)