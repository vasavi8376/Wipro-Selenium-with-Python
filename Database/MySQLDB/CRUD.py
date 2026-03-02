import mysql.connector
# create the connection to mysql database

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lalitha@123"
)

cursor = connection.cursor()
print("Connected successfully")

cursor.execute("CREATE DATABASE IF NOT EXISTS school")
connection.commit()

# Now reconnection with database:
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lalitha@123",
    database="school"
)

cursor = connection.cursor()
print("Connected successfully to school database")

# create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
studentid INT AUTO_INCREMENT PRIMARY KEY,
studentname VARCHAR(50),
subject VARCHAR(50),
marks INT)
''')
connection.commit()

# insert data
query = "INSERT INTO students(studentname, subject, marks) VALUES (%s, %s, %s)"
values = ("John", "Maths", 85)
cursor.execute(query, values)
connection.commit()

# insert multiple records
student_data = [
    ("Ravi", "Science", 90),
    ("Sneha", "Maths", 70),
    ("Kiran", "Physics", 85)
]
cursor.executemany(query, student_data)
connection.commit()

# read data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# update the data
cursor.execute("UPDATE students SET marks=95 WHERE studentname='John'")
connection.commit()

# delete data
cursor.execute("DELETE FROM students WHERE studentname='Sneha'")
connection.commit()

cursor.close()
connection.close()
print("Connection closed")