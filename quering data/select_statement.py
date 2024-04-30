'''
Use the SELECT ... FROM statement to retrieve data from a table.
1. PostgreSQL evaluates the FROM clause before the SELECT clause.
2. Use a column alias to assign a temporary name to a column or an expression in a query.
3. In PostgreSQL, the FROM clause is optional. '''

import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def select_all():
    query = 'SELECT * FROM customer'
    cur.execute(query)
    customers = cur.fetchall()
    for customer in customers:
        print(customer)

def select_concat_values():
    query = '''SELECT first_name || ' ' || last_name, email FROM customer LIMIT 10'''
    # Selects from customer and concatenate f_name and l_name
    cur.execute(query)
    customers = cur.fetchall()
    for customer in customers:
        print(customer)

def select_cur_time():
    cur.execute('SELECT NOW()')
    print(cur.fetchall())