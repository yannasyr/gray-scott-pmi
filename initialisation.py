#---------Patterns aléatoires----------------

import matplotlib.pyplot as plt
import numpy as np
import random as rd

#---------------------------------------------------

def gaussienne(x,x0,y,y0,sigmaX,sigmaY):
    
    e1 = (x-x0)**2 / (2 * sigmaX * sigmaX)
    e2 = (y-y0)**2 / (2 * sigmaY * sigmaY)

    return (np.exp(-e1 -  e2))

#---------------------------------------------------

def init_mat(nb_pattern,taille_tache,N):
    U = np.ones((N,N))
    V = np.zeros((N,N))
    for k in range(nb_pattern):
        i = rd.randrange(taille_tache+1,N-taille_tache-1)
        j = rd.randrange(taille_tache+1,N-taille_tache-1)
        for a in range(taille_tache):
            V[ i, j - a ] = gaussienne( i , i , j-a , j,7,7)    #voisin gauche
            V[ i, j + a ] = gaussienne( i , i , j+a , j,7,7) #voisin droit
            V[ i + a, j ] = gaussienne( i+a , i , j , j,7,7)    #voisin bas
            V[ i - a, j ] = gaussienne( i-a , i , j , j,7,7)     #voisin haut
            V[ i - a, j - a] = gaussienne( i-a , i , j-a , j,7,7) #voisin haut gauche
            V[ i - a, j + a] = gaussienne( i-a , i , j+a , j,7,7) #voisin haut droite
            V[ i + a, j - a] = gaussienne( i+a , i , j-a , j,7,7)#voisin bas hauche
            V[ i + a, j + a] = gaussienne( i+a , i , j+a , j,7,7)  #voisin bas droite

            U[ i, j - a ] = (1 - V[ i, j - a ])*0.8
            U[ i, j + a ] = (1 - V[ i, j + a ])*0.8
            U[ i + a, j ] = (1 - V[ i + a, j ])*0.8
            U[ i - a, j ] = (1 - V[ i - a, j ])*0.8
            U[ i - a, j - a] = (1 - V[ i - a, j - a])*0.8
            U[ i - a, j + a] = (1 - V[ i - a, j + a])*0.8
            U[ i + a, j - a] = (1 - V[ i + a, j - a])*0.8
            U[ i + a, j + a] = (1 - V[ i + a, j + a])*0.8
            
    return U,V






