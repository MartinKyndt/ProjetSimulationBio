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
def inversion(gene_pos, dom_pos, sens, pos1, pos2) :
	new_pos_gene = []
	new_pos_dom = []
	new_sens = sens
	#Verify that the genes are not cut in half
	for i in range(len(gene_pos)):
		if pos1 >= gene_pos[i,0] and pos1 <= gene_pos[i,0] or pos2 >= gene_pos[i,0] and pos2 <= gene_pos[i,0]:
			print("impossible to cut the gene")
			break
	#Change positions of domains
	for i in range(len(dom_pos)) :
		for j in range (len(dom_pos[i])) :
			if dom_pos[i][j] > pos1 and dom_pos[i][j] < pos2 :
				new_pos_dom.append(pos1 + pos2 - dom_pos[i][j])
				print('previous dom_pos : ' + str(dom_pos[i][j]) + ' ; New dom_pos : ' + str(pos1 + pos2 - dom_pos[i][j]) + '\n')
			else :
				new_pos_dom.append(dom_pos[i][j])
				print('same dom_pos : ' + str(dom_pos[i][j])  + '\n')
	#Change positions of genes
	affected_genes = []
	for i in range(len(gene_pos)) :
		for j in range (len(gene_pos[i])) :
			if gene_pos[i][j] > pos1 and gene_pos[i][j] < pos2 :
				new_pos_gene.append(pos1 + pos2 - gene_pos[i][j])
				affected_genes.append(i)
			else :
				new_pos_gene.append(gene_pos[i][j])
	affected_genes = np.unique(np.array(affected_genes)
	#Change orientation of genes
	to_invert = []
	for i in affected_genes :
		to_invert.append(sens[i])
	inverted = np.flip(np.array(to_invert))
	for i in range(len(inverted)) :
		new_sens[i] = inverted[i]
		
	new_pos_dom = np.sort(np.array(new_pos_dom)).reshape(len(dom_pos), 2)
	new_pos_gene = np.sort(np.array(new_pos_gene)).reshape(len(gene_pos), 2)
	
	return (new_pos_gene, new_pos_dom, new_sens)
						


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

gene_pos, dom_pos = inversion(gene_pos, dom_pos, 4300, 12500)

print(gene_pos, '\n\n', dom_pos)
print()


#print(randomPos(data))

