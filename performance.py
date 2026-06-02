#Calcul de la performance des differentes methodes
import timeit












def temps_exec(fonction):
    return timeit.timeit(fonction, number=100)

