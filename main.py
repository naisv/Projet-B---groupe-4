#MGA802 - Mini projet B - Groupe 4
#Script principal

#Définition des variables globales : coefficients de la fonction polynomiale
p1=1
p2=1
p3=1
p4=1

import pandas as pd

from solution_analytique import compute_solution_analytique
from performance import compute_erreur, temps_exec
from methode_rectangle import integration_rectangle_base, integration_rectangle_numpy
from methode_trapeze import trap_python, trap_numpy
from methode_simpson import simpson_basique, simpson_numpy

if __name__ == "__main__":
    #parametres des integrales
    borne_inf = 1
    borne_sup = 10
    tailles_segments = [100, 1000, 10000]

    dictionnaire_fonctions = {
        "Rectangles": {
            "base": integration_rectangle_base,
            "numpy": integration_rectangle_numpy
        },
        "Trapèzes": {
            "base": trap_python,
            "numpy": trap_numpy
        },
        "Simpson": {
            "base": simpson_basique,
            "numpy": simpson_numpy
        }
    }

    # Liste des méthodes pour l'index du tableau
    liste_methodes = ["Rectangles", "Trapèzes", "Simpson"]

    # Création de l'index des lignes
    index_lignes = pd.MultiIndex.from_product(
        [["Erreur Absolue", "Temps total (s)"], liste_methodes],
        names=["Métrique", "Méthode"]
    )

    colonnes_dataframe = {}

    for n in tailles_segments:
        erreurs_base, erreurs_numpy = [], []
        temps_base, temps_numpy = [], []

        for methode in liste_methodes:
            f_base = dictionnaire_fonctions[methode]["base"]
            f_numpy = dictionnaire_fonctions[methode]["numpy"]

            # Calcul des erreurs
            erreurs_base.append(abs(compute_erreur(borne_inf, borne_sup, n, f_base)))
            erreurs_numpy.append(abs(compute_erreur(borne_inf, borne_sup, n, f_numpy)))

            # Mesure des temps d'exécution (100 lancements via temps_exec)
            temps_base.append(temps_exec(lambda: f_base(borne_inf, borne_sup, n)))
            temps_numpy.append(temps_exec(lambda: f_numpy(borne_inf, borne_sup, n)))

        # Calcul du gain de performance pour ce 'n' spécifique
        gains = ["-", "-", "-"]  # Pas de sens pour l'erreur
        for i in range(3):
            gain_calculé = temps_base[i] / temps_numpy[i]
            gains.append(f"{gain_calculé:.1f}x")

        # Formatage des données
        erreurs_base_formatees = [f"{x:.10f}" for x in erreurs_base]
        erreurs_numpy_formatees = [f"{x:.10f}" for x in erreurs_numpy]
        temps_base_formates = [f"{x:.4f}" for x in temps_base]
        temps_numpy_formates = [f"{x:.4f}" for x in temps_numpy]

        # Ajout des données au dictionnaire des colonnes avec un tuple (n, Implémentation)
        colonnes_dataframe[(f"n = {n}", "Python de base")] = erreurs_base_formatees + temps_base_formates
        colonnes_dataframe[(f"n = {n}", "NumPy")] = erreurs_numpy_formatees + temps_numpy_formates
        colonnes_dataframe[(f"n = {n}", "Gain")] = gains

    index_colonnes = pd.MultiIndex.from_tuples(colonnes_dataframe.keys(), names=["Segments", "Version"])

    # Génération du DataFrame final
    df_comparatif = pd.DataFrame(colonnes_dataframe, index=index_lignes, columns=index_colonnes)

    # Configuration de l'affichage de la console
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    print(
        f"\n========================================================================================================================")
    print(f"                                   TABLEAU COMPARATIF MULTI-ÉCHELLES DE SEGMENTS (n)")
    print(
        f"========================================================================================================================\n")
    print(df_comparatif)
    print(
        f"\n========================================================================================================================")