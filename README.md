# Newsletter DB Query

This Python3 script queries a PostgreSQL `news` database with 3 different tables: `articles`, `authors`, and `log`.

It prints:
 * The 3 most popular articles of all time
 * The most popular authors, sorted by hits
 * Days with more than 1% request error rate

## How to Run

This program requires an active server operating PostgreSQL that can run Python3 locally. One relatively easy way to accomplish this locally, without provisioning remote servers through Heroku, Amazon Lightsail, or other services is to use [Vagrant](https://www.vagrantup.com/), a Linux VM.

Please refer to their documentation on getting set up, then add the `newsdata.sql` file to the `vagrant` shared folder.

To execute the program, input:

```bash
 $ python3 newsquery.py
```

### Dependencies

Running this program requires:

 * postgresql
 * Python3
 * psycopg

I ran into some challenges getting psycopg to work with Python3. If you're using Python3, you may need to run the following from the `/vagrant` directory:
```
pip3 install psycopg2-binary --user
```
