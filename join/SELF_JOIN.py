"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-self-join/
A PostgreSQL self-join is a regular join that joins a table to itself using the INNER JOIN or LEFT JOIN.
Self-joins are very useful for querying hierarchical data or comparing rows within the same table.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def inner_join():
    # The following query finds all pairs of films that have the same length,
    sql = """SELECT f1.title, f2.title, f1.length FROM film f1 
            INNER JOIN film f2 ON f1.film_id > f2.film_id AND f1.length = f2.length;"""
    cur.execute(sql)
    films = cur.fetchmany(10)
    for film in films:
        print(film)

inner_join()