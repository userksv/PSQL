"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-left-join/
The LEFT JOIN clause joins a left table with the right table and returns the rows from the left table that 
    may or may not have corresponding rows in the right table.
The LEFT JOIN can be useful for selecting rows from one table that do not have matching rows in another.
If the columns for joining two tables have the same name, you can use the USING syntax

Use the PostgreSQL LEFT JOIN clause to select rows from one table that may or may not have corresponding rows in other tables.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def left_join():
    # The following statement uses the LEFT JOIN clause to join film table with the inventory table:
    sql = """SELECT film.film_id, film.title, inventory.inventory_id FROM film 
            LEFT JOIN inventory ON inventory.film_id = film.film_id ORDER BY film.title;"""

    # Because the film and inventory tables share the same film_id column, you can use the USING syntax:
    sql = """SELECT f.film_id, f.title, i.inventory_id FROM film f
            LEFT JOIN inventory i USING (film_id) ORDER BY i.inventory_id;"""
    
    cur.execute(sql)
    records = cur.fetchall()
    desc = cur.description
    for record in records:
        print(record)
    print(desc)

# left_join()

def left_join_where():
    # The following uses the LEFT JOIN clause to join the inventory and film tables. 
    # It includes a WHERE clause that identifies the films that are not present in the inventory
    sql = """SELECT f.film_id, f.title, i.inventory_id FROM film f 
            LEFT JOIN inventory i USING (film_id) 
            WHERE i.film_id IS NULL ORDER BY f.title;"""
    cur.execute(sql)
    records = cur.fetchall()
    desc = cur.description
    for record in records:
        print(record)
    print(desc)

left_join_where()