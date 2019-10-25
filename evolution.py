# -*- coding: utf-8 -*-
import numpy as np
import random

print('Ceci est notre code') 


#Ecrit les données TSS et TTS dans l'ordre : 
#debut de domaine, debut de gene, fin de gene, fin de domaine
def loadData(TSS, TTS) : 
	gene_pos = []
	dom_pos = []
	f1 = open(TSS)
	f2 = open(TTS)
	tss = [[e for e in l[:-1].split('\t')] for l in f1.readlines()[1:]]
	tts = [[e for e in l[:-1].split('\t')] for l in f2.readlines()[1:]]
	for i in range(10) :
		dom_pos.append([(3000*i)+1, 3000*(i+1)])
		gene_pos.append([int(tss[i][2]),int(tts[i][2])])
	return (np.array(gene_pos), np.array(dom_pos))


def writeData(gene_pos) :
	f1 = open('TSSevol.dat', 'w')
	f2 = open('TTSevol.dat', 'w')
	f1.write('TUindex\tTUorient\tTTS_pos\tTTS_sstrength\n')
	f2.write('TUindex\tTUorient\tTTS_pos\tTTS_proba_off\n')
	for i in range(len(gene_pos)):
		f1.write(str(i)+'\t')
		f2.write(str(i)+'\t')
		if gene_pos[i,0]<gene_pos[i,1]:
			f1.write('+\t')
			f2.write('+\t')
		else:
			f1.write('-\t')
			f2.write('-\t')
		f1.write(str(gene_pos[i,0])+'\t.2\n')
		f2.write(str(gene_pos[i,1])+'\t1.\n')
	f1.close()
	f2.close()
	
gene_pos, dom_poss = loadData('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat')
writeData(gene_pos)

#Ajoute un codon à une position définie dans le génome
#Décale toutes les positions suivantes
def insertion(gene_pos, dom_pos, pos) :
	for i in range(len(gene_pos)) :
		for j in range(len(gene_pos[i])) :
			if gene_pos[i][j] >= pos :
				gene_pos[i][j] += 1
	for i in range(len(dom_pos)) :
		for j in range(len(dom_pos[i])) :
			if dom_pos[i][j] >= pos :
				dom_pos[i][j] += 1

 
 #pos1 < pos2
 #Les positions ne se trouvent pas dans les régions codantes

def inversion(data, pos1, pos2) :
	data_copy = data
	new_pos_gene = []
	new_pos_dom = []
	for i in range(len(data)) :
		for j in range (len(data[i])) :
			if data[i][j] > pos1 and data[i][j] < pos2 :
					if j = 0 or j = 3 : #La position concernée est une barrière de domaine
						new_pos_dom.append(pos1 + pos2 - data[i][j])
						
					elif j = 1 or j = 2 : #La position concernée est une barrière de gène
						new_pos_gene.append(pos1 + pos2 - data[i][j])		


#print(inversion(data, 9500, 19000))


def deletion(gene_pos, dom_pos, pos) : 
	for i in range(len(gene_pos)) :
		for j in range(len(gene_pos[i])) :
			if gene_pos[i][j] >= pos :
				gene_pos[i][j] -= 1
	for i in range(len(dom_pos)) :
		for j in range(len(dom_pos[i])) :
			if dom_pos[i][j] >= pos :
				dom_pos[i][j] -= 1

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

gene_pos, dom_pos = loadData('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat') 

print(gene_pos, dom_pos)
print()

#print(randomPos(data))

