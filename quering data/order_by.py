"""
The ORDER BY clause allows you to sort rows returned by a SELECT clause
in ascending or descending order based on a sort expression.
"""
import psycopg2

conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def order_by_first_name():
    query = """SELECT first_name, last_name FROM customer ORDER BY first_name LIMIT 10"""
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)

# order_by_first_name()

def order_by_multiple_columns():
    """
    The following statement selects the first name and last name from the customer 
    table and sorts the rows by the first name in ascending order and last name in descending order:
    """
    query = """
        SELECT first_name, last_name FROM customer 
        ORDER BY
            first_name ASC,
            last_name DESC
            LIMIT 10
    """
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)

# order_by_multiple_columns()

def order_by_expression():
    """
    The following statement selects the first names and their lengths. 
    It sorts the rows by the lengths of the first names
    """
    query = """
        SELECT first_name, LENGTH(first_name) len
        FROM customer 
        ORDER BY
            len DESC
            LIMIT 10
    """
    cur.execute(query)
    names = cur.fetchall()
    for name in names:
        print(name)

# order_by_expression()

def order_by_clause():
    """Use NULLS FIRST and NULLS LAST options to explicitly specify the order of NULL with other non-null values."""
    # ORDER BY sort_expresssion [ASC | DESC] [NULLS FIRST | NULLS LAST]
    """
        CREATE TABLE sort_demo(num INT);
        INSERT INTO sort_demo(num) 
        VALUES 
            (1), 
            (2), 
            (3), 
            (null);
        --/////--
        SELECT num FROM sort_demo ORDER BY num NULLS LAST;
    """
    pass