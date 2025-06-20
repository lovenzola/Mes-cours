# A. CREER UNE FENETRE et PERSONNALISATION
import tkinter as tk
# Creer la fenetre
root= tk.Tk()
# Personnaliser : titre, dimension, icone
root.title('Ma premiere page')
root.geometry('600x450')
root.resizable(False, False) # Empeche le redimensionnement

# B. AJOUT DES WIDJETS
# On commence par le specifier puis l'afficher avec pack ()
# 1. LABEL: pour afficher un texte
label = tk.Label(root, text='Apprenons Tkinter')
label.pack() 
# 2. BUTTON: reagir à une action (comprise dans une fonction)
def saluer():
    print("Bienvenue dans ce nouveau cours")

bouton= tk.Button(root, text="Cliquez", command=saluer)
bouton.pack()

# ENTRY: champ de saisi du texte, une ligne unique

champ= tk.Entry(root) #Affiche un champ de saisi sur la fenêtre
champ.pack()
# Pour recuperer la valeur entrée
champ.get()
# TEXT: Zone de saisi multi-lignes. Reçoit une largeur et hauteur

texte= tk.Text(root, height=5, width=50)
texte.pack()
# Pour recuperer la valeur entrée
texte.get("1.0",tk.END) # 1.0 signifie ligne 1, colonne 0 cad le debut jusqua END, la fin

# Checkbutton : fouurnit des cases que l'on peut cocher. Les choix sont TRUE and FALSE stockés dans une variable

var= tk.BooleanVar()
check= tk.Checkbutton(root, text='Vous êtes prêt???', variable= var)
check.pack()
# L'on peut recuperer la valeur choisie avec 
var.get()

# RadioButton: choix unique parmi choix multiples
genre= tk.StringVar()
choix1 = tk.Radiobutton(root, text='Femme', value= 'F', variable= genre)
choix2 = tk.Radiobutton(root, text='Homme', value= 'H', variable= genre)
choix1.pack()
choix2.pack()
# L'on peut recuperer la valeur choisie avec 
genre.get()

# Listbox: liste deroulante avec choix multiples
titre= tk.Label(root, text='Choisissez les notions connues')
titre.pack()
liste= tk.Listbox(root)
liste.insert(1, "Creation et personnalisation de fenetres")
liste.insert(2, "Les widgets")
liste.insert(3, "Geometrie")
liste.insert(4, "images, polices et couleurs")
liste.insert(5, "Options avancées")
liste.pack()

root.mainloop()
#Pour recuperer les valeurs choisies
#selection = liste.get(liste.curselection)
# C. Methodes de placements
# 1. PACK()
# 2. GRID()
roote = tk.Tk()
roote.geometry("100x150")
tk.Label(roote, text="Nom").grid(row=0, column=0)
tk.Entry(roote).grid(row=0, column=1, padx= 5, pady= 5, sticky="e")

tk.Label(roote,text="Age").grid(row=1,column=0)
tk.Entry(roote).grid(row=1, column=1, padx= 5, pady= 5, sticky="s")
roote.mainloop()

# D. Gestion d'evenements et callbacks dans tkinter

# 1. Avec les boutons et callback de la fonction definie
# Voir widget bouton
# 2. Lire ce que l'utilisateur a entrer

def afficher_nom():
    nom = champ_nom.get()
    print('Nom saisi:', nom)
rootez= tk.Tk()
rootez.geometry("600x350")
champ_nom= tk.Entry(rootez)
champ_nom.pack()
btn= tk.Button(rootez, text='Afficher', command=afficher_nom)
btn.pack()

# 3. Evenements du clavier ou souris avec .bind()
# 3.1 Liés au clavier
# Pour chaque touche pressée
def touche(event):
    print("Touche pressee:", event.keysym)

rootez.bind("<Key>", touche)

# detecter la touche Enter
def valider(event):
    print("Message validee")
champ= tk.Entry(rootez)
champ.pack()
champ.bind("<Return>", valider)


# 3.2 Liés à la souris 
def clic(event):
    print(f"Clic detecté à x= {event.x}, y= {event.y}")

rootez.bind("<Button-1>",clic) 
rootez.mainloop()

# Exercice 
def valide(event):
    texte= champ_texte.get()
    print("Texte saisi:", texte)
fenetre= tk.Tk()
fenetre.title("Mon app")
fenetre.geometry("900x700")
fenetre.resizable(False, False)
champ_texte= tk.Entry(fenetre)
champ_texte.pack()
champ_texte.bind("<Return>", valide)
# 6. MENU BAR ET BARRE D'OUTILS 
# 6.1 MENU
#Creation du menu dans la fenetre
menu_bar = tk.Menu(fenetre)
# Definition des commandes
def quitter():
    root.quit()
# Definition des sous menus
menu_fichier = tk.Menu(menu_bar, tearoff=0)
menu_accueil = tk.Menu(menu_bar, tearoff=0)
menu_parametres = tk.Menu(menu_bar, tearoff=0)
# Creation des options dans les sous menu
menu_fichier.add_command(label="Enregistrer")
menu_fichier.add_command(label="Ajouter un etudiant")
menu_fichier.add_command(label="Renommer")
menu_fichier.add_command(label="Nouveau")
#----------------------------------------------------------------------------------------------
menu_accueil.add_command(label="Profil")
menu_accueil.add_command(label="Texte")
menu_accueil.add_command(label="Mon compte")
#----------------------------------------------------------------------------------------------
menu_parametres.add_command(label="Deconnexion")
menu_parametres.add_command(label="Securite")
menu_parametres.add_command(label="Quitter", command= quitter)
#---------------------------------------------------------------------------------------------
# Stockage dans le menu
menu_bar.add_cascade(label="Fichier", menu=menu_fichier)
menu_bar.add_cascade(label="Accueil", menu=menu_accueil)
menu_bar.add_cascade(label="Parametres", menu=menu_parametres)
#---------------------------------------------------------------------------------------------
# Ajout dans la fenetre
fenetre.config(menu=menu_bar)


# 6.2 BARRE D'OUTILS (Mieux compris avec les frames)
# 1. Creation de la barre d'outils dans une frame 
barre_outil = tk.Frame(fenetre, bd=1, relief=tk.RAISED)

# 2. Definition des commandes 
def nouveau():
    print("Creer un nouveau fichier...")

def supprimer():
    print("Suppression du fichier...")

#3. Definition des boutons
bouton1= tk.Button(barre_outil, text="Nouveau", command=nouveau)
bouton1.pack(side=tk.LEFT, padx=2, pady=2)
bouton2= tk.Button(barre_outil,text="Supprimer", command=supprimer)
bouton2.pack(side=tk.LEFT, padx=2, pady=2)

# Affichage de la barre d'outils 
barre_outil.pack(side=tk.TOP, fill= tk.X)



#7. TOPLEVEL : fenêtre secondaire liéée à la fenêtre principale, elle peut être ouverte par un bouton par exemple

#Definition de la commande 
def ouvrir():
    fenetre_alerte = tk.Toplevel(fenetre)
    fenetre_alerte.title("Alerte")
    fenetre_alerte.geometry("400x400")
    label= tk.Label(fenetre_alerte,text="Votre requete a ete soumis avec succes")
    label.pack(pady=45)
labele= tk.Label(fenetre, text="Soumettez votre requete")
labele.pack()
texter= tk.Text(fenetre,height=5,width=100)
texter.pack()
boutn= tk.Button(fenetre, text="Envoyer", bg="aliceblue", command=ouvrir)
boutn.pack()

# 8. LES VARIABLES TKINTER permettent de stocker les valeurs entrées, mettre une valeur par defaut ou les modifier.
# Ces variables sont : IntVar(), StringVar(), BooleanVar(), DoubleVar()
# Stocker
nom= tk.StringVar() # Definition d'une variable
label= tk.Label(fenetre, text="Entrez votre nom")
label.pack()
entree= tk.Entry(fenetre, textvariable=nom) # la valeur sera stockée dans la variable nom
entree.pack()
def afficher():
    print("Nom saisi:", nom.get())

btn1= tk.Button(fenetre, text="Afficher", command=afficher)
btn1.pack()

# Mettre une valeur par defaut
nom= tk.StringVar() # Definition d'une variable
nom.set("Nzola") # La valeur par defaut
label= tk.Label(fenetre, text="Entrez votre nom")
label.pack()
entree= tk.Entry(fenetre, textvariable=nom) # la valeur sera stockée dans la variable nom
entree.pack()
def afficher():
    print("Nom saisi:", nom.get())

btn2= tk.Button(fenetre, text="Afficher", command=afficher)
btn2.pack()

# Pour modifier 
nom= tk.StringVar() # Definition d'une variable
label= tk.Label(fenetre, text="Entrez votre nom")
label.pack()
entree= tk.Entry(fenetre, textvariable=nom) # la valeur sera stockée dans la variable nom
entree.pack()
def effacer():
    nom.set(" ")
btn3= tk.Button(fenetre, text="Effacer", command= effacer)
btn3.pack()
# Modifier 
nom= tk.StringVar() # Definition d'une variable
#--------------------------------------------------------------------------------------
def dire_oui():
    print("Je suis de cet avis ")
def dire_non():
    print("Je ne suis pas de cet avis ")
boutn1= tk.Button(fenetre, text="OUI", command=dire_oui)
boutn1.pack()
boutn2= tk.Button(fenetre, text="NON", command=dire_non)
boutn2.pack()
entree= tk.Entry(fenetre, textvariable=nom) # la valeur sera stockée dans la variable nom
entree.pack()
label= tk.Label(fenetre, text="Etes vous de cet avis?")
label.pack()
def modifier():
    nom.set("Je m'abstiens")
btn1= tk.Button(fenetre, text="S'abstenir", command=modifier)
btn1.pack()
fenetre.mainloop()
# 9. LES FRAMES
new_fenetre= tk.Tk()
new_fenetre.geometry("300x300")
new_fenetre.resizable(False,False)
#--------------------------------------------------------------------------------------------------------
header= tk.Frame(new_fenetre, bg="aliceblue",borderwidth=2, relief="groove", padx=10, pady=10)
header.pack(padx=20, pady=20)
section= tk.Frame(new_fenetre, bg="bisque", pady=40)
section.pack(side="bottom", fill="x")
#---------------------------------------------------------------------------------------------------------
def nouveau():
    print("Ajout d'un nouveau dossier")
def enregistrer():
    print("Enregistré avec succès")
#---------------------------------------------------------------------------------------------------------
tk.Button(section, text="Ajouter", command=nouveau).pack(pady=10)
tk.Button(section, text="Enregistrer", command=enregistrer).pack()
new_fenetre.mainloop()

# EXERCICE
fenestra= tk.Tk()
fenestra.geometry("800x500")
fenestra.resizable(False,False)
#frame1= tk.Frame(fenestra,bg="white", borderwidth=2, relief="groove", padx=10, pady=10)
#frame1.pack(side=tk.LEFT,padx=20,pady=20)
#tk.Label(frame1, text="Nom:").grid(row=0, column=0, padx=10)
#tk.Entry(frame1).grid(row=0, column=1)
conteneur= tk.Frame(fenestra)
conteneur.pack()
gauche= tk.Frame(conteneur, bg="blue")
droite= tk.Frame(conteneur,bg="red")
gauche.pack(side="left", fill="y")
droite.pack(side="right", fill="y")

fenestra.mainloop()











