import psycopg2

conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def all_tables():
    query = ''' SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' '''
    cur.execute(query)
    tables = cur.fetchall()
    for table in tables:
        print(table)
