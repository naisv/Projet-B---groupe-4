#Module de la méthode des trapèzes

#Importation de la bibliothèque Numpy
import numpy as np

#Importation des fonctions qui retournent le polynome et son intégrale exacte (solution analytique)
from solution_analytique import polynome, compute_solution_analytique

"""Fonction calculant l'intégrale d'une fonction selon la méthode des trapèzes en utilisant Python de base
Paramètres en entrée: intervalle [a,b] et le nombre de segments n
Retourne la valeur de l'intégrale calculée selon la méthode des trapèzes"""
def trap_python(a,b,n):
    h=(b-a)/n #calcul du pas
    somme_aires= 0.0
    for i in range(n):
        borne_inf=a+i*h
        borne_sup=a+(i+1)*h
        trapeze=1/2*(borne_sup-borne_inf)*(polynome(borne_sup)+polynome(borne_inf))
        somme_aires+=trapeze
    return somme_aires

#Fonction calculant l'intégrale entre [a,b] fixé en paramètre selon la méthode des trapèzes en utilisant Numpy
def trap_numpy(a,b,n):
    x=np.linspace(a,b,n+1) #tableau avec n valeurs uniformément réparties entre a et b
    y=polynome(x) #tableau avec les images de x de la fonction polynome
    h=(b-a)/n #calcul du pas
    somme_aires=h*(np.sum(y)-0.5*(y[0]+y[-1]))
    return somme_aires
