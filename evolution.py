import numpy as np
import random

print('Ceci est notre code') 


#Ecrit les données TSS et TTS dans l'ordre : 
#debut de domaine, debut de gene, fin de gene, fin de domaine
def loadData(TSS, TTS) : 
	data = [] 
	f1 = open(TSS)
	f2 = open(TTS)
	tss = [[e for e in l[:-1].split('\t')] for l in f1.readlines()[1:]]
	tts = [[e for e in l[:-1].split('\t')] for l in f2.readlines()[1:]]
	for i in range(10) :
		data.append([(3000*i)+1, int(tss[i][2]),int(tts[i][2]), 3000*(i+1)]) 
	return np.array(data)
		data.append([int(tss[i][2]),int(tts[i][2]), (3000*i)+1, 3000*(i+1)]) 
	return data

	

#def writeData(TSS, TTS) 

#Ajoute un codon à une position définie dans le génome
#Décale toutes les positions suivantes
def insertion(data, pos) :
	for i in range(len(data)) :
		for j in range(len(data[0])) :
			if data[i][j] >= pos :
				data[i][j] += 1
"""
 #pos1 < pos2
def inversion(data, pos1, pos2) :
	for i in range(len(data)) :
		if pos1 > data[i][0] and pos1 < data[i][3] #La coupure se fait dans le domaine
			
			if flat_data[i*4+j] > pos1 and flat_data[i*4+j] <= pos2 :
				#new_pos = pos2 - (flat_data[i]-pos1)
				flat_data[i] = new_pos
	tab_data = flat_data.reshape(len(data), len(data[0]))
	return tab_data
 """

data = loadData('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat')
print(data)
print()
insertion(data, 3500)
print(data)
print()


#print(inversion(data, 9500, 19000))


def deletion(data, pos) : 
	for i in range(len(data)) : 
		for j in range(len(data[0])) : 
			if(data[i][j] > pos) : 
				data[i][j] = data[i][j]-1 
	
def randomPos(data) : 
	deb = 1 
	fin = data[9][3]
	count = 0
	while(count != 10) : 
		count = 0
		pos = random.randint(deb,fin)
		for i in range(len(data)): 
			if(pos < data[i][0] & pos > data[i][1]) : 
				count +=1 
	return pos

dat = loadData('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat') 
print(dat)
deletion(dat, 3) 
print(dat) 
print(randomPos(dat))

