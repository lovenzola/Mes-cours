from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Date, Insert
# On importe les modules nécessaires pour une table et autres applications
#D'abord créer une variable qui va contenir l'adresse de la base de données
engine = create_engine("postgresql+psycopg2://postgres:12345678@localhost:5433/Projet_cartes")
#Puis on connecte cette variable
connection = engine.connect()
if connection:
    print("Connexion reussie")
else:
    print("Connexion echoue!")
#MetaData permet d'accéder aux infos d'une table
#On crée une variable qui va permettre de gérer les infos d'une table
metadonne= MetaData(schema="Conception_carte")
paiement = Table(
    'paiement', metadonne,
    Column('id_paiement', Integer, primary_key=True ),
    Column('Nom', String),
    Column('Matricule', String),
    Column('Date_paiement', Date)
)
#Après qu'une table conçue, on la crée dans la table
metadonne.create_all(engine)
if metadonne:
    print("Table creee avec succes!")
else:
    print("Erreur de creation")

#Comment insérer
# On doit toujours definir la requête de la table avant de l'executer sur la BD
#insertion = paiement.insert().values(
   # id_paiement= 1,
   # Nom= "Nzola",
   # Matricule= "SI013",
   # Date_paiement= "2025-05-17" 
#)
# Puis on reconnecte la BD
#connection= engine.connect()
#Connection fait ref a la BD
#La BD execute puis commit pour valider cette transaction
#connection.execute(insertion)
#connection.commit()
#if connection:
    #print("Insertion reussie!")
#else:
    #print("Erreur survenue")

#Comment selectionner une table
from sqlalchemy import select
#On crée une variable qui aura les infos de la table puis la variable qui pointe vers la table choisie
metadata = MetaData()
paiement= Table('etudiants',metadata, autoload_with=engine, schema='Conception_carte')
#On selectionne et on execute
selection= select(paiement)
with engine.connect() as connection:
    resultat= connection.execute(selection) # Contient les infos de la table et pour afficher:
    for ligne in resultat:
        print(ligne)
#Selection avec condition
# Avec where
selecte= select(paiement).where(paiement.c.id==2)
with engine.connect() as connection:
    result = connection.execute(selecte)
    for col in result:
        print("Nouvelle selection" \
        "\n------------------")
        print(col)
# Avec and, or, et not il faut importer
from sqlalchemy import and_, or_, not_
meta= MetaData()
paye = Table('paiement', metadata, autoload_with=engine, schema='Conception_carte')
#inserte= paye.insert().values(
   # id_paiement = 2,
   # Nom= "Kotalo",
   # Matricule = "AE876",
   # Date_paiement = "2025-02-19"
#)
#connection= engine.connect()
#connection.execute(inserte)
#connection.commit()
#if connection:
 #   print("Insertion reussie!")
#else:
 #   print("Erreur survenue!")
#connection.close()

selecti= select(paye)
with engine.connect() as connection:
    resu= connection.execute(selecti)
    for colonne in resu :
        print(colonne)
print("New selection ")
selec= select(paye).where(
    or_(
        and_(
           paye.c.id_paiement == 1 
        ),
        paye.c.Matricule== "SI013"
    )
)
with engine.connect() as connection:
    res= connection.execute(selec)
    for col in res :
        print(col)
#inser= paye.insert().values(
    #id_paiement= 3,
   # Nom= "Bembida",
   # Matricule= "MD567",
   # Date_paiement= "2025-01-14"
#)
#connection= engine.connect()
#connection.execute(inser)
#connection.commit()
sel= select(paye)
with engine.connect() as connection:
    resultats= connection.execute(sel)
    print("Apres mis a jour")
    for line in resultats:
        print("-",line)


# Avec Order By
from sqlalchemy import desc
selectionne= select(paye).order_by(desc(paye.c.Date_paiement))
with engine.connect() as connection:
    re= connection.execute(selectionne)
    print("Trier avec order by desc")
    for col in re:
        print("-", col)
# Si on veut faire de facon ascendante on a pas besoin de preciser
selectionn= select(paye).order_by(paye.c.Date_paiement)
with engine.connect() as connection:
    re= connection.execute(selectionn)
    print("Trier avec order by asc")
    for col in re:
        print("-", col)
#insert= paye.insert().values(
   # id_paiement= 14,
   # Nom = "Munjinga",
   # Matricule= "SI063",
   # Date_paiement= "2025-03-07"
#)
#connection= engine.connect()
#connection.execute(insert)
#connection.commit()
metadonnees= MetaData()
etudiant= Table('etudiants', metadonnees, autoload_with= engine, schema='Conception_carte')
#insert = etudiant.insert().values(
  #  id= 13,
   # nom= "Kalala",
  #  prenom= "Princesse",
  #  matricule= "DR063"
#)
#connection = engine.connect()
#connection.execute(insert)
#connection.commit()
select_limit= select(paye).order_by(desc(paye.c.Nom)).limit(5)
with engine.connect() as connection:
    resolve= connection.execute(select_limit)
    print("Order  y melée au limit")
    for line in resolve :
        print("-",line)
# Limit associé à l' offset
select_offset= select(paye).order_by(paye.c.Nom).limit(4).offset(2)
with engine.connect() as connection:
    resol= connection.execute(select_offset)
    print("Order  y melée au limit et offset")
    for line in resol :
        print("-",line)
#Avec not et like
from sqlalchemy import not_
select_like = select(paye).where(
    not_(paye.c.Matricule.like("SI%"))
)
with engine.connect() as connection:
    revol= connection.execute(select_like)
    print("Avec utilisation du like")
    for line in revol:
        print(line)

# MODIFICATION D'UNE TABLE
from sqlalchemy import Update
mod_matricule= Update(paye).where(paye.c.id_paiement== 3).values(Matricule = "AE567")
connection= engine.connect()
connection.execute(mod_matricule)
connection.commit()
if connection:
    print("Modification reussie!")
else:
    print("Erreur survenue")
# Suppression des lignes d'une table
from sqlalchemy import delete
supp_ligne= delete(paye).where(paye.c.id_paiement==8)
connection= engine.connect()
connection.execute(supp_ligne)
connection.commit()
if connection :
    print("Requete executee avec succes!")
else:
    print("Erreur survenue")
# Modifications avancees 
from sqlalchemy import text
# Cette fonction permettra de faire executer des scripts bruts
#with engine.connect() as connection:
   # connection.execute(text('alter table "Conception_carte"."paiement" add column montant numeric ;'))
   # connection.commit()

# Les jointures
# Inner join
from sqlalchemy import select
jointure= select(
    etudiant.c.nom,
    etudiant.c.matricule,
    paye.c.Date_paiement
).join(paye, etudiant.c.id == paye.c.id_paiement)

with engine.connect() as connection:
    results= connection.execute(jointure)
    print("Avec INNER JOIN")
    for col in results:
        print("-",col)
# Left outer join\ Right outer join \ Cross join \ Full outer join

from sqlalchemy import outerjoin
left_join = select(
    etudiant.c.nom,
    etudiant.c.matricule,
    paye.c.Date_paiement
).select_from(etudiant.outerjoin(paye, etudiant.c.id== paye.c.id_paiement))
with engine.connect() as connection:
    resulto= connection.execute(left_join)
    print("Avec LEFT JOIN")
    for col in resulto:
        print("-",col)
# Pour full outer 
#full_join = select(
 #   etudiant.c.nom,
  #  etudiant.c.matricule,
   # paye.c.Date_paiement
#).select_from(paye,etudiant, etudiant.c.id== paye.c.id_paiement, full=True)
#with engine.connect() as connection:
 #   resultos= connection.execute(full_join)
   # print("Avec FULL JOIN")
    #for col in resulto:
     #   print("-",col)
# Les fonctions d'agregation
from sqlalchemy import func
#1. Count & Group by 
select_count= select (
    paye.c.id_paiement,
    func.count(paye.c.montant).label("Nombre_paiement")
).group_by(paye.c.id_paiement)
with engine.connect() as connection:
    resultoss= connection.execute(select_count)
    for row in resultoss:
        print(row)
# sum, avg, max 
select_sum = select(
    paye.c.Nom,
    paye.c.id_paiement,
    func.sum(paye.c.montant).label("Total_paiement")
).group_by(paye.c.Nom, paye.c.id_paiement)
with engine.connect() as connection:
    ress= connection.execute(select_sum)
    for row in ress:
        print(row)
select_total= select(func.sum(paye.c.montant).label("Total_paiement"))
with engine.connect() as connection:
    resst= connection.execute(select_total)
    for row in resst:
        print(row)
select_max= select(func.max(paye.c.montant).label("Max_paiement"))
with engine.connect() as connection:
    resst= connection.execute(select_max)
    for row in resst:
        print(row)
select_moyenne= select(func.round(func.avg(paye.c.montant).label("Moyenne_paiement")),2)
with engine.connect() as connection:
    resst= connection.execute(select_moyenne)
    for row in resst:
        print(row)

# Les transactions : permet de faire executer deux taches à la fois pas l'une sans l'autre
#Deux facons d'ecrire :
# The first
connection= engine.connect()
#trans= connection.begin()
#try:
 #   operation= paye.insert().values(id_paiement = 15, Nom = "Bembida",Matricule = "MD890",montant= 900)
  #  connection.execute(operation)
    # L'on peut rajouter d'autres requetes
   # trans.commit()
    #print("Transaction reussie")
#except Exception as e: 
 #   trans.rollback()
  #  print("ERREUR :",e)
# Avec with engine.begin
#with engine.begin() as connection:
 #   connection.execute(
  #      paye.insert().values(
   #         id_paiement= 17, Nom = 'Sephora', Matricule= "AE401", montant= 1000 
    #    )
    #)
#if connection:
  #  print("Transaction reussie")
# Dans ce cas le commit et rollback sont automatiques

# Les binparam() permettent de créer des parametres reutilisables 
from sqlalchemy import bindparam
definition= Update(paye).where(paye.c.id_paiement == bindparam('id_value')).values(Nom= bindparam('nouveau_nom'))
# Ces parametres permettent de faire plusieurs modifications sans avoir à toujours mettre le Update
# Utiliser aussi avec le select, insert, etc...

action = [
    {'id_value': 4, 'nouveau_nom' : 'Deborah'},
    {'id_value': 6, 'nouveau_nom' : 'Emerance'},
    {'id_value': 11, 'nouveau_nom' : 'Divine'},
    {'id_value': 3, 'nouveau_nom' : 'Asnath'},
    {'id_value': 6, 'nouveau_nom' : 'Joseph'}
]
with engine.begin() as connection:
    connection.execute(definition, action)

# Les fonctions avancées 
from  sqlalchemy import select, func
#A. Liéés au texte
# 1. Mettre le texte en miniscule\ majuscule (upper)\ Majuscule en debut (Initcap)
minisc= select(func.lower(paye.c.Nom))
with engine.connect() as connection:
    resul= connection.execute(minisc).fetchall()
    for row in resul:
        print("-",row)

# 2. Extraire une partie du texte : substring

#B. Liéés aux dates
# 1. Now(): Date et heure actuelles :

datheure= select(func.now())
with engine.connect() as connection:
    resultatss = connection.execute(datheure).scalar() # scalar permet de convertir la date
    print("Date et heure actuelle: ", resultatss)
# 2. CURRENT_DATE et current_time : renvoie la date du jour uniquement ou l'heure uniquement

# 3. AGE : permet de calculer une durée. 
# Premier cas avec now() donne les jours, secondes et microsecondes 
calcul = select(func.age(func.now(), paye.c.Date_paiement))
with engine.connect() as connection: 
    resss= connection.execute(calcul)
    for row in resss:
        print("Duree:", row)
# Renvoie juste les jours 
calcula = select(func.age(paye.c.Date_paiement)) 
with engine.connect() as connection: 
    resss= connection.execute(calcula)
    for row in resss:
        print("Duree:",row)

# 4. date_part() permet d'extraire juste une partie de date, day,month, hour, minute, second, year
year = select(func.date_part('month',paye.c.Date_paiement)) 
with engine.connect() as connection: 
    resss= connection.execute(year)
    for row in resss:
        print("Mois de paiement:", row)
# 5. EXTRACT() equivalent à date_part()  sous un autre nom

# Les fonctions conditionnelles 
#A. CASE 
from sqlalchemy import case
casee= select(
    paye.c.montant,
    case((paye.c.montant >= 970, 'Pret pour la carte'),
         else_='En attente').label('statut')
)
with engine.connect() as connection:
    for row in connection.execute(casee):
        print(row)
# Exemple plus avancé 
# Il consiste à mettre un statut par rapport au matricule
statut_case = case(
    (
        and_(
            paye.c.Matricule.like('SI%'),
            paye.c.montant >= 970
        ), 'Pret pour la carte'
    ),
    (
        and_(
            paye.c.Matricule.like('AE%'),
            paye.c.montant >= 915
        ),  'Pret pour la carte'
    ),
    (
        and_(
            paye.c.Matricule.like('MD%'),
            paye.c.montant >= 930
        ), 'Pret pour la carte'
    ),
    (
        and_(
            paye.c.Matricule.like('DR%'),
            paye.c.montant >= 870
        ),'Pret pour la carte'
    ),
    (
        and_(
            paye.c.Matricule.like('TH%'),
            paye.c.montant >= 850
        ), 'Pret pour la carte'
    ),
    else_= 'Non eligible'
).label('Statut')

caser = select(
    paye.c.Nom,
    paye.c.montant,
    statut_case,
    func.sum(paye.c.montant)).group_by(paye.c.id_paiement).order_by(paye.c.Nom)

with engine.connect() as connection:
    for row in connection.execute(caser):
        print(row)

# COALESCE permet de prendre la premiere valeur non null 

coale= select(
    etudiant.c.nom,
    func.coalesce(etudiant.c.prenom, 'Vide').label('prenom')
)

with engine.connect() as connection:
    for row in connection.execute(coale):
        print(row)

# LES SOUS REQUETES: Ce sont des requêtes qu'on imbrique comme element dans les requettes principales
# 1. Sous-requête avec subquery() cree une table temporaire puis sera utilisée dans une requete
# Ici la sous-requete est reutilisée dans une requete (dans un FROM)
# On peut l'utiliser avec join, exists
sous_req= select(paye.c.id_paiement).where(paye.c.montant >= 700).subquery()
reque_principale= select(etudiant.c.nom).where(etudiant.c.id.in_(sous_req))

with engine.connect() as connection:
    for row in connection.execute(reque_principale):
        print(row)
    
# Sous requete avec alias : juste une nouvelle façon de nommer une requête interne

sous_requête = (
    select(
        paye.c.id_paiement,
        func.sum(paye.c.montant).label('total_paye')
    )
    .group_by(paye.c.id_paiement)
    .alias('totaux')
)

requete= (
    select(
        etudiant.c.nom, sous_requête.c.total_paye
    )
    .join (sous_requête, sous_requête.c.id_paiement == etudiant.c.id)
    .where(sous_requête.c.total_paye > 700)
)

with engine.connect() as connection:
    for row in connection.execute(requete):
        print(row)

# scalar subquery: Sous-requete utilisée dans le where, select,... est une donnée(valeur) et non pas une table

sous= select(func.max(paye.c.montant)).scalar_subquery()
principale= select(paye.c.Nom).where(paye.c.montant > sous)
with engine.connect() as connection:
    for row in connection.execute(principale):
        print(row)

# LES METADONNEES
# Permettent d'accéder aux données de la Table 
# Deux approches 
# A. Avec METADATA pour refleter les elts cad structure de la BD

meta= MetaData("Conception_carte")
meta.reflect(bind=engine) 
# 1. Afficher toutes les tables
print(meta.tables.keys())

#2. Accéder à une table précise
# paiement= meta.tables['nom_table']
#B.Avec inspect 
from sqlalchemy import inspect
insp= inspect(engine)
#Voir les tables du schema public ou autre
print(insp.get_table_names(schema="Conception_carte"))

# Voir toutes les colonnes 
for col in insp.get_columns('paiement', schema='Conception_carte'):
    print(col['name'],":",col['type']) # Renvoie le nom et son type

print(insp.get_pk_constraint('paiement', schema='Conception_carte'))
