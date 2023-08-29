from database import create_database
from data_generator import (
    populate_teachers,
    populate_subjects,
    populate_students,
    populate_grades,
    populate_groups
)

import sqlite3

def main():
    conn = sqlite3.connect('Data/University.db')
    cursor = conn.cursor()

    create_database(cursor)
    
    populate_groups(cursor)
    populate_teachers(cursor)
    populate_subjects(cursor)
    populate_students(cursor)
    populate_grades(cursor)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()