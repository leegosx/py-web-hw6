# Data Generator and Query Executor

## Overview

This project aims to generate a SQLite database with fake data and execute SQL queries on it. The project consists of multiple Python files and SQL query files to handle the database creation, data generation, and query execution.

## Files Description

### Python Files

- `main.py`: The main entry point of the application. It imports functions from other Python files to create the database and populate it with data.
- `database.py`: Contains functions to create the SQLite database and its tables.
- `data_generator.py`: Provides functions to generate fake data for the database using the Faker library.
- `fake_subject_and_group.py`: Generates random subjects and group names.
- `executer.py`: Executes SQL queries on the SQLite database and returns the results.

### SQL Files
- `query_1.sql, query_2.sql, query_3.sql, query_4.sql, query_5.sql, query_6.sql, query_7.sql, query_8.sql, query_9.sql, and query_10.sql`: These files contain different SQL queries to perform specific tasks on the database.
`additional_query.sql`: An additional SQL query for specialized tasks.
`additional_query_2.sql`: Another additional SQL query for specialized tasks.


## SQL Query Descriptions
`query_1.sql`: Identifies the top 5 students with the highest average scores across all subjects.
`query_2.sql`: Determines the student with the highest average score in a particular subject.
`query_3.sql`: Calculates the average score in groups for a specific subject.
`query_4.sql`: Computes the average score across the entire grades table.
`query_5.sql`: Lists the courses taught by a specific teacher.
`query_6.sql`: Displays the list of students in a specific group.
`query_7.sql`: Provides the grades of students in a specific group for a particular subject.
`query_8.sql`: Finds the average grade given by a specific teacher across their subjects.
`query_9.sql`: Shows the list of courses attended by a specific student.
`query_10.sql`: Lists the courses taught by a specific teacher to a particular student.


## Additional SQL Query Descriptions
`additional_query.sql`: Computes the average grade that a specific teacher gives to a particular student.
`additional_query_2.sql`: Displays the grades of students in a specific group for a particular subject in the last lesson.


## How to Use

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run `python main.py` to create and populate the database.
4. Run `python executer.py` to execute SQL queries.

## Dependencies

- Python 3.11.4
- SQLite
- PrettyTable
- Faker library

## Author

[Dmytro Klymenko]

## License

MIT License
