CREATE VIEW articles_views AS
    SELECT articles.id, title, count(articles.id) AS views
    FROM articles, log
    WHERE path = ('/article/' || slug)
    AND status = '200 OK'
    GROUP BY articles.id;

CREATE VIEW error_requests AS
    SELECT date(time) AS date, count(*) AS errors
    FROM log
    WHERE status != '200 OK'
    GROUP BY date;

CREATE VIEW all_requests AS
    SELECT date(time) AS date, count(*) AS requests
    FROM log
    GROUP BY date;