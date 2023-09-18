import mysql.connector

class Student:
    def __init__(self, student_id, first_name, last_name, gpa):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa

    def _connect_database():
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Gab$sign15",
                database="assignment"
            )
            return mydb
        except mysql.connector.Error as error:
            print(f"Error: {error}")
            return None

    def insert_student(self,):
        db_connection = self._connect_database()
        if db_connection is not None:
            try:
                cursor = db_connection.cursor()
                query = "INSERT INTO students (student_id, first_name, last_name, gpa) VALUES (%s, %s, %s, %s)"
                values = (self.student_id, self.first_name, self.last_name, self.gpa)
                cursor.execute(query, values)
                db_connection.commit()
                print("Student information inserted successfully.")
            except mysql.connector.IntegrityError as err:
                print(f"Error: Duplicate student ID - {err}")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            finally:
                cursor.close()
                db_connection.close()

    def get_student_by_id(self, student_id):
        db_connection = Student._connect_database()
        if db_connection is not None:
            try:
                cursor = db_connection.cursor()
                query = "SELECT * FROM students WHERE student_id = %s"
                cursor.execute(query, (student_id,))
                student_data = cursor.fetchone()
                if student_data:
                    student = Student(*student_data)
                    return student
                else:
                    print("Student ID not found.")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            finally:
                cursor.close()
                db_connection.close()

    def update_gpa(self):
        db_connection = self._connect_database()
        if db_connection is not None:
            try:
                cursor = db_connection.cursor()
                query = "UPDATE students SET gpa = %s WHERE student_id = %s"
                values = (self.gpa, self.student_id)
                cursor.execute(query, values)
                if cursor.rowcount > 0:
                    db_connection.commit()
                    print("GPA updated successfully.")
                else:
                    print("Student ID not found.")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            finally:
                cursor.close()
                db_connection.close()


if __name__ == "__main__":
    student1 = Student("1", "Gabriella", "Chinyere", 4.8)
    student1.insert_student()

    retrieved_student = Student.get_student_by_id("1")
    if retrieved_student:
        print(f"Student ID: {retrieved_student.student_id}")
        print(f"Name: {retrieved_student.first_name} {retrieved_student.last_name}")
        print(f"GPA: {retrieved_student.gpa}")

    student1.gpa = 4.0
    student1.update_gpa()
