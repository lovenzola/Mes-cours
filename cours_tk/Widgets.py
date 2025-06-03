from tkinter import *
from tkinter import ttk

root= Tk()
button = ttk.Button(root, text="Hello", command="buttonpressed")
button.grid() # Comme pack
#root.mainloop()

#L'on peut modifier  un element en faisant:
button['text']= "Goodbye"
#root.mainloop()

#Autre manière
button.configure(text="ANYMORE")
#root.mainloop()

# bind est une fonction qui saisi un evenement et execute le code 
l =ttk.Label(root, text="Starting...")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<3>', lambda e: l.configure(text='Clicked right mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
root.mainloop()

# les evenements entre guillemets 
