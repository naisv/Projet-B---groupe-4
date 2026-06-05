# MGA802 - Mini projet B - Groupe 4
# Script principal

# Définition des variables globales : coefficients de la fonction polynomiale
p1 = 1
p2 = 1
p3 = 1
p4 = 0

from time import perf_counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

from solution_analytique import compute_solution_analytique, polynome
from performance import compute_erreur, temps_exec, convergence
from methode_rectangle import integration_rectangle_base, integration_rectangle_numpy
from methode_trapeze import trap_python, trap_numpy
from methode_simpson import simpson_basique, simpson_numpy

if __name__ == "__main__":
    # Paramètres des intégrales
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

    liste_methodes = ["Rectangles", "Trapèzes", "Simpson"]

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

            erreurs_base.append(abs(compute_erreur(borne_inf, borne_sup, n, f_base)))
            erreurs_numpy.append(abs(compute_erreur(borne_inf, borne_sup, n, f_numpy)))

            temps_base.append(temps_exec(lambda: f_base(borne_inf, borne_sup, n)))
            temps_numpy.append(temps_exec(lambda: f_numpy(borne_inf, borne_sup, n)))

        gains = ["-", "-", "-"]
        for i in range(3):
            gain_calculé = temps_base[i] / temps_numpy[i]
            gains.append(f"{gain_calculé:.1f}x")

        erreurs_base_formatees = [f"{x:.10f}" for x in erreurs_base]
        erreurs_numpy_formatees = [f"{x:.10f}" for x in erreurs_numpy]
        temps_base_formates = [f"{x:.4f}" for x in temps_base]
        temps_numpy_formates = [f"{x:.4f}" for x in temps_numpy]

        colonnes_dataframe[(f"n = {n}", "Python de base")] = erreurs_base_formatees + temps_base_formates
        colonnes_dataframe[(f"n = {n}", "NumPy")] = erreurs_numpy_formatees + temps_numpy_formates
        colonnes_dataframe[(f"n = {n}", "Gain")] = gains

    index_colonnes = pd.MultiIndex.from_tuples(colonnes_dataframe.keys(), names=["Segments", "Version"])
    df_comparatif = pd.DataFrame(colonnes_dataframe, index=index_lignes, columns=index_colonnes)

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

    # Section Graphiques

    a = 0
    b = 100

    # Récupération des données d'intégration pour les tracés de convergence
    solution_exacte = compute_solution_analytique(a, b)
    nombre_segments, cv_rectangle_python = convergence(integration_rectangle_base, a, b)
    _, cv_rectangle_numpy = convergence(integration_rectangle_numpy, a, b)
    _, cv_trapeze_python = convergence(trap_python, a, b)
    _, cv_trapeze_numpy = convergence(trap_numpy, a, b)
    _, cv_simpson_python = convergence(simpson_basique, a, b)
    _, cv_simpson_numpy = convergence(simpson_numpy, a, b)

    # GRAPHIQUE 1 : Convergence des méthodes
    plt.figure(figsize=(12, 7))
    plt.axhline(y=solution_exacte, color='black', linestyle=':', label="Valeur exacte théorique")
    plt.plot(nombre_segments, cv_rectangle_python, label="Rectangle (Python)", color="blue", linestyle="-")
    plt.plot(nombre_segments, cv_rectangle_numpy, label="Rectangle (NumPy)", color="cyan", linestyle="--")
    plt.plot(nombre_segments, cv_trapeze_python, label="Trapèze (Python)", color="green", linestyle="-")
    plt.plot(nombre_segments, cv_trapeze_numpy, label="Trapèze (NumPy)", color="lime", linestyle="--")
    plt.plot(nombre_segments, cv_simpson_python, label="Simpson (Python)", color="red", linestyle="-")
    plt.plot(nombre_segments, cv_simpson_numpy, label="Simpson (NumPy)", color="orange", linestyle="--")

    plt.xlabel("Nombre de segments ($n$)", fontsize=11)
    plt.ylabel("Valeur de l'intégrale calculée", fontsize=11)
    plt.title(f"Comparaison de la convergence des méthodes\nFonction étudiée : f(x) = {p1} + {p2}x + {p3}x² + {p4}x³ Intervalle [{a}, {b}]",
              fontsize=13, fontweight='bold', pad=15)
    plt.grid(True, which='both', linestyle=':', alpha=0.7)
    plt.legend(loc="best", fontsize=10)
    plt.show()

    # GRAPHIQUE 2 : Validation avec SciPy
    # liste vectorisée
    grilles_calcul = [a + np.arange(n + 1) * ((b - a) / n) for n in nombre_segments]
    valeurs_y = [p1 + p2 * x + p3 * (x ** 2) + p4 * (x ** 3) for x in grilles_calcul]

    cv_trapeze_scipy = list(map(integrate.trapezoid, valeurs_y, grilles_calcul))
    cv_simpson_scipy = list(map(integrate.simpson, valeurs_y, grilles_calcul))

    plt.figure(figsize=(12, 7))
    plt.axhline(y=solution_exacte, color='black', linestyle=':', label="Valeur exacte théorique")
    plt.plot(nombre_segments, cv_trapeze_numpy, label="Trapèze (NumPy)", color="lime", linestyle="-")
    plt.plot(nombre_segments, cv_trapeze_scipy, label="Trapèze (SciPy)", color="darkgreen", linestyle="--")
    plt.plot(nombre_segments, cv_simpson_numpy, label="Simpson (NumPy)", color="orange", linestyle="-")
    plt.plot(nombre_segments, cv_simpson_scipy, label="Simpson (SciPy)", color="darkred", linestyle="--")

    plt.xlabel("Nombre de segments ($n$)", fontsize=11)
    plt.ylabel("Valeur de l'intégrale calculée", fontsize=11)
    plt.title(f"Vérification de la convergence des méthodes pré-programmées (SciPy)\nFonction étudiée : f(x) = {p1} + {p2}x + {p3}x² + {p4}x³ Intervalle [{a}, {b}]",
              fontsize=13, fontweight='bold', pad=15)
    plt.grid(True, which='both', linestyle=':', alpha=0.7)
    plt.legend(loc="best", fontsize=10)
    plt.show()

    # GRAPHIQUE 3 : Sous-graphiques des performances temporelles
    temps_trap_base, temps_trap_np, temps_trap_scipy = [], [], []
    temps_simp_base, temps_simp_np, temps_simp_scipy = [], [], []

    for n in nombre_segments:
        h_cv = (b - a) / n
        x_cv = a + np.arange(n + 1) * h_cv
        y_cv = p1 + p2 * x_cv + p3 * (x_cv ** 2) + p4 * (x_cv ** 3)

        temps_trap_base.append(temps_exec(lambda: trap_python(a, b, n)))
        temps_trap_np.append(temps_exec(lambda: trap_numpy(a, b, n)))
        temps_trap_scipy.append(temps_exec(lambda: integrate.trapezoid(y_cv, x_cv)))

        temps_simp_base.append(temps_exec(lambda: simpson_basique(a, b, n)))
        temps_simp_np.append(temps_exec(lambda: simpson_numpy(a, b, n)))
        temps_simp_scipy.append(temps_exec(lambda: integrate.simpson(y_cv, x_cv)))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

    ax1.plot(nombre_segments, temps_trap_base, label="Trapèze (Python de base)", color="red", linestyle="-", marker="o")
    ax1.plot(nombre_segments, temps_trap_np, label="Trapèze (NumPy)", color="lime", linestyle="-", marker="s")
    ax1.plot(nombre_segments, temps_trap_scipy, label="Trapèze (SciPy)", color="darkgreen", linestyle="--", marker="^")
    ax1.set_yscale('log')
    ax1.set_xlabel("Nombre de segments ($n$)", fontsize=11)
    ax1.set_ylabel("Temps d'exécution total pour 100 lancements (s)", fontsize=11)
    ax1.set_title("Méthode des Trapèzes", fontsize=12, fontweight='bold')
    ax1.grid(True, which='both', linestyle=':', alpha=0.7)
    ax1.legend(loc="best", fontsize=10)

    ax2.plot(nombre_segments, temps_simp_base, label="Simpson (Python de base)", color="red", linestyle="-", marker="o")
    ax2.plot(nombre_segments, temps_simp_np, label="Simpson (NumPy)", color="orange", linestyle="-", marker="s")
    ax2.plot(nombre_segments, temps_simp_scipy, label="Simpson (SciPy)", color="darkred", linestyle="--", marker="^")
    ax2.set_yscale('log')
    ax2.set_xlabel("Nombre de segments ($n$)", fontsize=11)
    ax2.set_ylabel("Temps d'exécution total pour 100 lancements (s)", fontsize=11)
    ax2.set_title("Méthode de Simpson", fontsize=12, fontweight='bold')
    ax2.grid(True, which='both', linestyle=':', alpha=0.7)
    ax2.legend(loc="best", fontsize=10)

    plt.suptitle(
        f"Analyse Comparative des Performances Temporelles (Échelle Logarithmique)\nPython de base vs NumPy vs SciPy \n Fonction étudiée : f(x) = {p1} + {p2}x + {p3}x² + {p4}x³ Intervalle [{a}, {b}]",
        fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.show()

    # GRAPHIQUE 4 : Comparaison des erreurs pour les 3 méthodes (rectangle, trapèzes, simpson)
    # Listes pour stocker les erreurs d'une seule implémentation (NumPy) par méthode
    err_rect = []
    err_trap = []
    err_simp = []

    # --- Calcul des erreurs ---
    for n in nombre_segments:
        # 1. Calcul des erreurs (en s'assurant d'avoir la valeur absolue)
        e_rect = abs(compute_erreur(a, b, n, integration_rectangle_numpy))
        e_trap = abs(compute_erreur(a, b, n, trap_numpy))
        e_simp = abs(compute_erreur(a, b, n, simpson_numpy))

        # 2. Protection contre le zéro absolu pour l'échelle log-log
        # Si la méthode (comme Simpson) trouve l'aire exacte, l'erreur est 0.0
        err_rect.append(e_rect if e_rect > 0 else 1e-16)
        err_trap.append(e_trap if e_trap > 0 else 1e-16)
        err_simp.append(e_simp if e_simp > 0 else 1e-16)

    # --- Création de la figure (Un seul grand graphique) ---
    fig, ax = plt.subplots(figsize=(12, 8))

    # Tracé des 3 méthodes mathématiques
    ax.plot(nombre_segments, err_rect, label="Rectangles", color="deepskyblue", linestyle="-", marker="s",
            linewidth=2)
    ax.plot(nombre_segments, err_trap, label="Trapèzes", color="lime", linestyle="-", marker="^", linewidth=2)
    ax.plot(nombre_segments, err_simp, label="Simpson", color="magenta", linestyle="-", marker="o", linewidth=2)

    # Paramétrage des axes en Log-Log
    ax.set_xscale('log')
    ax.set_yscale('log')

    # Habillage du graphique
    ax.set_xlabel("Nombre de segments ($n$)", fontsize=12)
    ax.set_ylabel("Erreur absolue", fontsize=12)
    ax.set_title(f"Comparaison de l'erreur absolue des méthodes d'intégration numérique (Numpy)\nFonction étudiée : f(x) = {p1} + {p2}x + {p3}x² + {p4}x³ Intervalle [{a}, {b}]", fontsize=14, fontweight='bold')
    ax.grid(True, which='both', linestyle=':', alpha=0.7)

    # Ajout d'une légende claire
    ax.legend(loc="upper right", fontsize=11, title="Méthodes (Implémentation NumPy)", title_fontsize=12)

    plt.tight_layout()
    plt.show()