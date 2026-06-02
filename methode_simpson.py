#Module de la méthode simpson

from solution_analytique import polynome

def simpson_basique(a, b, n=10):
    pas=(b-a)/n
    u=a #correspond au "a" de la formule dans l'énoncé du devoir
    v=a+pas #correspond au "b" de la formule dans l'énoncé du devoir
    aire=0
    for i in range(n):
        aire+=(v-u)/6*(polynome(u)+4*polynome((u+v)/2)+polynome(v))
        #On avance d'un pas
        u=v
        v+=pas
    return aire
