"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-intersect/

The INTERSECT operator returns a result set containing rows that are available in both result sets.
    Use the PostgreSQL INTERSECT operator to combine two result sets and return a single result set containing rows that appear in both result sets.
    Place the ORDER BY clause after the second query to sort the rows in the result set returned by the INTERSECT operator.
"""

from turtle import filling
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def intersect():
    # The filling statement uses the INTERSECT operator to find the most popular films which are also 
    # the top-rated films and sorts the films by release year:
    sql = """SELECT * FROM most_popular_films INTERSECT SELECT * FROM top_rated_films ORDER BY release_year;"""
    cur.execute(sql)
    films = cur.fetchall()
    for film in films:
        print(film)

intersect()