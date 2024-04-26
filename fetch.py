"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-fetch/
The FETCH clause is functionally equivalent to the LIMIT clause. If you plan to make your application compatible 
with other database systems, you should use the FETCH clause because it follows the standard SQL.

OFFSET row_to_skip { ROW | ROWS }
FETCH { FIRST | NEXT } [ row_count ] { ROW | ROWS } ONLY

Use the PostgreSQL FETCH clause to skip a certain number of rows and retrieve a specific number of rows from a query.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def fetch():
    # The following query uses the FETCH clause to select the first film sorted by titles in ascending order:
    query = """SELECT film_id, title FROM film ORDER BY title FETCH FIRST ROW ONLY;"""
    cur.execute(query)
    films = cur.fetchall()
    for film in films:
        print(film)
    
# fetch()

def fecth_first_five():
    # The following query uses the FETCH clause to select the first five films sorted by titles:
    query = """SELECT film_id, title FROM film ORDER BY title FETCH FIRST 5 ROW ONLY"""
    cur.execute(query)
    films = cur.fetchall()
    for film in films:
        print(film)
    
# fecth_first_five()

def fetch_first_five_offset():
    # The following statement returns the next five films after the first five films sorted by titles:
    query = """SELECT film_id, title FROM film ORDER BY title OFFSET 5 ROWS FETCH FIRST 5 ROW ONLY"""
    cur.execute(query)
    films = cur.fetchall()
    for film in films:
        print(film)

# fetch_first_five_offset()

