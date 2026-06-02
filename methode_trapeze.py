#Module de la méthode des trapèzes

#Importation des fonctions qui retournent le polynome et son intégrale exacte (solution analytique)
from solution_analytique import polynome, compute_solution_analytique

"""Fonction calculant l'intégrale d'une fonction selon la méthode des trapèzes en utilisant python de base
Prend en entrée: intervalle [a,b] et le nombre de segments n
Retourne la valeur de l'intégrale calculée selon la méthode des trapèzes"""
def trap_python(a,b,n):
    somme=0
    for i in range(n):
        borne_inf=a+i*(b-a)/n
        borne_sup=a+(i+1)*(b-a)/n
        trapeze=(borne_sup-borne_inf)*(polynome(borne_sup)+polynome(borne_inf))/2
        somme+=trapeze
    return somme