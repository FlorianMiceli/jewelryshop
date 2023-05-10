import psycopg2
import psycopg2.extras
from sshtunnel import SSHTunnelForwarder
import os
from dotenv import load_dotenv
load_dotenv()

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

def openConn():
    tunnel = SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=(pg_host, pg_port)
    )
    tunnel.start()
    conn = psycopg2.connect(
            host='localhost', 
            port=tunnel.local_bind_port,
            dbname=pg_database,
            user=pg_user,
            password=pg_password,
            sslmode='disable', 
        )
    return conn, tunnel

def closeConn(conn, tunnel):
    conn.close()
    tunnel.stop()

def request(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    return results
