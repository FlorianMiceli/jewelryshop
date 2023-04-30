import psycopg2
import psycopg2.extras
from sshtunnel import SSHTunnelForwarder
import os
from dotenv import load_dotenv
load_dotenv()
from jinja2 import Template
from xhtml2pdf import pisa
import json 

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

# catalog to generate/update
title = 'Catalogue détaillé'

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

    # get request in json file
    os.chdir('jewelryshop/catalogs')
    with open('catalogsRequests.json', 'r', encoding='utf-8') as f:
        catalogs = json.load(f)
        request = catalogs[title]

    # get headers
    cur = conn.cursor()
    get_headers_request = f'SELECT * FROM ({request[:-1]}) AS subquery LIMIT 1;'
    cur.execute(get_headers_request)
    results = cur.fetchall()
    headers = [col.name for col in [header for header in cur.description]]
    
    # execute and get results
    cur.execute(request)
    results = cur.fetchall()
    cur.close()
    conn.close()

# generate PDF
with open('template.html', 'r') as f:
    template_string = f.read()
    template = Template(template_string)
    result = template.render(data=results, title=title, headers=headers)
    with open(f'catalogsPDF/{title}.pdf', 'wb') as f:
        pisa.CreatePDF(result, dest=f)
    print('PDF generated')