"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-where/
To retrieve rows that satisfy a specified condition, you use a WHERE clause.
Use a WHERE clause in the SELECT statement to filter rows of a query based on one or more conditions.
"""

import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def where_equal():
    query = """SELECT last_name, first_name FROM customer WHERE first_name = 'Jamie'"""
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)

# where_equal()

def where_and():
    # WHERE and logical AND
    query = """SELECT last_name, first_name FROM customer WHERE first_name = 'Jamie' AND last_name = 'Rice'"""
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)

# where_and()

def where_or():
    """The following example uses a WHERE clause with an OR operator to find the customers
    whose last name is Rodriguez or first name is Adam"""

    query = """SELECT first_name, last_name FROM customer WHERE last_name = 'Rodriguez' OR first_name = 'Adam'"""
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)

# where_or()

def where_in():
    """The following example uses the WHERE clause with the IN operator to find the customers 
    with first names in the list Ann, Anne, and Annie"""
    
    query = """SELECT first_name, last_name FROM customer WHERE first_name IN ('Ann', 'Anne', 'Annie')"""
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)
        
# where_in()

def where_like():
    """To find a string that matches a specified pattern, you use the LIKE operator.
    The following example uses the LIKE operator in the WHERE clause to find customers whose first names start with the word Ann
    The % is called a wildcard that matches any string."""
    
    query = """SELECT first_name, last_name FROM customer WHERE first_name LIKE 'Ann%'"""
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)

# where_like()

def where_between():
    """The following example finds customers whose first names start with the letter A and contains 3 to 5 characters
    by using the BETWEEN operator. The BETWEEN operator returns true if a value is in a range of values."""

    query = """SELECT first_name, LENGTH(first_name) name_length FROM customer WHERE first_name 
    LIKE 'A%' AND LENGTH(first_name) BETWEEN 3 AND 5 ORDER BY name_length"""
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)

# where_between()

def where_not_equal():
    """This example finds customers whose first names start with Bra and last names are not Motley
    Note that you can use the != operator and <> operator interchangeably because they are equivalent."""
    
    query = """SELECT first_name, last_name FROM customer WHERE first_name LIKE 'Bra%' AND last_name <> 'Motley';"""
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)
    
# where_not_equal()