#Module de calcul de la solution analytique

#Importation des variables globales des coefficients de la fonction polynomiale
from main import p1,p2,p3,p4

#Fonction qui retourne la valeur de la fonction polynomiale pour un x donné en entrée
def polynome(x):
    return p1+p2*x+p3*(x**2)+p4*(x**3)

#Fonction qui calcule l'intégrale analytiquement d'une fonction polynomiale sur un intervalle [a,b] fixé en entrée
def compute_solution_analytique(a,b):
    F_a = p1 * a + (p2 / 2) * (a ** 2) + (p3 / 3) * (a ** 3) + (p4 / 4) * (a ** 4)
    F_b = p1 * b + (p2 / 2) * (b ** 2) + (p3 / 3) * (b ** 3) + (p4 / 4) * (b ** 4)
    return F_b - F_a