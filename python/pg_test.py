import os
import psycopg2

def get_connection():
    #dsn = os.environ.get('DATABASE_URL')
    #return psycopg2.connect("host=127.0.0.1 port=5432 user=user1 password=pass dbname=mydb")
    return psycopg2.connect("postgresql://postgres:test@127.0.0.1:5432/testdb")

a = [b"aaaaaa", b"bbbbbbbb"]

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute('INSERT INTO t_test (col1) VALUES (%s)', (bytes(a)),)
        #cur.execute('SELECT * from t_test')
        #for row in cur:
        #    print(row)
    conn.commit()
