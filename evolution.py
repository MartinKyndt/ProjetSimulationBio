# -*- coding: utf-8 -*-
import numpy as np
import random
import shutil

print('Ceci est notre code') 


#Ecrit les données TSS et TTS dans l'ordre : 
#debut de domaine, debut de gene, fin de gene, fin de domaine
def loadData(TSS, TTS) : 
	gene_pos = []
	dom_pos = []
	sens = []
	f1 = open(TSS)
	f2 = open(TTS)
	tss = [[e for e in l[:-1].split('\t')] for l in f1.readlines()[1:]]
	tts = [[e for e in l[:-1].split('\t')] for l in f2.readlines()[1:]]
	for i in range(10) :
		dom_pos.append([(3000*i)+1, 3000*(i+1)])
		gene_pos.append([int(tss[i][2]),int(tts[i][2])])
		sens.append(tss[i][1])
	return (np.array(gene_pos), np.array(dom_pos), np.array(sens))

def writeData_init(TSS, TTS) :
	f1 = open('tousgenesidentiques/TSSevol_prev.dat', 'w')
	f2 = open('tousgenesidentiques/TTSevol_prev.dat', 'w')
	f3 = open('tousgenesidentiques/TSSevol.dat', 'w')
	f4 = open('tousgenesidentiques/TTSevol.dat', 'w')
	f1.close()
	f2.close()
	f3.close()
	f4.close()
	shutil.copy(TSS,'tousgenesidentiques/TSSevol_prev.dat')
	shutil.copy(TTS,'tousgenesidentiques/TTSevol_prev.dat')
	shutil.copy(TSS,'tousgenesidentiques/TSSevol.dat')
	shutil.copy(TTS,'tousgenesidentiques/TTSevol.dat')
	
def writeData(gene_pos, sens) :
	f1 = open('tousgenesidentiques/TSSevol.dat', 'w')
	f2 = open('tousgenesidentiques/TTSevol.dat', 'w')
	f1.write('TUindex\tTUorient\tTTS_pos\tTTS_sstrength\n')
	f2.write('TUindex\tTUorient\tTTS_pos\tTTS_proba_off\n')
	for i in range(len(gene_pos)):
		f1.write(str(i)+'\t')
		f2.write(str(i)+'\t')
		f1.write(sens[i]+'\t')
		f2.write(sens[i]+'\t')
		f1.write(str(gene_pos[i,0])+'\t.2\n')
		f2.write(str(gene_pos[i,1])+'\t1.\n')
	f1.close()
	f2.close()
	
#gene_pos, dom_poss, sens = loadData('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat')
writeData_init('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat')

#Ajoute un codon à une position définie dans le génome
#Décale toutes les positions suivantes
def insertion(gene_pos, dom_pos, pos) :
	for i in range(len(gene_pos)) :
		for j in range(len(gene_pos[i])) :
			if gene_pos[i,j] >= pos :
				gene_pos[i,j] += 1
	for i in range(len(dom_pos)) :
		for j in range(len(dom_pos[i])) :
			if dom_pos[i,j] >= pos :
				dom_pos[i,j] += 1

#Méthode deletion, delete une position aléatoire pos
#Décale toutes les positions suivantes
def deletion(gene_pos, dom_pos, pos) : 
	for i in range(len(gene_pos)) :
		for j in range(len(gene_pos[i])) :
			if gene_pos[i][j] >= pos :
				gene_pos[i][j] -= 1
	for i in range(len(dom_pos)) :
		for j in range(len(dom_pos[i])) :
			if dom_pos[i][j] >= pos :
				dom_pos[i][j] -= 1

 #pos1 < pos2
 #Les positions ne se trouvent pas dans les régions codantes
def inversion(gene_pos, dom_pos, pos1, pos2) :
	new_pos_gene = []
	new_pos_dom = []
	for i in range(len(dom_pos)) :
		for j in range (len(dom_pos[i])) :
			if dom_pos[i][j] > pos1 and dom_pos[i][j] < pos2 :
				new_pos_dom.append(pos1 + pos2 - data[i][j])
			else :
				new_pos_dom.append(data[i][j])
					
	for i in range(len(gene_pos)) :
		for j in range (len(gene_pos[i])) :
			if gene_pos[i][j] > pos1 and gene_pos[i][j] < pos2 :
				new_pos_dom.append(pos1 + pos2 - data[i][j])
			else :
				new_pos_dom.append(data[i][j])				
	new_pos_dom = np.sort(np.array(new_pos_dom)).reshape(2, len(pos_dom))
	new_pos_gene = np.sort(np.array(new_pos_gene)).reshape(2, len(pos_dom))
	
	return (new_pos_gene, new_pos_dom)
						
<<<<<<< HEAD
=======


#print(inversion(data, 9500, 19000))


def deletion(gene_pos, dom_pos, pos) : 
	for i in range(len(gene_pos)) :
		for j in range(len(gene_pos[i])) :
			if gene_pos[i,j] >= pos :
				gene_pos[i,j] -= 1
	for i in range(len(dom_pos)) :
		for j in range(len(dom_pos[i])) :
			if dom_pos[i,j] >= pos :
				dom_pos[i,j] -= 1

>>>>>>> abca614e5ff9767a1419b324ee797d83151646ea
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


#print(randomPos(data))

