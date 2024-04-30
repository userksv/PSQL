"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-and/

Use the AND operator to combine multiple boolean expressions.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def where_AND():
    """The following example uses the AND operator in the WHERE clause to find the films 
    that have a length greater than 180 and a rental rate less than 1:"""

    query = """SELECT title, length, rental_rate FROM film WHERE length > 180 AND rental_rate < 1"""
    cur.execute(query)
    films = cur.fetchall()
    for film in films:
        print(film)

# where_AND()