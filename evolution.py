# -*- coding: utf-8 -*-
import numpy as np
import random
import shutil
import sys

print('Ceci est notre code') 

####################################
#ECRITURE ET LA LECTURE DE FICHIERS#
####################################

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
	shutil.copy(TSS,'tousgenesidentiques/TSSevol.dat')
	shutil.copy(TTS,'tousgenesidentiques/TTSevol.dat')
	
def writeData(gene_pos, sens, inversion=False) :
		shutil.copy('tousgenesidentiques/TSSevol.dat', 'tousgenesidentiques/TSSevol_prev.dat')
		shutil.copy('tousgenesidentiques/TTSevol.dat', 'tousgenesidentiques/TTSevol_prev.dat')
		f1 = open('tousgenesidentiques/TSSevol.dat', 'w')
		f2 = open('tousgenesidentiques/TTSevol.dat', 'w')
		f1.write('TUindex\tTUorient\tTTS_pos\tTTS_sstrength\n')
		f2.write('TUindex\tTUorient\tTTS_pos\tTTS_proba_off\n')
		for i in range(len(gene_pos)):
			f1.write(str(i)+'\t')
			f2.write(str(i)+'\t')
			f1.write(sens[i]+'\t')
			f2.write(sens[i]+'\t')
			f1.write(str(gene_pos[i,0]+4)+'\t.2\n')
			f2.write(str(gene_pos[i,1]+4)+'\t1.\n')
		f1.close()
		f2.close()
		
def writeData_inversion():
	shutil.copy('tousgenesidentiques/TSSevol_prev.dat', 'tousgenesidentiques/TSSevol.dat')
	shutil.copy('tousgenesidentiques/TTSevol_prev.dat', 'tousgenesidentiques/TTSevol.dat')
	

#writeData_init('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat')	
#gene_pos, dom_poss, sens = loadData('tousgenesidentiques/TSSevol.dat', 'tousgenesidentiques/TTSevol.dat')
#writeData(gene_pos, sens)
#writeData_inversion()


#########################
#EVENEMENTS DE MUTATIONS#
#########################


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
def deletion(gene_pos, dom_pos) : 
	pos = randomPos(gene_pos, dom_pos)
	for i in range(len(gene_pos)) :
		for j in range(len(gene_pos[i])) :
			if gene_pos[i][j] >= pos :
				gene_pos[i][j] -= 1
	for i in range(len(dom_pos)) :
		for j in range(len(dom_pos[i])) :
			if dom_pos[i][j] >= pos :
				dom_pos[i][j] -= 1

			
			
			
 #pos1 < pos2
def inversion(gene_pos, dom_pos, sens) :
	pos1 = randomPos(dom_pos, gene_pos)
	pos2 = randomPos(dom_pos, gene_pos)
	pos11 = min(pos1, pos2)
	pos22 = max(pos1, pos2)
	pos1 = pos11
	pos2 = pos22
	new_pos_gene = []
	new_pos_dom = []
	new_sens = sens
	#Verify that the genes are not cut in half
	for i in range(len(gene_pos)):
		"""print('i : ', i)
		#print('gene position : ', gene_pos[i,0],gene_pos[i,1])
		#print('positions of mutations : ', pos1, pos2, '\n')"""
		if pos1 >= gene_pos[i,0] and pos1 <= gene_pos[i,1] or pos2 >= gene_pos[i,0] and pos2 <= gene_pos[i,1]:
			sys.exit('impossible to cut the gene')
	#Change positions of domains
	for i in range(len(dom_pos)) :
		for j in range (len(dom_pos[i])) :
			if dom_pos[i][j] > pos1 and dom_pos[i][j] < pos2 :
				new_pos_dom.append(pos1 + pos2 - dom_pos[i][j])
				"""print('previous dom_pos : ' + str(dom_pos[i][j]) + ' ; New dom_pos : ' + str(pos1 + pos2 - dom_pos[i][j]) + '\n')"""
			else :
				new_pos_dom.append(dom_pos[i][j])
				"""print('same dom_pos : ' + str(dom_pos[i][j])  + '\n')"""
	#Change positions of genes
	affected_genes = []
	for i in range(len(gene_pos)) :
		for j in range (len(gene_pos[i])) :
			if gene_pos[i][j] > pos1 and gene_pos[i][j] < pos2 :
				new_pos_gene.append(pos1 + pos2 - gene_pos[i][j])
				affected_genes.append(i)
				"""print('previous gene_pos : ' + str(gene_pos[i][j]) + ' ; New gene_pos : ' + str(pos1 + pos2 - gene_pos[i][j]) + '\n')"""
			else :
				new_pos_gene.append(gene_pos[i][j])
				"""print('same gene_pos : ' + str(gene_pos[i][j])  + '\n')"""
	#Change orientation of genes
	affected_genes = np.unique(np.array(affected_genes))
	print('\n', affected_genes)
	to_invert = []
	for i in affected_genes :
		to_invert.append(sens[i])
	inverted = np.flip(np.array(to_invert))
	print(inverted)
	for i in range(len(inverted)) :
		if inverted[i] == "+" :
			inverted[i] = "-"
		else :
			inverted[i] = "+"
	print(inverted)
	for i in (affected_genes) :
		new_sens[i] = inverted[i-affected_genes[0]]
		
	new_pos_dom = np.sort(np.array(new_pos_dom)).reshape(len(dom_pos), 2)
	new_pos_gene = np.sort(np.array(new_pos_gene)).reshape(len(gene_pos), 2)
	
	return (new_pos_gene, new_pos_dom, new_sens)

##############################################
#CHOIX D'UNE POSITION ALEATOIRE POUR MUTATION#
##############################################

#Les positions ne se trouvent pas dans les régions codantes
def randomPos(dom_pos, gene_pos) : 
	deb = dom_pos[0,0]
	fin = dom_pos[-1,0]
	count = 0
	cond = False
	while(not cond) : 
		pos = random.randint(deb,fin)
		for i in range(len(gene_pos)):
			if i == 0 :
				if(pos < gene_pos[i,0]) :
					cond = True
			if(pos > gene_pos[i-1][1] and pos < gene_pos[i][0]) : 
				cond = True
	print("position for inversion", pos)
	return pos
	
	
#########
#FITNESS#
#########


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
	
	
################
#TESTS METHODES#
################

def main(argv) 
#bimbimbibm 

if __name__ == "__main__" : 
#boumboumboum 
	main(sys.argv[1]) 

writeData_init('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat')
gene_pos, dom_pos, sens = loadData('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat')

print(gene_pos, '\n\n', dom_pos, '\n\n', sens)

gene_pos, dom_pos, sens = inversion(gene_pos, dom_pos, sens)

print(gene_pos, '\n\n', dom_pos, '\n\n', sens)


