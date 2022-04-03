import os
import psycopg2

def get_connection():
    return psycopg2.connect("postgresql://postgres:test@127.0.0.1:5432/testdb")

with get_connection() as conn:
    with conn.cursor() as cur:
        json = {
            "title": "test title"
        }

        cur.execute("INSERT INTO t_test (col1) VALUES (%)", (psycopg2.Binary(b"hogehoge"),))
    conn.commit()
