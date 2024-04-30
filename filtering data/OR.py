"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-or/
Use the OR operator to combine multiple boolean expressions.
"""

import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def where_OR():
    """The following example uses the OR operator in the WHERE clause to find the films that have a rental rate is 0.99 or 2.99:"""
    query = """SELECT title, rental_rate FROM film WHERE rental_rate = 0.99 OR rental_rate = 2.99"""
    cur.execute(query)
    films = cur.fetchmany(10)
    for film in films:
        print(film)

where_OR()