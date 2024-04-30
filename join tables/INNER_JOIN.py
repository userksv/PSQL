"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-inner-join/
Use INNER JOIN clauses to select data from two or more related tables and return rows that have matching values in all tables.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def inner_join():
    # The following statement uses the INNER JOIN clause to select data from both tables:
    sql = """SELECT 
                customer.customer_id, 
                customer.first_name, 
                customer.last_name, 
                payment.amount, 
                payment.payment_date 
            FROM customer 
            INNER JOIN payment ON payment.customer_id = customer.customer_id 
            ORDER BY payment.payment_date"""
    
    # Since both tables have the same customer_id column, you can use the USING syntax:
    sql = """SELECT 
                customer_id, 
                first_name, 
                last_name, 
                amount, 
                payment_date 
            FROM customer 
            INNER JOIN payment USING(customer_id) ORDER BY payment_date"""
    cur.execute(sql)
    records = cur.fetchmany(10)
    desc = cur.description
    print(desc)
    for record in records:
        print(record)

# inner_join()

def inner_join_three_tables():
    # Each staff member can handle zero or multiple payments, with each payment being processed by one and only one staff member.
    # Similarly, each customer can make zero or multiple payments, and each payment is associated with a single customer.
    # The following example uses INNER JOIN clauses to retrieve data from three tables
    sql = """SELECT 
                c.customer_id, 
                c.first_name || ' ' || c.last_name customer_name, 
                s.first_name || ' ' || s.last_name staff_name, 
                p.amount, 
                p.payment_date 
            FROM customer c 
            INNER JOIN payment p USING (customer_id) 
            INNER JOIN staff s using(staff_id) 
            ORDER BY payment_date"""
    cur.execute(sql)
    records = cur.fetchmany(10)
    desc = cur.description
    print(desc)
    for record in records:
        print(record)

inner_join_three_tables()
    