import sqlite3

def create_database(cursor):
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        group_id INTEGER NOT NULL,
        FOREIGN KEY (group_id) REFERENCES groups(id)
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Groups(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Teachers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subjects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        teacher_id INTEGER NOT NULL,
        FOREIGN KEY (teacher_id) REFERENCES Teachers(id)
        );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        subject_id INTEGER NOT NULL,
        grade INTEGER NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (student_id) REFERENCES Students(id),
        FOREIGN KEY (subject_id) REFERENCES Subjects(id)
        );
    """)