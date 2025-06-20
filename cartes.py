from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Dimensions recommandées d'une carte d'étudiant (en points)
CARTE_LARGEUR = 243  # largeur en points
CARTE_HAUTEUR = 153  # hauteur en points

# Créer un canvas avec dimensions personnalisées
c = canvas.Canvas("carte_etudiant_test.pdf", pagesize=(CARTE_LARGEUR, CARTE_HAUTEUR))

# Dessiner un cadre autour de la carte
c.setLineWidth(2)
c.rect(5, 5, CARTE_LARGEUR - 10, CARTE_HAUTEUR - 10)  # petit décalage pour éviter le bord absolu

# Ajouter un titre
c.setFont("Helvetica-Bold", 14)
c.drawCentredString(CARTE_LARGEUR / 2, CARTE_HAUTEUR - 25, "CARTE D'ÉTUDIANT")

# Ajouter des infos fictives
c.setFont("Helvetica", 10)
c.drawString(20, CARTE_HAUTEUR - 50, "Nom : Nzola")
c.drawString(20, CARTE_HAUTEUR - 65, "Post-nom : Samba")
c.drawString(20, CARTE_HAUTEUR - 80, "Prénom : Love")
c.drawString(20, CARTE_HAUTEUR - 95, "Matricule : FASI23-001")
c.drawString(20, CARTE_HAUTEUR - 110, "Promotion : L1")
c.drawString(20, CARTE_HAUTEUR - 125, "Adresse : Bandal, Kinshasa")

# Terminer le PDF
c.save()