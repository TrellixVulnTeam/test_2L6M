# -*- coding: utf-8 -*-
import psycopg2

def connect():
    con = psycopg2.connect("host=" + "localhost" + " port=" + "5432" + " dbname=" + "postgres" + " user=" + "postgres" + " password=" + "postgres")

    return con
if __name__ == '__main__':
    con = connect()
