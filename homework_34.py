"""
Task 1

Create a table

Create a table of your choice inside the sample
SQLite database, rename it, and add a new column. Insert a couple rows inside your table.
Also, perform UPDATE and DELETE statements on inserted rows.

As a solution to this task, create a file named: task1.sql, with all the SQL
statements you have used to accomplish this task
"""

import sqlite3

def make_query(connection,query):
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()

if __name__ == '__main__':
    connection = sqlite3.connect("homework_34.db")
    make_query(connection,
    """
    CREATE TABLE IF NOT EXISTS Songs (
    Id INTEGER PRIMARY KEY,
    Band TEXT,
    Title TEXT,
    Album TEXT,
    Year INTEGER,
    Length TEXT,
    Genre TEXT)
    """)

    make_query(connection,
    """
    INSERT OR IGNORE INTO Songs VALUES(1,'WHILE SHE SLEEPS','FAKERS PLAGUE','SLEEPS SOCIETY',2022,'5:53','METALCORE')
    """)

    make_query(connection,
    """
    INSERT OR IGNORE INTO Songs VALUES(2,'WHILE SHE SLEEPS','ANTI-SOCIAL','SO WHAT?',2019,'4:14','METALCORE')
    """)

    make_query(connection,
    """
    INSERT OR IGNORE INTO Songs VALUES(3,'DEFTONES','CHANGE','WHITE PONY',2000,'4:59','ALTERNATIVE')
    """)

    make_query(connection,
    """
    UPDATE Songs
    SET Genre='ROCK'
    WHERE Genre='METALCORE'
    """)

    make_query(connection,
    """
    DELETE FROM Songs WHERE Band='WHILE SHE SLEEPS'              
    """)

"""
TASK 2 

1)
SELECT
e.first_name as FirstName,  e.last_name as LastName
FROM employees as e

2)
SELECT
DISTINCT(e.department_id)
FROM employees as e

3)
SELECT
*
FROM employees as e
ORDER by e.first_name DESC

4)
SELECT
e.first_name as FirstName,  e.last_name as LastName,
e.salary as Salary,  e.salary/100*12  as PF
FROM employees as e

5)
SELECT
MIN(e.salary), MAX(e.salary)
FROM employees as e

6)
SELECT
Round((e.salary/12),2)
FROM employees as e
"""