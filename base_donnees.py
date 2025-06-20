from sqlalchemy import create_engine 
engine= create_engine('postgresql+psycopg2://user:12345678@localhost:5433/Projet_cartes')

import psycopg2
try:
    conn= psycopg2.connect(
        dbname= "Projet_cartes",
        user= "postgres",
        password= "12345678",
        host= "localhost",
        port= "5433"
    )
    print("Connexion reussie a Postgresql !")
    

except Exception as e:
    print("Erreur survenue lors de la connexion:", e)

cur= conn.cursor()
cur.execute("""Select table_name from information_schema.tables where table_schema= 'Conception_carte'""")

tables= cur.fetchall()
print("Tables dans la base de données :")
if not tables:
    print("Aucune table créée.")
else:
    for table in tables:
        print(table[0])
cur.close()
conn.close()

