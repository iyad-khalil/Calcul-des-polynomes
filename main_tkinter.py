import tkinter as tk
from tkinter import messagebox
from polynome_utils import calculer_racines, factoriser_polynome, tracer_polynome, formater_racines

def calculer_racines_gui():
    try:
        coefficients = list(map(float, coef_entry.get().strip().split()))
        inclure_complexes = complexe_var.get()
        racines = calculer_racines(coefficients, complexes=inclure_complexes)
        racines_formatees = formater_racines(racines)
        result_var.set(f"Racines : {racines_formatees}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du calcul des racines : {e}")

def factoriser_polynome_gui():
    try:
        coefficients = list(map(float, coef_entry.get().strip().split()))
        polynome_factorise = factoriser_polynome(coefficients)
        result_var.set(f"Polynôme factorisé : {polynome_factorise}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la factorisation : {e}")

def tracer_polynome_gui():
    try:
        coefficients = list(map(float, coef_entry.get().strip().split()))
        tracer_polynome(coefficients)
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du tracé du graphe : {e}")

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Calculateur de Polynômes")
root.geometry("500x400")

# Variables
result_var = tk.StringVar()
complexe_var = tk.BooleanVar()

# Widgets
tk.Label(root, text="Coefficients du polynôme (séparés par des espaces) :").pack(pady=10)
coef_entry = tk.Entry(root, width=50)
coef_entry.pack(pady=5)

tk.Checkbutton(root, text="Inclure les racines complexes", variable=complexe_var).pack(pady=5)

tk.Button(root, text="Calculer les Racines", command=calculer_racines_gui).pack(pady=10)
tk.Button(root, text="Factoriser le Polynôme", command=factoriser_polynome_gui).pack(pady=10)
tk.Button(root, text="Tracer le Graphe", command=tracer_polynome_gui).pack(pady=10)

tk.Label(root, text="Résultat :").pack(pady=10)
tk.Label(root, textvariable=result_var, wraplength=450, justify="left").pack(pady=5)

# Lancer l'application
root.mainloop()
