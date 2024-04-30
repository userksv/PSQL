"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-group-by/
The GROUP BY clause divides the rows returned from the SELECT statement into groups.
For each group, you can apply an aggregate function such as SUM() to calculate the sum of items 
    or COUNT() to get the number of items in the groups.
Use the PostgreSQL GROUP BY clause to divide rows into groups and apply an aggregate function to each group.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def group_by():
    # Using PostgreSQL GROUP BY without an aggregate function example
    # The following example uses the GROUP BY clause to retrieve the customer_id from the payment table:
    sql = """SELECT customer_id FROM payment GROUP BY customer_id ORDER BY customer_id LIMIT 10;"""
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
        print(record)
    # Each customer has one or more payments. The GROUP BY clause removes duplicate values in the 
    # customer_id column and returns distinct customer ids. 
    # In this example, the GROUP BY clause works like the DISTINCT operator.
# group_by()

def group_by_sum():
    # The GROUP BY clause is useful when used in conjunction with an aggregate function.
    # The following query uses the GROUP BY clause to retrieve the total payment paid by each customer:
    sql = """SELECT customer_id, SUM (amount) FROM payment GROUP BY customer_id ORDER BY customer_id LIMIT 10;"""
    cur.execute(sql)    
    records = cur.fetchall()
    desc = cur.description
    for record in records:
        print(record)
    print(desc)

# group_by_sum()

def group_by_join():
    # The following statement uses the GROUP BY clause to retrieve the total payment for each 
    # customer and display the customer name and amount:
    sql = """SELECT first_name || ' ' || last_name AS full_name, SUM (amount) amount 
            FROM payment
            INNER JOIN customer USING (customer_id)
            GROUP BY full_name 
            ORDER BY amount DESC;"""
    cur.execute(sql)    
    records = cur.fetchall()
    desc = cur.description
    for record in records:
        print(record)
    print(desc)

# group_by_join()

def group_by_count():
    # The following example uses the GROUP BY clause with the COUNT() 
    # function to count the number of payments processed by each staff:
    sql = """SELECT staff_id, COUNT (payment_id) FROM payment GROUP BY staff_id LIMIT 10;"""
    cur.execute(sql)    
    records = cur.fetchall()
    desc = cur.description
    for record in records:
        print(record)
    print(desc)

# group_by_count()

def group_by_multiple_columns():
    # The following example uses a GROUP BY clause to group rows by values in two columns:
    sql = """SELECT customer_id, staff_id, SUM(amount) FROM payment GROUP BY staff_id, customer_id ORDER BY customer_id
    LIMIT 10;"""
    cur.execute(sql)    
    records = cur.fetchall()
    desc = cur.description
    for record in records:
        print(record)
    print(desc)

# group_by_multiple_columns()

def group_by_date_column():
    # The following example uses the GROUP BY clause to group the payments by payment date:
    sql = """SELECT payment_date::date payment_date, SUM(amount) sum FROM payment 
            GROUP BY payment_date::date ORDER BY payment_date DESC LIMIT 10;"""
    cur.execute(sql)    
    records = cur.fetchall()
    desc = cur.description
    for record in records:
        print(record)
    print(desc)
    # Since the values in the payment_date column are timestamps, we cast them to date values using the cast operator ::
# group_by_date_column()