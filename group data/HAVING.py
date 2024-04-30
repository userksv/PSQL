"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-having/
The HAVING clause specifies a search condition for a group. 
The HAVING clause is often used with the GROUP BY clause to filter groups based on a specified condition.
Use the HAVING clause to specify the filter condition for groups returned by the GROUP BY clause.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def having_sum():
    # The following query uses the GROUP BY clause with the SUM() function to find the total payment of each customer
    sql = """SELECT customer_id, SUM (amount) amount FROM payment GROUP BY customer_id ORDER BY amount DESC LIMIT 10;"""
    
    # The following statement adds the HAVING clause to select the only customers who have been spending more than 200:
    sql = """SELECT customer_id, SUM (amount) amount FROM payment GROUP BY customer_id 
            HAVING SUM (amount) > 200 ORDER BY amount DESC LIMIT 10;"""
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
        print(record)
        
# having_sum()

def having_count():
    # The following query uses the GROUP BY clause to find the number of customers per store:
    sql = """SELECT store_id, COUNT (customer_id) FROM customer GROUP BY store_id"""

    # The following statement adds the HAVING clause to select a store that has more than 300 customers:
    sql = """SELECT store_id, COUNT (customer_id) FROM customer 
            GROUP BY store_id HAVING COUNT(customer_id) > 300;"""
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
        print(record)
        
having_count()