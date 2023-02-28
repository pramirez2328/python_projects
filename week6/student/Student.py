import sqlite3

'''
create a class Student usings sqlite3, with the following methods:
create_table, insert_student, get_students_by_name, get_students_by_age,
get_students_by_major, get_all_students, and __repr__
'''


class Student:
    def __init__(self, name='', age='', major=''):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        self.create_table()
        self.name = name
        self.age = age
        self.major = major

    def create_table(self):
        with self.conn:
            self.c.execute(
                '''CREATE TABLE IF NOT EXISTS students
                  (name TEXT,
                  age INTEGER,
                  major TEXT)
                '''
            )

    def insert_student(self, student):
        with self.conn:
            self.c.execute(
                "INSERT INTO students VALUES (?, ?, ?)",
                (student['name'], student['age'], student['major']),
            )

    def get_all_students(self):
        self.c.execute("SELECT * FROM students")
        return self.c.fetchall()


s1 = Student()

s1.insert_student({'name': 'Maria', 'age': 20, 'major': 'CS'})

print(s1.get_all_students())
