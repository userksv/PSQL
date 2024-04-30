"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-cross-join/
In PostgreSQL, a cross-join allows you to join two tables by combining each row from 
    the first table with every row from the second table, resulting in a complete combination of all rows.
Use the PostgreSQL CROSS JOIN clause to make a cartesian product of rows in two tables.    
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def cross_join():
    sql = """SELECT * FROM T1 CROSS JOIN T2;"""
    sql = """SELECT * FROM T1, T2;""" # same query
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
        print(record)

# cross_join()