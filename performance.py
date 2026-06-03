#Calcul de la performance des differentes methodes

import timeit
from solution_analytique import compute_solution_analytique
from methode_rectangle import *

def compute_erreur(a, b, n, fonction):
    """
    fonction qui calcule l'erreur entre la methode choisie et la valeur analytique
    """
    return compute_solution_analytique(a,b) - fonction(a,b,n)

def temps_exec(fonction):
    return timeit.timeit(fonction, number=100)

def convergence (fonction, a,b,n_max=1000,pas=20):
    solutions=[]
    liste_n=[]
    for i in range (pas,n_max+1,pas):
        liste_n.append(i)
        solutions.append(fonction(a,b,i))

    return liste_n,solutions