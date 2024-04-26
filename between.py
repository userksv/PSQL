"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-between/
The BETWEEN operator allows you to check if a value falls within a range of values.
    (value BETWEEN low AND high)
    (value >= low AND value <= high)
If you want to check if a value is outside a specific range, you can use the NOT BETWEEN operator as follows:
    (value NOT BETWEEN low AND high)
    (value < low OR value > high)

Use the BETWEEN operator to check if a value falls within a particular range.
Use the NOT BETWEEN operator to negate the BETWEEN operator.
"""

import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()

def between_payment_ids():
    # The following query uses the BETWEEN operator to retrieve payments with payment_id is between 17503 and 17505
    query = """SELECT payment_id, amount FROM payment WHERE payment_id BETWEEN 17503 AND 17505 ORDER BY payment_id"""
    cur.execute(query)
    payments = cur.fetchall()
    for payment in payments:
        print(payment)

# between_payment_ids()

def NOT_between_payments_ids():
    # The following example uses the NOT BETWEEN operator to find payments with the payment_id not between 17503 and 17505
    query = """SELECT payment_id, amount FROM payment WHERE payment_id NOT BETWEEN 17503 AND 17505 ORDER BY payment_id"""
    cur.execute(query)
    payments = cur.fetchmany(10)
    for payment in payments:
        print(payment)

# NOT_between_payments_ids()

def between_dates():
    """
    If you want to check a value against a date range, you use the literal date in ISO 8601 format, which is YYYY-MM-DD.
    The following example uses the BETWEEN operator to find payments whose payment dates are between 
    2007-02-15 and 2007-02-20 and amount more than 10:
    """
    query = """SELECT payment_id, amount, payment_date FROM payment WHERE payment_date BETWEEN '2007-02-15' AND '2007-02-20' 
                AND amount > 10 ORDER BY payment_date"""
    cur.execute(query)
    payments = cur.fetchmany(10)
    for payment in payments:
        print(payment)

# between_dates()

