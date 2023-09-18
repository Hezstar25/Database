import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Gab$sign15',
    database = 'company'
)


cursor = mydb.cursor()

cursor.execute(
    # 'INSERT INTO staff(firstname, lastname, address, salary) VALUES ("John", "JAmes", "Abuja, Nigeria", 100000)'
    'INSERT INTO staff(firstname, lastname, address, salary) VALUES (%s, %s, %s, %s)', ('Onyi', 'Amaka','Newcastle', 500000)

)
mydb.commit()

cursor.execute('SELECT * FROM staff')
result = cursor.fetchall()
print(result)

# mycursor.execute("SHOW DATABASES")
# cursor.execute('CREATE TABLE teacher(id INT PRIMARY KEY , name VACHAAR(25), course TEXT, age INT )')
# for db in mycursor:
    # print(db)

# mycursor.execute("CREATE TABLE CLASS(id INT PRIMARY KEY, name VARCHAR(25), age INT(2))")

# mycursor.execute("SHOW TABLEs")
# for tb in mycursor:
    # print(tb)
    # mycursor = mycursor.execute("CREATE DATABASE company")
# print(mydb)
# mycursor.execute(
#     "CREATE TABLE if not exists staff(id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(50) NOT NULL, lastname VARCHAR(50) NOT NULL, address TEXT, salary INT)"
# )

# 'INSERT INTO assignment(student_id, first_name, last_name, gpa), 