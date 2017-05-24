import psycopg2


QUERY1 = "SELECT title, views FROM articles_views ORDER BY views DESC LIMIT 3;"

QUERY2 = """SELECT name, sum(views) AS sum
            FROM authors, articles_views, articles
            WHERE articles.author=authors.id
            AND articles.id=articles_views.id
            GROUP BY authors.id
            ORDER BY sum DESC;"""

QUERY3 = """SELECT error_requests.date, (errors::float/requests::float)
            FROM error_requests, all_requests
            WHERE error_requests.date=all_requests.date
            AND (errors::float/requests::float)>=0.01;"""

QUERIES = [QUERY1, QUERY2, QUERY3]


def query_database(q):
    """Returns results for a given database query"""

    conn = psycopg2.connect('dbname=news')
    cur = conn.cursor()
    cur.execute(q)
    results = cur.fetchall()
    conn.close()

    return results
