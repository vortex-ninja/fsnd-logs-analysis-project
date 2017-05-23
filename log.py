from logdb import QUERIES, query_database


def most_popular_articles():

    results = query_database(QUERIES[0])
    print('\nWhat are the most popular three articles of all time?\n')
    for title, views in results:
        print(' * "{}" -- {} views'.format(title, views))


most_popular_articles()
