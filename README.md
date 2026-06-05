# Projet B - Groupe 4 : Intégration Numérique

Ce projet a pour objectif de concevoir et de comparer différentes méthodes d'intégration numérique pour le calcul de l'intégrale d'une fonction polynomiale.  L'étude cherche également à comparer différentes méthodes de programmation sous Python (python de base, Numpy et Scipy).

## Fonctionnalités et Méthodes Implémentées

Le projet implémente trois méthodes géométriques d'approximation d'intégrales :
* **Méthode des Rectangles** (évaluée au point gauche)
* **Méthode des Trapèzes**
* **Méthode de Simpson**

Chaque méthode est déclinée sous trois approches de codage afin d'analyser les gains d'optimisation :
1.  **Python de base :** Implémentation algorithmique classique à l'aide de boucles itératives (`for`).
2.  **NumPy (Vectorisé) :** Optimisation des performances grâce à la vectorisation des tableaux de calculs.
3.  **SciPy :** Validation des résultats à l'aide des modules de référence pré-programmés (`integrate.trapezoid`, `integrate.simpson`).

## Visualisation et Analyse

Le script principal génère trois analyses graphiques :

1.  **Graphique de convergence :** Une figure à 3 sous-graphes (un par méthode) comparant l'évolution de la valeur calculée par rapport à la solution analytique exacte, en faisant varier le nombre de segments $n$ permettant d'observer la convergence de nos fonctions.
2.  **Graphique d'erreur absolue (Échelle Log-Log) :** Une étude en échelle double-logarithmique de l'erreur absolue en fonction du nombre de segments $n$.
3.  **Graphique de temps d'exécution (Echelle Logarithmique)**: Une étude du temps d'exécution en fonction du nombre de segments $n$ en 2 sosu-graphes (méthode des trapèzes et de Simpson)

## Installation et Prérequis

Assurez-vous de disposer d'un environnement Python 3.14 fonctionnel ainsi que des bibliothèques scientifiques nécessaires:
```bash
pip install numpy matplotlib scipy pandas
```
## Configuration
Paramètres définis par défaut dans le script principal:
- coefficients de la fonction polynomiale $p_1$, $p_2$, $p_3$, $p_4$ fixés à 1 
- intervalle de l'intégrale $[a,b]=[0,100]$
- nombre de segments n variant entre 20 et 1000 par pas de 20  

Ces paramètres peuvent être modifiés par l'utilisateur dans le script principal.

## Guide d'utilisation

Pour lancer le programme, il suffit d'exécuter le script principal `main.py`. L'ensemble du processus est entièrement automatisé : le script configure les paramètres, effectue les calculs d'intégration pour toutes les méthodes (Python, NumPy, SciPy) et génère automatiquement l'ensemble des graphiques comparatifs de convergence et d'erreur absolue.

Exécutez simplement la commande suivante dans votre terminal :

```bash
python main.py 


