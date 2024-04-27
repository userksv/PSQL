"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-like/
PostgreSQL offers two wildcards:
Percent sign ( %) matches any sequence of zero or more characters.
Underscore sign (_)  matches any single character.
ILIKE - case-insensitive matching
    Use the LIKE operator to match data by patterns.
    Use the NOT LIKE operator to negate the LIKE operator.
    Use the % wildcard to match zero or more characters.
    Use the _ wildcard to match a single character.
    Use the ESCAPE option to specify the escape character.
    Use the ILIKE operator to match data case-insensitively.
"""

import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def like():
    # The following example uses the LIKE operator to find customers whose first names contain the string er :
    query = """SELECT first_name FROM customer WHERE first_name LIKE '%er%' ORDER BY first_name"""
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)

# like()

def like_both_wildcards():
    # The following example uses the LIKE operator with a pattern that contains both the percent ( %) and underscore (_) wildcards:
    query = """SELECT first_name, last_name FROM customer WHERE first_name LIKE '_her%' ORDER BY first_name"""
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)

# like_both_wildcards()