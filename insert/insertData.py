import psycopg2
import psycopg2.extras
from sshtunnel import SSHTunnelForwarder
import os
from dotenv import load_dotenv
load_dotenv()
from jinja2 import Template
from xhtml2pdf import pisa
import pandas as pd

# creds
ssh_host = 'ssh2.pgip.universite-paris-saclay.fr'
ssh_port = 22
ssh_username = os.getenv('SSH_USERNAME')
ssh_password = os.getenv('SSH_PASSWORD')

pg_host = 'tp-postgres'
pg_port = 5432
pg_database = os.getenv('PG_USERNAME')
pg_user = os.getenv('PG_USERNAME')
pg_password = os.getenv('PG_USERNAME')

def insertIntoDBfromXLSX(XLSXfilename, conn):
    os.chdir('jewelryshop/insert/dataToInsert')
    f = pd.read_excel(f'{XLSXfilename}.xlsx')
    cur = conn.cursor()
    for row in f.iterrows():
        attributes = ','.join(tuple(f.columns[1:]))
        request = f'INSERT INTO {f.columns[0]} ({attributes}) VALUES {tuple(row[1][1:])}'
        print(request)
        cur.execute(request)
    conn.commit()
    cur.close()

def insertIntoDBfromMultipleXLSX(filesList, conn):
    for filename in filesList:
        insertIntoDBfromXLSX(filename, conn)

# connexion SSH
with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=(pg_host, pg_port)
) as tunnel:
    # connexion PostgreSQL
    print('tunnel open')
    conn = psycopg2.connect(
        host='localhost',
        port=tunnel.local_bind_port,
        dbname=pg_database,
        user=pg_user,
        password=pg_password,
        sslmode='disable',
    )
    print('connection open')

    insertIntoDBfromXLSX('chaines2022', conn)

    conn.close()
