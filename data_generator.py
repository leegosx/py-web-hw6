import random
from faker import Faker
from fake_subject_and_group import fake_subject, fake_group_name

fake = Faker()

def populate_teachers(cursor, num_teachers=5):
    for _ in range(num_teachers):
        teacher_name = fake.name()
        cursor.execute("""INSERT INTO Teachers (name) VALUES (?);""", 
                       (teacher_name,))
        

def populate_subjects(cursor, num_subjects=8):
    #Запит для отримання всіх ID викладачів
    cursor.execute("""SELECT id FROM Teachers;""")
    teacher_ids = [row[0] for row in cursor.fetchall()]
    
    for _ in range(num_subjects):
        subject_name = fake_subject()
        teacher_id = random.choice(teacher_ids)
        cursor.execute("""INSERT INTO Subjects (name, teacher_id) VALUES (?, ?);""",
                       (subject_name, teacher_id))


def populate_students(cursor, num_students=50):
    #Запит для отримання всіх ID груп
    cursor.execute("""SELECT id FROM Groups;""")
    group_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(num_students):
        student_name = fake.name()
        group_id = random.choice(group_ids)
        cursor.execute("""INSERT INTO Students (name, group_id) VALUES (?, ?);""", 
                       (student_name, group_id))
    

def populate_groups(cursor, num_groups=3):
    for _ in range(num_groups):
        group_name = fake_group_name()
        cursor.execute("""INSERT INTO Groups (name) VALUES (?);""", (group_name,))


def populate_grades(cursor, num_grades_per_student=20):
    #Запит для отримання всіх ID студентів та предметів
    cursor.execute("""SELECT id FROM Students;""")
    student_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("""SELECT id FROM Subjects;""")
    subject_ids = [row[0] for row in cursor.fetchall()]
    
    for student_id in student_ids:
        for _ in range(num_grades_per_student):
            subject_id = random.choice(subject_ids)
            grade = fake.random_element(elements=(1, 2, 3, 4, 5))
            date = fake.date_this_year()
            cursor.execute("INSERT INTO Grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?);",
                           (student_id, subject_id, grade, date))