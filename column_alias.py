'''
A column alias allows you to assign a column or an expression in the select list of a SELECT
statement a temporary name. The column alias exists temporarily during the execution of the query.
Use double quotes (“) to surround column aliases that contain spaces.
'''

import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def col_alias():
    query = '''SELECT first_name AS alias_name FROM customer LIMIT 10'''
    cur.execute(query)
    first_name = cur.fetchall()
    print(first_name)

col_alias()

def col_alias_with_concat():
    query = """SELECT first_name || ' ' || last_name AS "full name" FROM customer LIMIT 10"""
    cur.execute(query)
    full_names = cur.fetchall()
    print(full_names)

col_alias_with_concat()

def col_names():
    cur.execute("Select * FROM customer LIMIT 0")
    colnames = [desc[0] for desc in cur.description]
    print(colnames)

col_names()