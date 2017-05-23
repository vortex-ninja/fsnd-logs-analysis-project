import psycopg2

QUERY1 = """select title, count(articles.id) as num
                 from log, articles
                 where path = ('/article/' || articles.slug)
                 and status ='200 OK'
                 group by articles.id
                 order by num desc
                 limit 3;"""

QUERY2 = "select name, s from authors, authors_pop where author=id;"

QUERY3 = """select requests_not_ok_404.date, (not_ok::float/all_requests::float)
          from requests_not_ok_404, requests_all
          where requests_not_ok_404.date=requests_all.date
          and (not_ok::float/all_requests::float)>=0.01;"""

QUERIES = [QUERY1, QUERY2, QUERY3]


def query_database(q):
    """Returns results for a given database query"""

    conn = psycopg2.connect('dbname=news')
    cur = conn.cursor()
    cur.execute(q)
    results = cur.fetchall()
    conn.close()

    return results
