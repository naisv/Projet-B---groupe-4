#MGA802 - Mini projet B - Groupe 4
#Script principal

import pandas as pd

from solution_analytique import compute_solution_analytique
from performance import compute_erreur, temps_exec
from methode_rectangle import integration_rectangle_base, integration_rectangle_numpy
from methode_trapeze import trap_python, trap_numpy
from methode_simpson import simpson_basique, simpson_numpy

#Définition des variables globales : coefficients de la fonction polynomiale
p1=1
p2=1
p3=1
p4=1

#parametres des integrales
borne_inf = 1
borne_sup = 10
nb_segments = 1000

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


erreurs_base = []
erreurs_numpy = []
temps_base = []
temps_numpy = []

for methode, implémentations in dictionnaire_fonctions.items():
    f_base = implémentations["base"]
    f_numpy = implémentations["numpy"]

    err_b = compute_erreur(borne_inf, borne_sup, nb_segments, f_base)
    err_np = compute_erreur(borne_inf, borne_sup, nb_segments, f_numpy)

    erreurs_base.append(abs(err_b))
    erreurs_numpy.append(abs(err_np))


    t_base = temps_exec(lambda: f_base(borne_inf, borne_sup, nb_segments))
    t_numpy = temps_exec(lambda: f_numpy(borne_inf, borne_sup, nb_segments))

    temps_base.append(t_base)
    temps_numpy.append(t_numpy)


# Combinaison des données (Erreurs puis Temps)
donnees_combinees = {
    "Python de base": erreurs_base + temps_base,
    "NumPy (Vectorisé)": erreurs_numpy + temps_numpy
}

liste_methodes = ["Rectangles", "Trapèzes", "Simpson"]
index_multi = pd.MultiIndex.from_product(
    [["Erreur Absolue", "Temps d'exécution total (s)"], liste_methodes],
    names=["Métrique", "Méthode"]
)

# Génération du DataFrame final
df_analyse = pd.DataFrame(donnees_combinees, index=index_multi)

# Calcul dynamique du facteur d'accélération (Gain)
df_analyse["Gain (x)"] = df_analyse["Python de base"] / df_analyse["NumPy (Vectorisé)"]

# Nettoyage de la colonne Gain pour les lignes d'erreurs
df_analyse.loc["Erreur Absolue", "Gain (x)"] = "-"


print(f"\n=========================================================")
print(f"  ANALYSE COMPARATIVE NUMÉRIQUE (n = {nb_segments} segments)")
print(f"=========================================================\n")
print(df_analyse)
print(f"\n=========================================================")