#--------------Programmation Python du PMI-------------

import matplotlib.pyplot as plt
import numpy as np
import time
import random as rd
import initialisation #programme py annexe pour générer 
                      #des images contenant des pattern aléatoires 
                      #suivant une distribution gaussienne 

#------------------------------------------------------

N = 256
feed=0.03
kill=0.062
Du=2
Dv=1
dx=1
dt=1
nb_iter=200
frame = 100
U,V = initialisation.init_mat(10,20,N)

#------------------------------------------------------

def Laplacien(M):
	L = -1*M
	L += 0.2*np.roll(M, (0,-1), (0,1)) # voisin de droite
	L += 0.2*np.roll(M, (0,+1), (0,1)) # voisin de gauche
	L += 0.2*np.roll(M, (-1,0), (0,1)) # voisin du dessus
	L += 0.2*np.roll(M, (+1,0), (0,1)) # voisin du bas
	L += 0.05*np.roll(M, (-1,-1), (0,1)) #voisin diagonale droite bas
	L += 0.05*np.roll(M, (+1,-1), (0,1)) #voisin diagonale droite haut
	L += 0.05*np.roll(M, (+1,+1), (0,1))#voisin diagonale gauche haut
	L += 0.05*np.roll(M, (-1,+1), (0,1)) #voisin diagonale gauche bas
	
	return L/(dx*dx)

#------------------------------------------------------

def update_etat(A, B, DA, DB, f, k, dt):
	
	LA = Laplacien(A)
	LB = Laplacien(B)
	
	diff_A = (DA*LA - A*B**2 + f*(1-A)) * dt
	diff_B = (DB*LB + A*B**2 - (k+f)*B) * dt
	
	A += diff_A
	B += diff_B

#------------------------------------------------------

def main(feed,kill,Du,Dv):

	plt.ion()
	plt.figure()
	
	for k in range(nb_iter):
		update_etat(A,B,Du,Dv,feed,kill,dt)
		if k % frame== 0:
			# filename = "Uframe_{:02d}.png".format(k//frame) 
			# print(filename)
			plt.imshow(U, cmap="jet")
			print(k)
			# plt.savefig(filename)
			plt.pause(0.005)

#-------------------------------------------------------

# start = time.time()

main(feed,kill,Du,Dv)

# end = time.time()

# print("Temps d'execution : ",end-start)
# print("Pour une image de taille ",N,"x",N)
# print("Et ",nb_iter," nombre d'itérations")

#-------------------------------------------------------
