from logdb import QUERIES, query_database


def most_popular_articles():
    """Lists three most popular articles"""

    results = query_database(QUERIES[0])
    print('\nWhat are the most popular three articles of all time?\n')
    for title, views in results:
        print(' * "{}" -- {} views'.format(title, views))


def most_popular_authors():
    """Lists most popular authors"""

    results = query_database(QUERIES[1])
    print('\nWho are the most popular article authors of all time?\n')
    for author, views in results:
        print(' * {} -- {} views'.format(author, views))


def error_dates():
    """Lists days on which error requests make up more than 1% all requests"""

    results = query_database(QUERIES[2])
    print('\nOn which days did more than 1% of requests lead to errors?\n')
    for date, rate in results:
        print(' * {} -- {:.2%}'.format(date, rate))


most_popular_articles()
most_popular_authors()
error_dates()
