"""
The SELECT DISTINCT removes duplicate rows from a result set.
The SELECT DISTINCT clause retains one row for each group of duplicates.
The SELECT DISTINCT clause can be applied to one or more columns in the select list of the SELECT statement.
PostgreSQL treats NULLs as duplicates so that it keeps one NULL for all NULLs when you apply the SELECT DISTINCT clause.

Summary
Use the SELECT DISTINCT to remove duplicate rows from a result set of a query.
"""
import psycopg2

conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def select_distinct():
    """
    In practice, you often use the SELECT DISTINCT clause to analyze the uniqueness of values in a column.
    For example, you may want to know how many rental rates for films from the film table:
    """
    query = """SELECT DISTINCT rental_rate FROM film ORDER BY rental_rate"""
    cur.execute(query)
    rates = cur.fetchmany(10)
    for rate in rates:
        print(rate)

select_distinct()