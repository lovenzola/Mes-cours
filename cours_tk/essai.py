import tkinter as tk
from tkinter import ttk, messagebox

# ------------------ COULEURS ------------------ #
COLOR_BG_DARK = "#0D1B2A"
COLOR_BG_LIGHT = "#1B263B"
COLOR_TEXT_WHITE = "#FFFFFF"
COLOR_TEXT_BLACK = "#000000"
COLOR_BUTTON = "#0077B6"
FONT_TITLE = ("Helvetica", 18, "bold")
FONT_NORMAL = ("Helvetica", 12)

# ------------------ APPLICATION PRINCIPALE ------------------ #
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conception automatique des cartes d’étudiants")
        self.geometry("800x500")
        self.resizable(False, False)
        self.configure(bg=COLOR_BG_DARK)

        self.attempts = 0  # Compteur pour la connexion
        self.current_frame = None
        self.show_welcome()

    # Affiche une section donnée
    def switch_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)

    # Accueil initial
    def show_welcome(self):
        frame = tk.Frame(self, bg=COLOR_BG_DARK)
        frame.pack(fill="both", expand=True)

        title = tk.Label(frame, text="🎓 Gestion des Cartes Étudiants", fg=COLOR_TEXT_WHITE, bg=COLOR_BG_DARK, font=FONT_TITLE)
        title.pack(pady=100)

        start_btn = tk.Button(frame, text="Se connecter", command=lambda: self.switch_frame(LoginPage),
                              bg=COLOR_BUTTON, fg=COLOR_TEXT_WHITE, font=FONT_NORMAL, width=20)
        start_btn.pack()

        self.current_frame = frame

# ------------------ PAGE DE CONNEXION ------------------ #
class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=COLOR_BG_LIGHT)

        tk.Label(self, text="Connexion", bg=COLOR_BG_LIGHT, fg=COLOR_TEXT_WHITE, font=FONT_TITLE).pack(pady=20)

        self.username_entry = self.create_input("Nom d’utilisateur :")
        self.password_entry = self.create_input("Mot de passe :", show="*")

        login_btn = tk.Button(self, text="Se connecter", bg=COLOR_BUTTON, fg=COLOR_TEXT_WHITE, font=FONT_NORMAL,
                              command=self.attempt_login)
        login_btn.pack(pady=20)

    def create_input(self, label_text, show=None):
        tk.Label(self, text=label_text, bg=COLOR_BG_LIGHT, fg=COLOR_TEXT_WHITE, font=FONT_NORMAL).pack(pady=(10, 0))
        entry = tk.Entry(self, show=show, font=FONT_NORMAL, width=30)
        entry.pack()
        return entry

    def attempt_login(self):
        user = self.username_entry.get()
        pwd = self.password_entry.get()

        if user == "admin" and pwd == "admin":
            self.master.switch_frame(DashboardPage)
        else:
            self.master.attempts += 1
            messagebox.showerror("Erreur", "Identifiants incorrects.")
            if self.master.attempts >= 5:
                messagebox.showwarning("Bloqué", "Trop de tentatives. Réessaye plus tard.")
                self.master.destroy()

# ------------------ TABLEAU DE BORD ------------------ #
class DashboardPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=COLOR_BG_DARK)

        tk.Label(self, text="Tableau de bord", bg=COLOR_BG_DARK, fg=COLOR_TEXT_WHITE, font=FONT_TITLE).pack(pady=20)

        btn_paiement = tk.Button(self, text="➕ Enregistrer un paiement", command=self.simulate_paiement,
                                 bg=COLOR_BUTTON, fg=COLOR_TEXT_WHITE, font=FONT_NORMAL, width=30)
        btn_paiement.pack(pady=10)

        btn_generer = tk.Button(self, text="🖨 Générer une carte", command=self.simulate_generation,
                                bg=COLOR_BUTTON, fg=COLOR_TEXT_WHITE, font=FONT_NORMAL, width=30)
        btn_generer.pack(pady=10)

        btn_historique = tk.Button(self, text="📜 Voir l'historique", command=self.simulate_historique,
                                   bg=COLOR_BUTTON, fg=COLOR_TEXT_WHITE, font=FONT_NORMAL, width=30)
        btn_historique.pack(pady=10)

        btn_logout = tk.Button(self, text="🔒 Déconnexion", command=lambda: master.switch_frame(LoginPage),
                               bg="red", fg=COLOR_TEXT_WHITE, font=FONT_NORMAL, width=20)
        btn_logout.pack(pady=40)

    def simulate_paiement(self):
        messagebox.showinfo("Paiement", "Paiement enregistré (simulation).")

    def simulate_generation(self):
        messagebox.showinfo("Génération", "Carte générée (simulation).")

    def simulate_historique(self):
        messagebox.showinfo("Historique", "Historique affiché (simulation).")

# ------------------ LANCEMENT ------------------ #
if __name__ == "__main__":
    app = App()
    app.mainloop()