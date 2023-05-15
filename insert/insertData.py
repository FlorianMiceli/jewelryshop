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
    f = pd.read_excel(f'{XLSXfilename}.xlsx')
    cur = conn.cursor()
    for row in f.iterrows():
        attributes = ','.join(tuple(f.columns[1:]))
        values = tuple(row[1][1:])
        # values starting with 'to_timestamp' needs to be without quotes
        values = str(values).replace('"to_timestamp', 'to_timestamp').replace(')"', ")")
        request = f'INSERT INTO {f.columns[0]} ({attributes}) VALUES {values}'.replace(' nan,', ' NULL,')
        print(request)
        cur.execute(request)
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
    os.chdir('jewelryshop/insert/dataToInsert')

    # 2022
    to_insert = ['chaines2022', 'perles2022', 'colliers2022','pendentifs']
    insertIntoDBfromMultipleXLSX(to_insert, conn)

    # inflation 
    cur = conn.cursor()
    cur.execute("UPDATE COLLIERS SET prixCollier = prixCollier*1.12 WHERE typeProduit = 'collier';")
    cur.execute("UPDATE PERLES SET prixPerle = prixPerle*1.12 WHERE typeProduit = 'perle';")
    cur.execute("UPDATE CHAINES SET prixChaine = prixChaine*1.12 WHERE typeProduit = 'chaine';")

    # 2023
    to_insert = ['chaines2023', 'colliers2023', 'perles2023', 'pendentifs2']
    insertIntoDBfromMultipleXLSX(to_insert, conn)

    # promotions 
    to_insert = 'promotions'
    insertIntoDBfromXLSX(to_insert, conn)

    conn.commit()
    conn.close()