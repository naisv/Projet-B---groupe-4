#Module de la méthode des rectangles

import numpy as np
from solution_analytique import polynome, compute_solution_analytique


def integration_rectangle_base(a, b, n):
    """
    Calcule l'intégrale numérique par la méthode des rectangles.
    """

    #Calcul du pas
    h = (b - a) / n
    somme_aires = 0.0

    for i in range(n):
        x_i = a + i * h
        # Évaluation de la fonction de degré 3 au point x_i
        f_xi = polynome(x_i)
        somme_aires += f_xi * h

    return somme_aires

def integration_rectangle_numpy(a, b, n):
    """
    Calcule l'intégrale numérique avec la méthode des rectangles
    en utilisant NumPy (Vectorisé)
    """

    # Calcul du pas
    h = (b - a) / n

    # Création d'un tableau contenant tous les points x_i (de 0 à n-1)
    # np.arange(n) génère [0, 1, 2, ..., n-1]
    x = a + np.arange(n) * h

    # Évaluation de la fonction pour TOUS les points x en même temps
    f_x = polynome(x)

    # Somme des aires : (f(x_0) + f(x_1) + ... + f(x_n-1)) * h
    somme_aires = np.sum(f_x) * h

    return somme_aires
