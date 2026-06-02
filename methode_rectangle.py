#Module de la méthode des rectangles

from solution_analytique import polynome, compute_solution_analytique


def integration_rectangle_base(a, b, n):
    """
    Calcule l'intégrale numérique par la méthode des rectangles.
    """
    h = (b - a) / n
    somme_aires = 0.0

    for i in range(n):
        x_i = a + i * h
        # Évaluation de la fonction de degré 3 au point x_i
        f_xi = polynome(x_i)
        somme_aires += f_xi * h

    return somme_aires

def compute_erreur_rectangle(a, b, n):
    return compute_solution_analytique(a, b) - integration_rectangle_base(a, b, n)