#!/usr/bin/env python3
import psycopg2


def main():

    def pop_art():
        cur.execute("""
        select articles.title, count(log.id) as hits
            from log join articles
            on articles.slug = SUBSTRING(log.path, 10)
            group by title
            order by hits desc
            limit 3;
            """)
        res = cur.fetchall()
        print("\n1. What are the three most popular articles of all time?")
        for r in res:
            print("'{}' with {} hits".format(*r))
        return res

    def pop_author():
        cur.execute("""
        select
            authors.name,
            count(log.id) as hits
        from
            articles
        inner join log on articles.slug = SUBSTRING(log.path, 10)
        inner join authors on authors.id = articles.author
        group by authors.name
        order by hits desc;
        """)
        res = cur.fetchall()
        print('\n2. Who are the most popular authors of all time?')
        for r in res:
            print('{} - {} views'.format(*r))
        return res

    def err_rate():
        cur.execute("""
        select day,
            err,
            ttl,
            to_char(err::float/ttl::float * 100, 'FM999999999.00') as rate
        from
            (select time::date as day,
            sum(case when status != '200 OK' then 1 else 0 end) as err,
            sum(case when status != '200 ok' then 1 else 1 end) as ttl
            from log
            group by day) hits
        where (err::float/ttl::float * 100) > 1
        group by day,err,ttl
        order by rate desc;
        """)
        res = cur.fetchall()
        print("\n3. Days with HTTP error rates over 1% are:")
        print((res[0][0]).strftime("%Y-%B-%d") + " had error rate: " + str(res[0][3]))
        return res

    try:
        conn = psycopg2.connect("dbname=news")
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
    else:
        pop_art()
        pop_author()
        err_rate()
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    main()
