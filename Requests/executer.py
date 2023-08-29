import sqlite3
from prettytable import PrettyTable


def connect_to_data_base(data_base, query_file_name) -> list():
    # Connect to the database
    conn = sqlite3.connect(data_base)
    cursor = conn.cursor()

    # Read the SQL queries from the file
    with open(query_file_name, "r") as query_file:
        queries = query_file.read().split(';')

    # Execute each query
    for query in queries:
        if query.strip():
            cursor.execute(query)

    results = cursor.fetchall()
    conn.close()
    return results



def create_prettytable(header_first, header_second, header_three, data_base_results):
    table = PrettyTable()
    if header_second:
        table.field_names = [header_first, header_second, header_three]
    else:
        table.field_names = [header_first]
    for row in data_base_results:
        table.add_row(row)
    return table

def create_prettytable_for_two_colums(header_first, header_second, data_base_results):
    table = PrettyTable()
    if header_second:
        table.field_names = [header_first, header_second]
    else:
        table.field_names = [header_first]
    for row in data_base_results:
        table.add_row(row)
    return table

def first_query():
    con_result = connect_to_data_base(db_path, "query_1.sql")
    print(create_prettytable("Student ID", "Name", "Average GPA", con_result))

def second_query():
    con_result = connect_to_data_base(db_path, "query_2.sql")
    print(create_prettytable("Student ID", "Name", "Average GPA in Mathematics", con_result))

def third_query():
    con_result = connect_to_data_base(db_path, "query_3.sql")
    print(create_prettytable_for_two_colums("Subject & Auditorium", "Average GPA", con_result))
    
def fourth_query():
    con_result = connect_to_data_base(db_path, "query_4.sql")
    print(create_prettytable_for_two_colums("Average GPA in all Stream", None, con_result))
    
def fifth_query():
    con_result = connect_to_data_base(db_path, "query_5.sql")
    print(create_prettytable_for_two_colums("Teacher", "Subject", con_result))
    
def sixth_query():
    con_result = connect_to_data_base(db_path, "query_6.sql")
    print(create_prettytable_for_two_colums("Student's from group 2", None, con_result))
    
def seventh_query():
    con_result = connect_to_data_base(db_path, "query_7.sql")
    print(create_prettytable_for_two_colums("Student's from group 3", "Anthropology Grade", con_result))
    
def eighth_query():
    con_result = connect_to_data_base(db_path, "query_8.sql")
    print(create_prettytable("Teacher", "Average GPA given in Geograph", None, con_result))
    
def ninth_query():
    con_result = connect_to_data_base(db_path, "query_9.sql")
    print(create_prettytable_for_two_colums("Subjects visited by David Smith", None, con_result))
    
def tenth_query():
    con_result = connect_to_data_base(db_path, "query_10.sql")
    print(create_prettytable_for_two_colums("Student", "Subjects of Katherine Griffin", con_result))

def first_additional_query():
    con_result = connect_to_data_base(db_path, "additional_query.sql")
    print(create_prettytable_for_two_colums("Average GPA given by Fernando Vincent to Melissa Lindsey",None, con_result))

def second_additional_query():
    con_result = connect_to_data_base(db_path, "additional_query_2.sql")
    print(create_prettytable_for_two_colums("Student of group 2", "Grades of Architecture on last lesson", con_result))
    
db_path = "D:/IT_S/py-web-hw6/Data/university.db"

if __name__ == "__main__":
    first_query()
    second_query()
    third_query()
    fourth_query()
    fifth_query()
    sixth_query()
    seventh_query()
    eighth_query()
    ninth_query()
    tenth_query()
    first_additional_query()
    second_additional_query()