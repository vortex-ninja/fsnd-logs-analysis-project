import psycopg2

# Queries use this defined views
#
# 1. articles_views
# Counts how many times an article was viewed. Checks if the path given was
# correct and whether the server responded with 200 OK status code.
#
# SELECT articles.id, title, count(articles.id) AS views
# FROM articles, log
# WHERE path = ('/article/' || slug)
# AND status = '200 OK'
# GROUP BY articles.id;
#
# 2. error_requests
# Counts how many error (not '200 OK') requests happened every day.
#
# SELECT date(time) AS date, count(*) AS errors
# FROM log
# WHERE status != '200 OK'
# GROUP BY date;
#
# 3. all_requests
# Counts how many requests in total happened every day.
#
# SELECT date(time) AS date, count(*) AS requests
# FROM log
# GROUP BY date;


QUERY1 = "SELECT title, views FROM articles_views ORDER BY views DESC LIMIT 3;"

QUERY2 = """SELECT name, sum(views) AS sum
            FROM authors, articles_views, articles
            WHERE articles.author=authors.id
            AND articles.id=articles_views.id
            GROUP BY authors.id
            ORDER BY sum DESC;"""

# Is it possible not to repeat the expression '(errors::float/requests::float)'
# twice in this query? I tried to give it an alias with 'AS' but it didn't work.

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
