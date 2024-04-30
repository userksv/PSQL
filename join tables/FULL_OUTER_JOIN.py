"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-full-outer-join/
The FULL OUTER JOIN combine data from two tables and returns all rows from both tables, 
    including matching and non-matching rows from both sides.
In other words, the FULL OUTER JOIN combines the results of both the left join and the right join.

Use the PostgreSQL FULL OUTER JOIN clause to combine data from both tables, 
    ensuring that matching rows are included from both the left and right tables, as well as unmatched rows from either table.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def full_outer_join():
    # The following query uses the FULL OUTER JOIN to query data from both employees and departments tables:
    sql = """SELECT employee_name, department_name FROM employees e 
            FULL OUTER JOIN departments d ON d.department_id = e.department_id;"""
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
        print(record)

# full_outer_join()

def full_outer_join_where():
    # The following example use the FULL OUTER JOIN with a WHERE clause to find the department that does not have any employees:
    sql = """SELECT employee_name, department_name FROM employees e 
            FULL OUTER JOIN departments d ON d.department_id = e.department_id
            WHERE employee_name IS NULL;"""
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
        print(record)

# full_outer_join_where()