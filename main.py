from polynome_utils import calculer_racines, factoriser_polynome, formater_racines, tracer_polynome, methode_newton

def afficher_menu():
    """
    Affiche le menu des options pour l'utilisateur.
    """
    print("\n=== Menu ===")
    print("1. Calculer les racines d'un polynôme")
    print("2. Factoriser un polynôme")
    print("3. Tracer le graphe d'un polynôme")
    print("4. Quitter")
    print("5. Trouver une racine avec la méthode de Newton")

def saisir_coefficients():
    """
    Permet à l'utilisateur de saisir les coefficients d'un polynôme.
    """
    print("\nSaisissez les coefficients du polynôme (du degré le plus élevé au plus bas).")
    print("Exemple : Pour x^3 - 6x^2 + 11x - 6, entrez : 1 -6 11 -6")
    try:
        coefficients = list(map(float, input("Coefficients : ").strip().split()))
        if not coefficients:
            raise ValueError("La liste des coefficients ne peut pas être vide.")
        return coefficients
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
        return saisir_coefficients()

def main():
    """
    Point d'entrée principal pour l'application.
    """
    while True:
        afficher_menu()
        choix = input("\nVotre choix : ")

        if choix == "1":
            # Calcul des racines
            coefficients = saisir_coefficients()
            inclure_complexes = input("Inclure les racines complexes ? (o/n) : ").strip().lower() == 'o'
            racines = calculer_racines(coefficients, complexes=inclure_complexes)
            racines_formatees = formater_racines(racines)
            print(f"Les racines du polynôme sont : {racines_formatees}")

        elif choix == "2":
            # Factorisation symbolique
            coefficients = saisir_coefficients()
            polynome_factorise = factoriser_polynome(coefficients)
            print(f"Le polynôme factorisé est : {polynome_factorise}")

        elif choix == "3":
            # Tracer le graphe du polynôme
            coefficients = saisir_coefficients()
            try:
                xmin = float(input("Entrez la valeur minimale de x (par défaut -10) : ") or -10)
                xmax = float(input("Entrez la valeur maximale de x (par défaut 10) : ") or 10)
                points = int(input("Entrez le nombre de points pour le tracé (par défaut 500) : ") or 500)
                tracer_polynome(coefficients, xmin=xmin, xmax=xmax, points=points)
            except Exception as e:
                print(f"Erreur lors du tracé du graphe : {e}")

        elif choix == "4":
            # Quitter
            print("Merci d'avoir utilisé le programme. À bientôt !")
            break

        elif choix == "5":
            # Trouver une racine avec la méthode de Newton
            coefficients = saisir_coefficients()
            try:
                x0 = float(input("Entrez la valeur initiale (x0) : "))
                tol = float(input("Entrez la tolérance (par défaut 1e-6) : ") or 1e-6)
                max_iter = int(input("Entrez le nombre maximal d'itérations (par défaut 100) : ") or 100)
                racine = methode_newton(coefficients, x0=x0, tol=tol, max_iter=max_iter)
                print(f"La racine approchée est : {racine}")
            except Exception as e:
                print(f"Erreur : {e}")

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
