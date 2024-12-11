from sympy import symbols, solve, factor
import numpy as np
import matplotlib.pyplot as plt
from sympy import diff

def calculer_racines(coefficients, complexes=False):
    """
    Calcule les racines d'un polynôme à partir de ses coefficients.

    Arguments:
    coefficients -- Liste des coefficients du polynôme, du degré le plus élevé au plus bas.
    complexes -- Booléen pour activer la gestion des coefficients complexes.

    Retourne:
    Une liste des racines du polynôme.
    """
    if not coefficients:
        raise ValueError("La liste des coefficients ne peut pas être vide.")
    
    x = symbols('x')
    # Construire le polynôme à partir des coefficients
    polynome = sum(coeff * x**i for i, coeff in enumerate(reversed(coefficients)))
    # Résoudre le polynôme avec ou sans solution complexe
    if complexes:
        racines = solve(polynome, x, domain="CC")  # CC pour Complex Field
    else:
        racines = solve(polynome, x)
    return racines

def factoriser_polynome(coefficients):
    """
    Factorise symboliquement un polynôme à partir de ses coefficients.

    Arguments:
    coefficients -- Liste des coefficients du polynôme, du degré le plus élevé au plus bas.

    Retourne:
    Une expression factorisée du polynôme.
    """
    if not coefficients:
        raise ValueError("La liste des coefficients ne peut pas être vide.")
    
    x = symbols('x')
    polynome = sum(coeff * x**i for i, coeff in enumerate(reversed(coefficients)))
    return factor(polynome)

def formater_racines(racines, precision=4):
    """
    Formate les racines pour les afficher avec une précision donnée.

    Arguments:
    racines -- Liste des racines.
    precision -- Nombre de décimales.

    Retourne:
    Une liste des racines formatées.
    """
    return [round(r.evalf(), precision) for r in racines]

def tracer_polynome(coefficients, xmin=-10, xmax=10, points=500, save_as=None):
    x = np.linspace(xmin, xmax, points)
    y = np.polyval(coefficients, x)
    plt.plot(x, y, label="Polynôme")
    plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
    plt.axvline(0, color='black', linewidth=0.5, linestyle="--")
    plt.title("Graphe du Polynôme")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    if save_as:
        plt.savefig(save_as)
    else:
        plt.show()
    plt.close()



def methode_newton(coefficients, x0=0, tol=1e-6, max_iter=100):
    """
    Résout un polynôme numériquement en utilisant la méthode de Newton-Raphson.

    Arguments:
    coefficients -- Liste des coefficients du polynôme (du degré le plus élevé au plus bas).
    x0 -- Valeur initiale pour l'itération.
    tol -- Tolérance pour l'arrêt de l'itération.
    max_iter -- Nombre maximal d'itérations.

    Retourne:
    La racine approchée trouvée ou une exception si la convergence échoue.
    """
    if not coefficients:
        raise ValueError("La liste des coefficients ne peut pas être vide.")
    
    x = symbols('x')
    # Construire le polynôme et sa dérivée
    polynome = sum(coeff * x**i for i, coeff in enumerate(reversed(coefficients)))
    derivee = diff(polynome, x)
    
    # Initialisation
    iteration = 0
    xn = x0
    
    while iteration < max_iter:
        # Évaluer le polynôme et sa dérivée en xn
        fxn = polynome.subs(x, xn)
        dfxn = derivee.subs(x, xn)
        
        if dfxn == 0:
            raise ValueError("La dérivée s'annule, méthode de Newton échouée.")
        
        # Nouvelle approximation
        xn_next = xn - fxn / dfxn
        
        # Vérifier la convergence
        if abs(xn_next - xn) < tol:
            return float(xn_next)  # Retourner la racine approchée
        
        xn = xn_next
        iteration += 1
    
    raise ValueError("La méthode de Newton n'a pas convergé après le nombre maximal d'itérations.")
