import psycopg2

QUERY1 = """select title, count(articles.id) as num
                 from log, articles
                 where path = ('/article/' || articles.slug)
                 and status ='200 OK'
                 group by articles.id
                 order by num desc
                 limit 3;"""


def query_database(q):
    """Returns results for a given database query"""

    conn = psycopg2.connect('dbname=news')
    cur = conn.cursor()
    cur.execute(q)
    results = cur.fetchall()
    conn.close()

    return results


# code for testing

print(query_database(QUERY1))
