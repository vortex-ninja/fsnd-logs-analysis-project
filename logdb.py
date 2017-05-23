import psycopg2


def most_popular_articles():
    """Returns three most popular articles of all time"""

    conn = psycopg2.connect('dbname=news')
    cur = conn.cursor()
    cur.execute("""select title, count(articles.id) as num
                 from log, articles
                 where path = ('/article/' || articles.slug)
                 and status ='200 OK'
                 group by articles.id
                 order by num desc
                 limit 3;""")

    results = cur.fetchall()

    return results
