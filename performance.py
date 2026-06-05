#Calcul de la performance des différentes méthodes

import timeit
from solution_analytique import compute_solution_analytique
from methode_rectangle import *

def compute_erreur(a, b, n, fonction):
    #fonction qui calcule l'erreur absolue entre la methode choisie mise en paramètre et la valeur analytique
    return abs(compute_solution_analytique(a,b) - fonction(a,b,n))

def temps_exec(fonction):
    #fonction qui mesure 100 fois le temps d'exécution d'une fonction mise en paramètre retourne sa moyenne
    return timeit.timeit(fonction, number=100)


    return liste_n,solutions