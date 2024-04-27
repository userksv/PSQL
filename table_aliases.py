"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-alias/
A table alias is a feature in SQL that allows you to assign a temporary name to a table during the execution of a query.
Use PostgreSQL table aliases to assign a temporary name to a table during the execution of a query. 
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def alias():
    # The following example uses a table alias to retrieve five titles from the film table:
    sql = """SELECT f.title FROM film AS f ORDER BY f.title LIMIT 5"""
    cur.execute(sql)
    films = cur.fetchall()
    alias = cur.description
    print(alias[0][0])
    for film in films:
        print(film)

# alias()

"""
Typically, you use table aliases in a query that has a join clause to retrieve data from multiple 
related tables that share the same column name.
If you use the same column name that comes from multiple tables in the same query without fully 
qualifying them, you will get an error.
To avoid this error, you can qualify the columns using the following syntax:
    (table_name.column_name)
"""
def alias_with_join():
    # the following query uses an INNER JOIN clause to retrieve data from the customer and payment tables
    sql = """SELECT c.customer_id, c.first_name, p.amount, p.payment_date FROM customer c 
            INNER JOIN payment p ON p.customer_id = c.customer_id ORDER BY p.payment_date DESC"""
    cur.execute(sql)
    records = cur.fetchmany(10)
    aliases = cur.description
    print(aliases)
    for record in records:
        print(record)

# alias_with_join()

def alias_self_join():    
    # When you join a table to itself (a.k.a self-join), you need to use table aliases. 
    # This is because referencing the same table multiple times within a query will result in an error.
    # The following example shows how to reference the film table twice in the same query using the table aliases
    sql = """SELECT f1.title, f2.title, f1.length FROM film f1 
            INNER JOIN film f2  ON f1.film_id <> f2.film_id AND f1.length = f2.length"""
    cur.execute(sql)
    aliases = cur.description
    print(aliases)
    films = cur.fetchmany(10)
    for film in films:
        print(film)

alias_self_join()