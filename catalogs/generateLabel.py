import psycopg2
import psycopg2.extras
from sshtunnel import SSHTunnelForwarder
import os
from dotenv import load_dotenv
load_dotenv()
from jinja2 import Template
from xhtml2pdf import pisa
import json 
import barcode
from barcode.writer import ImageWriter

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
title = 'Etiquette collier'
nomProduit = 'jonque'

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

# get composition, prix, idProduit, chaine
composition = ''
for i in range (len(results)):
    if results[i][0] == nomProduit:
        produit_index = i
        composition += results[i][2] + ', '
        i += 1
        while results[i][0] == '' :
            if results[i+1][0] != '' :
                composition += results[i][2]
            else :
                composition += results[i][2] + ', '
            i += 1
        break
prix = results[produit_index][3]
idProduit = results[produit_index][4]
chaine = results[produit_index][1] if results[produit_index][1] != '' else 'aucune'

# generate barcode
options = {
    'module_width': 0.8,
    'module_height': 60.0,
    'quiet_zone': 0,
    'font_size': 0,
}
code128 = barcode.Code128(idProduit, writer=ImageWriter())
code128.writer.dpi = 300
filename = code128.save("barcode", options=options)

# generate PDF
with open('templateLabel.html', 'r') as f:
    template_string = f.read()
    template = Template(template_string)
    result = template.render(prix=prix, idProduit=idProduit, composition=composition, chaine=chaine)
    with open(f'catalogsPDF/{title}.pdf', 'wb') as f:
        pisa.CreatePDF(result, dest=f)
    print('PDF generated')