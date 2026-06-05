#Module de la méthode Simpson

from solution_analytique import polynome, compute_solution_analytique
import numpy as np
def simpson_basique(a, b, n=10):
    #Fonction calculant l'intégrale numérique par la méthode de Simpson codée en Python de base
    h=(b-a)/n #Calcul du pas
    u=a #correspond au "a" de la formule dans l'énoncé du devoir
    v=a+h #correspond au "b" de la formule dans l'énoncé du devoir
    somme_aires=0.0
    for i in range(n):
        somme_aires+=(v-u)/6*(polynome(u)+4*polynome((u+v)/2)+polynome(v))
        #On avance d'un pas
        u=v
        v+=h
    return somme_aires

def simpson_numpy(a,b, n=10):
    # Fonction calculant l'intégrale numérique par la méthode de Simpson codée en Numpy (vectorisé)
    valeurs=np.linspace(a,b,n+1)
    u=valeurs[:-1] #la valeur a ne peut jamais être égale à la borne finale (b)
    v=valeurs[1:] #la valeur b ne peut jamais être égale à la borne initiale (a)
    f_valeurs=(polynome(u)+polynome(v)+4*polynome((u+v)/2))*(v-u)/6
    somme_aires=np.sum(f_valeurs)
    return somme_aires
