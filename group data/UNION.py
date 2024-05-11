"""
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-union/

The UNION operator allows you to combine the result sets of two or more SELECT statements into a single result set.
    Use the UNION to combine result sets of two queries and return distinct rows.
    Use the UNION ALL to combine the result sets of two queries but retain the duplicate rows.
"""
import psycopg2
conn = psycopg2.connect('dbname=dvdrental user=postgres')
cur = conn.cursor()


def union():
    # The following statement uses the UNION operator to combine data from the queries that retrieve 
    # data from the top_rated_films and most_popular_films:
    sql = """SELECT * FROM top_rated_films UNION SELECT * FROM most_popular_films;"""
    cur.execute(sql)
    films = cur.fetchall()
    for film in films:
        print(film)

# union()

def union_all():
    # The following statement uses the UNION ALL operator to combine result sets from queries that retrieve
    # data from top_rated_films and most_popular_films tables:
    sql = """SELECT * FROM top_rated_films UNION ALL SELECT * FROM most_popular_films;"""
    cur.execute(sql)
    films = cur.fetchall()
    for film in films:
        print(film)

# union_all()

def union_all_order_by():
    sql = """SELECT * FROM top_rated_films UNION ALL SELECT * FROM most_popular_films ORDER BY title;"""
    cur.execute(sql)
    films = cur.fetchall()
    for film in films:
        print(film)

union_all_order_by()