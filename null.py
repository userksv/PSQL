"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-is-null/

In databases, NULL means missing information or not applicable.
Use the IS NULL operator to check whether a value is NULL or not.
"""

import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def null():
    # The following example uses the IS NULL operator to find the addresses from the address 
    # table that the address2 column contains NULL:
    query = """SELECT address, address2 FROM address WHERE address2 IS NULL"""
    cur.execute(query)
    addresses = cur.fetchall()
    for addr in addresses:
        print(addr)

# null()

def not_null():
    # The following example uses the IS NOT NULL operator to retrieve the address that has the address2 not null:
    query = """SELECT address, address2 FROM address WHERE address2 IS NOT NULL"""
    cur.execute(query)
    addresses = cur.fetchall()
    for addr in addresses:
        print(addr)

not_null()
# Notice that the address2 is empty, not NULL. This is a good example of a bad practice when it comes
# to storing empty strings and NULL in the same column.