import numpy as np
import math


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
	
#print(fitness("result.dat","cible.dat")) 

