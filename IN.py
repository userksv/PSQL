"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-in/
The IN operator allows you to check whether a value matches any value in a list of values.
Use the IN operator to check if a value matches any value in a list of values.
Use the NOT operator to negate the IN operator.
"""

import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def select_where_IN():
    # The following example uses the IN operator to retrieve information about the film with id 1, 2, and 3:
    query = """SELECT film_id, title FROM film WHERE film_id in (1, 2, 3)"""
    cur.execute(query)
    films = cur.fetchall()
    for film in films:
        print(film)

# select_where_IN()

def select_where_IN_table():
    # The following example uses the IN operator to find the actors who have the last name in the list 'Allen', 'Chase', and 'Davis':
    query = """SELECT first_name, last_name FROM actor WHERE last_name IN ('Allen', 'Chase', 'Davis') ORDER BY last_name"""
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)

# select_where_IN_table()

def select_where_IN_dates():
    """The following statement uses the IN operator to find payments whose payment dates are
    in a list of dates: 2007-02-15 and 2007-02-16:
    In this example, the payment_date column has the type timestamp that consists of both date and time parts.
    To match the values in the payment_date column with a list of dates, you need to cast them to date values 
    that have the date part only.
    To do that you use the :: cast operator.
    CAST: Convert a value of One Type to Another -- payment_date::date
    """
    query = """SELECT payment_id, amount, payment_date FROM payment WHERE payment_date::date IN ('2007-02-15', '2007-02-16')"""
    cur.execute(query)
    payments = cur.fetchall()
    for payment in payments:
        print(payment)

# select_where_IN_dates()

def select_where_NOT_IN():
    # The following example uses the NOT IN operator to retrieve films whose id is not 1, 2, or 3:
    query = """SELECT film_id, title FROM film WHERE film_id NOT IN (1, 2, 3) ORDER BY film_id"""
    cur.execute(query)
    films = cur.fetchmany(10)
    for film in films:
        print(film)

# select_where_NOT_IN()