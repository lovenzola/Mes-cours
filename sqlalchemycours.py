# Se connecter à la BD 
from sqlalchemy import create_engine

engine= create_engine("postgresql+psycopg2://postgres:12345678@localhost:5433/Projet_cartes")
connection= engine.connect()
print("Connexion reussie!")
connection.close()

#Création de tables
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
# 1. On prepare la base
engine= create_engine("postgresql+psycopg2://postgres:12345678@localhost:5433/Projet_cartes")
metadonnee= MetaData(schema="Conception_carte")
# 2. On definit la table
etudiants= Table(
    'etudiants', metadonnee,
    Column('id', Integer, primary_key=True),
    Column('nom', String),
    Column('prenom', String),
    Column('matricule', String)
)
#3. On la crée dans la base

metadonnee.create_all(engine)
print("Table créée avec succès!")

# Inserez des elements dans une table
from sqlalchemy import create_engine, Table, Column, MetaData
# D'abord on se connecte
engine= create_engine("postgresql://postgres:12345678@localhost:5433/Projet_cartes")
connection= engine.connect()
# On charge la table à utilisée
metadonnee= MetaData()
table= Table('etudiants', metadonnee, autoload_with=engine, schema="Conception_carte")

# Insertion des données


