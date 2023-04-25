import psycopg2
import psycopg2.extras
from sshtunnel import SSHTunnelForwarder
import os
from dotenv import load_dotenv
load_dotenv()
from jinja2 import Template
from xhtml2pdf import pisa

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
    
    cur = conn.cursor()
    cur.execute('''
        SELECT 
            CASE WHEN c.NomCollier = lag(c.NomCollier) OVER (ORDER BY c.idcollier) THEN '' ELSE c.NomCollier END AS NomCollier, 
            CASE WHEN ch.NomChaine = lag(ch.NomChaine) OVER (ORDER BY c.idcollier) THEN '' ELSE ch.NomChaine END AS NomChaine, 
            nb_Perle, 
            NomPerle, 
            CASE WHEN c.PrixCollier = lag(c.PrixCollier) OVER (ORDER BY c.idcollier) THEN NULL ELSE c.PrixCollier END AS PrixCollier
        FROM 
            colliers AS c 
            JOIN pendentifs AS p ON p.idCollier = c.idCollier AND p.Nomproduit = c.type_de_produit 
            JOIN Perles AS po ON p.idPerle = po.idPerle AND p.type_de_produit = po.type_de_produit 
            JOIN Chaines AS ch ON c.idChaine = ch.idChaine AND ch.type_de_produit = c.NomProduit 
        ORDER BY 
            c.idcollier ASC;
    ''')

    results = cur.fetchall()
    cur.close()
    conn.close()

title = 'Catalogue Résumé'
headers = ['NomCollier', 'NomChaine', 'nb_Perle', 'NomPerle', 'PrixCollier']

os.chdir('jewelryshop/catalogs')
with open('template.html', 'r') as f:
    template_string = f.read()
    template = Template(template_string)
    result = template.render(data=results, title=title, headers=headers)
    with open(f'catalogsPDF/{title}.pdf', 'wb') as f:
        pisa.CreatePDF(result, dest=f)
print('PDF generated')
