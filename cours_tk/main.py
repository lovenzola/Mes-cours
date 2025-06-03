#On importe toutes les données tkinter
from tkinter import *
#1. Créer une fenêtre 

# Toujours créer une variable 
#Une fenetre recoit plusieurs fonctionnalites 
fenetre = Tk() # creation de la fenetre
fenetre.geometry('700x600') # la hauteur et la largeur
fenetre.title('Ma premiere fenetre bien moche') # le titre
fenetre['bg']= 'violet' # le background 
fenetre.resizable(height=False, width=False) # permet d'empecher le redimensionnementl
#fenetre.mainloop()#Afficher la fenetre
# Toujours le remettre pour faire executer une action
# 2. LES WIDGETS 

# Afficher du texte : Label, pack, place
#label = Label (fenetre, text="Il me fume")
#label.pack(side=CENTER, pady=100) # permet d'afficher le texte en haut au centre 
#fenetre.mainloop()
#label.pack(side=LEFT, padx=50) # Permet d'afficher avec précision side: alignement padx: padding x 

#Utilisation du place 
#label.place(x='50',y='30')
#fenetre.mainloop()
# Designer un label 
#C'est dans la definition du label que l'on definit toutes les propriétés du label: zone de texte
#font est une composition de font-size, font-family, font-style,.. bg: background, fg: foreground -- couleur du texte
label = Label (fenetre, text="Il me fume", font=("Verdana", 18, "bold"), bg="aliceblue", fg="bisque")
label.place(x='50',y='30')
sub_label = Label (fenetre, text="Hello guyss", font=("Verdana", 20, "italic bold"), bg='violet', fg= 'whitesmoke')
sub_label.pack()
#fenetre.mainloop()

# 4. BOUTON: Styliser de la même maniere
# Doit recevoir une fonction qu'il va executer
def saluer ():
    print("Tu m'enerves::")

bouton= Button(fenetre, text='click me', bg="blue", fg='white', command= saluer) 
bouton.pack(side=LEFT, padx=20)
#fenetre.mainloop()
# la fonction s'execute dans le terminal

# CREER UN MENU: peut meme recevoir des fonctions
mon_menu= Menu(fenetre) # on cree un menu dans fenetre

# Creation des onglets 

#mon_menu= Menu(mon_menu) # on cree les onglets dans le menu de la  fenetre
#mon_menu.add_cascade(label='fichiers')
#mon_menu.add_cascade(label='settings')
#mon_menu.config(menu= mon_menu)
# Creation de sous-onglets : apres la definition, on cree un lien avec chaque onglet
def modifier ():
    print("Modifié avec succès!")

fichiers = Menu(mon_menu, tearoff=0) # on crée un menu dans les onglets qui sont dans mon menu  puis pas de nvlle fenetre pour les sous onglets  
fichiers.add_command(label='Modifier', command= modifier())
fichiers.add_command(label='Renommer')
fichiers.add_command(label='Supprimer')
fichiers.add_command(label='Nouveau')
fichiers.add_command(label='Enregistrer ')
#-----------------------------------------------------------
settings= Menu(mon_menu, tearoff=0)
settings.add_command(label='General')
settings.add_command(label='Personnalisation')
settings.add_command(label='Se deconnecter')
#-----------------------------------------------------------
mon_menu.add_cascade(label='fichiers', menu=fichiers)
mon_menu.add_cascade(label='settings', menu=settings)


fenetre.config(menu=mon_menu) 

# 4. LES BOITES: Regroupement de widget 
boite = Frame(fenetre, bg='red') # On crée une frame qui va contenir les deux labels comme un bloc __ne pas oublier pack() ou place() apres les labels

label= Label(boite, text="OULALAH")
label.pack()
label2= Label(boite, text="MY GODDD")
label2.pack( )
boite.pack(expand=YES) # Aligner au centre
fenetre.mainloop()

#5. LES IMAGES

