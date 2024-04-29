"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-right-join/
The RIGHT JOIN clause joins a right table with a left table and returns the rows from the
    right table that may or may not have matching rows in the left table.
Use the PostgreSQL RIGHT JOIN clause to join a right table with a left table and return 
    rows from the right table that may or may not have corresponding rows in the left table.
The RIGHT JOIN is also known as RIGHT OUTER JOIN.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def right_join():
    # The following example uses the RIGHT JOIN clause to retrieve all rows from the film 
    # table that may or may not have corresponding rows in the inventory table:
    sql = """SELECT film.film_id, film.title, inventory.inventory_id FROM inventory 
            RIGHT JOIN film ON film.film_id = inventory.film_id ORDER BY film.title;"""

    # Since the film and inventory table has the film_id column, you can use the USING syntax:
    sql = """SELECT f.film_id, f.title, i.inventory_id FROM inventory i
            RIGHT JOIN film f USING(film_id) ORDER BY f.title;"""
    cur.execute(sql)
    records = cur.fetchall()
    desc = cur.description
    for record in records:
        print(record)
    print(desc)

# right_join()

def right_join_where():
    # The following query uses a RIGHT JOIN clause with a WHERE clause to retrieve the films that have no inventory:
    sql = """SELECT f.film_id, f.title, i.inventory_id FROM inventory i
            RIGHT JOIN film f USING(film_id) WHERE i.inventory_id IS NULL ORDER BY f.title;"""
    cur.execute(sql)
    records = cur.fetchall()
    desc = cur.description
    for record in records:
        print(record)
    print(desc)

# right_join_where()