"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-except/

The EXCEPT operator returns distinct rows from the first (left) query that are not in the second (right) query.
    Use the PostgreSQL EXCEPT operator to combine rows from two result sets and return a result set containing rows
        from the first result set that do not appear in the second result set.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def _except():
    # The following statement uses the EXCEPT operator to find the top-rated films that are not popular:
    sql = """SELECT * FROM top_rated_films EXCEPT SELECT * FROM most_popular_films;"""
    cur.execute(sql)
    films = cur.fetchall()
    for film in films:
        print(film)

_except()