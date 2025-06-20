from reportlab.pdfgen import canvas
from reportlab.lib.colors import whitesmoke, black

carte= canvas.Canvas("mini_carte.pdf", 40,50, pagesize="243x153")
carte.rect(40,50,243,153, stroke=True, fill= None)
carte.setFillColor(whitesmoke)
carte.setLineWidth(1.5)
carte.setStrokeColor(black)
carte.drawImage