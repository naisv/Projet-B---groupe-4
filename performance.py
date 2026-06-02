#Calcul de la performance des differentes methodes

from solution_analytique import compute_solution_analytique
from methode_rectangle import *

def compute_erreur(a, b, n, fonction):
    """
    fonction qui calcule l'erreur entre la methode choisie et la valeur analytique
    """
    return compute_solution_analytique(a,b) - fonction(a,b,n)
import timeit












def temps_exec(fonction):
    return timeit.timeit(fonction, number=100)

