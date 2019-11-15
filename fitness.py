import numpy as np
import math
from random import *

def fitness(result, expected) : 
	obs = [] 
	cible = [] 
	f1 = open(result)
	f2 = open(expected)
	t = [[e for e in l[:-1].split()] for l in f1.readlines()[0:]]
	tt = [[e for e in l[:-1].split()] for l in f2.readlines()[0:]] 
	for i in range(10) :
		obs.append(int(t[i][4]))
		cible.append(int(tt[i][4]))
	
	fitness = 0 
	for i in range(10) : 
		fitness += math.log(obs[i]/cible[i])
	
	return(fitness)
	

print(fitness("result.dat","cible.dat")) 


#def iter(seuils) : 
#	prob = random() 
	
#	if(prob < seuil[0]) #insertion
#	elif(prob < seuil[1]) #délétion 
#	else #invertion 
	
#	#writeData 
	
def checkFitness(event) :
	newfitness = fitness("result.dat","cible.dat")
	f = open("fitness.dat", 'r') 
	t = [[e for e in l[:-1].split(':')] for l in f.readlines()[0:]] 
	f = open("fitness.dat", 'a') 
	if(newfitness > float(t[len(t)-1][1])) : 
		f.write(event + '\t') 

		
	
checkFitness('Test')
