"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-natural-join/
In practice, you should avoid using the NATURAL JOIN whenever possible because sometimes it may cause an unexpected result.
Use the PostgreSQL NATURAL JOIN clause to query data from two or more tables that have common columns.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()
