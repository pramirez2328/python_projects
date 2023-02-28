import sqlite3
from Student import Student

conn = sqlite3.connect(':memory:')

c = conn.cursor()


def insert_student(student):
    with conn:
        c.execute(
            "INSERT INTO students VALUES (:name, :age, :major)",
            {'name': student.name, 'age': student.age, 'major': student.major},
        )


def get_students_by_name(name):
    c.execute("SELECT * FROM students WHERE name=:name", {'name': name})
    return c.fetchall()


def get_students_by_age(age):
    c.execute("SELECT * FROM students WHERE age=:age", {'age': age})
    return c.fetchall()


def get_students_by_major(major):
    c.execute("SELECT * FROM students WHERE major=:major", {'major': major})
    return c.fetchall()


def get_all_students():
    c.execute("SELECT * FROM students")
    return c.fetchall()


c.execute('''CREATE TABLE students (name text, age integer, major text)''')

s1 = Student('Maria', 20, 'CS')
s2 = Student('Pedro', 27, 'AD')

insert_student(s1)
insert_student(s2)

print(get_all_students())


conn.close()
