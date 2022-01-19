import os
import psycopg2

def get_connection():
    #dsn = os.environ.get('DATABASE_URL')
    return psycopg2.connect("host=localhost port=5432 user=postgres password=test dbname=postgres")

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute('INSERT INTO public."members" (name, age) VALUES (%s, %s)', ('foo','10'))
    conn.commit()
