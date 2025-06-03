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
def manger ()
