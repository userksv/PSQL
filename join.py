"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-joins/
PostgreSQL supports inner join, left join, right join, full outer join, cross join, natural join, 
and a special kind of join called self-join.
"""

import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def inner_join():
    # The following statement joins the first table (basket_a) with the second table (basket_b)
    # by matching the values in the fruit_a and fruit_b columns
    query = """SELECT a, fruit_a, b, fruit_b FROM basket_a INNER JOIN basket_b ON fruit_a = fruit_b"""
    cur.execute(query)
    fruits = cur.fetchall()
    for f in fruits:
        print(f)

# inner_join()

def left_join():
    # The following statement uses the left join clause to join the basket_a table with the basket_b table. 
    # In the left join context, the first table is called the left table and the second table is called the right table.
    query = """SELECT a, fruit_a, b, fruit_b FROM basket_a LEFT JOIN basket_b ON fruit_a = fruit_b"""
    cur.execute(query)
    fruits = cur.fetchall()
    for f in fruits:
        print(f)

# left_join()

def left_outer_join():
    # To select rows from the left table that do not have matching rows in the right table, 
    # you use the left join with a WHERE clause. For example:
    query = """SELECT a, fruit_a, b, fruit_b FROM basket_a LEFT JOIN basket_b ON fruit_a = fruit_b WHERE b IS NULL"""
    cur.execute(query)
    fruits = cur.fetchall()
    for f in fruits:
        print(f)

# left_outer_join()

def right_join():
    # The following statement uses the right join to join the basket_a table with the basket_b table:
    query = """SELECT a, fruit_a, b, fruit_b FROM basket_a RIGHT JOIN basket_b ON fruit_a = fruit_b"""
    cur.execute(query)
    fruits = cur.fetchall()
    for f in fruits:
        print(f) 

# right_join()

def right_outer_join():
    # The following statement uses the right join to join the basket_a table with the basket_b table:
    query = """SELECT a, fruit_a, b, fruit_b FROM basket_a RIGHT JOIN basket_b ON fruit_a = fruit_b WHERE a IS NULL"""
    cur.execute(query)
    fruits = cur.fetchall()
    for f in fruits:
        print(f) 

right_outer_join()

def full_outer_join():
    # The full outer join or full join returns a result set that contains all rows from both left and right tables, 
    # with the matching rows from both sides if available. 
    # In case there is no match, the columns of the table will be filled with NULL.
    query = """SELECT a, fruit_a, b, fruit_b FROM basket_a FULL OUTER JOIN basket_b ON fruit_a = fruit_b"""
    cur.execute(query)
    fruits = cur.fetchall()
    for f in fruits:
        print(f) 

# full_outer_join()

def full_join_is_null():
    # To return rows in a table that do not have matching rows in the other, you use the full join with a WHERE clause like this:
    query = """SELECT a, fruit_a, b, fruit_b FROM basket_a FULL OUTER JOIN basket_b ON fruit_a = fruit_b
                WHERE a IS NULL OR b IS NULL"""
    cur.execute(query)
    fruits = cur.fetchall()
    for f in fruits:
        print(f) 

full_join_is_null()