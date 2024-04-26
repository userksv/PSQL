"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-limit/
PostgreSQL LIMIT is an optional clause of the SELECT statement that constrains the number of rows returned by the query.
Use the PostgreSQL LIMIT OFFSET clause to retrieve a subset of rows returned by a query.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def limit():
    """The following statement uses the LIMIT clause to get the first five films sorted by film_id"""
    query = """SELECT film_id, title, release_year FROM film ORDER BY film_id LIMIT 5"""
    cur.execute(query)
    films = cur.fetchall()
    for film in films:
        print(film)

# limit()

def limit_offset():
    """To retrieve 4 films starting from the fourth one ordered by film_id, you can use both LIMIT and OFFSET clauses as follows"""
    query = """SELECT film_id, title, release_year FROM film ORDER BY film_id LIMIT 4 OFFSET 3"""
    cur.execute(query)
    films = cur.fetchall()
    for film in films:
        print(film)
    
# limit_offset()

def limit_0ffset_top_N_bottom():
    """The following example uses the LIMIT clause to retrieve the top 10 most expensive films by rental rate:"""
    query = """SELECT film_id, title, rental_rate FROM film ORDER BY rental_rate DESC LIMIT 10"""
    cur.execute(query)
    films = cur.fetchall()
    for film in films:
        print(film)

limit_0ffset_top_N_bottom()