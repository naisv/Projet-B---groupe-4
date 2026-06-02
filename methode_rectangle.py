#Module de la méthode des rectangles

from solution_analytique import polynome

def integration_rectangle(a_inf, b_sup, n):
    """
    Calcule l'intégrale numérique par la méthode des rectangles.
    """
    h = (b_sup - a_inf) / n
    somme_aires = 0.0

    for i in range(n):
        x_i = a_inf + i * h
        # Évaluation de la fonction de degré 3 au point x_i
        f_xi = polynome(x_i)
        somme_aires += f_xi * h

    return somme_aires