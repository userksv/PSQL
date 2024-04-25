import psycopg2

conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def all_tables():
    query = ''' SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' '''
    cur.execute(query)
    tables = cur.fetchall()
    for table in tables:
        print(table)

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
