# -*- coding: utf-8 -*-
import numpy as np
import random
import shutil
import sys
import os
import math
import time 
import pdb #Debugueur
import matplotlib.pyplot as plt
from TwisTranscripT.TSC import *


print('Ceci est notre code') 

####################################
#ECRITURE ET LA LECTURE DE FICHIERS#
####################################

#Ecrit les données TSS et TTS dans l'ordre : 
#debut de domaine, debut de gene, fin de gene, fin de domaine
def writeData_init(TSS, TTS, GFF) :
	f1 = open('tousgenesidentiques/TSSevol_prev.dat', 'w')
	f2 = open('tousgenesidentiques/TTSevol_prev.dat', 'w')
	f3 = open('tousgenesidentiques/TSSevol.dat', 'w')
	f4 = open('tousgenesidentiques/TTSevol.dat', 'w')
	f5 = open('tousgenesidentiques/tousgenesidentiques_evol_prev.gff', 'w')
	f6 = open('tousgenesidentiques/tousgenesidentiques_evol.gff', 'w')
	f1.close()
	f2.close()
	f3.close()
	f4.close()
	f5.close()
	f6.close()
	shutil.copy(TSS,'tousgenesidentiques/TSSevol.dat')
	shutil.copy(TTS,'tousgenesidentiques/TTSevol.dat')
	shutil.copy(GFF,'tousgenesidentiques/tousgenesidentiques_evol.gff')


def loadData(TSS, TTS, PROT, GFF) :
	num_gene = []
	gene_pos = []
	dom_pos = []
	sens = []
	f1 = open(TSS)
	f2 = open(TTS)
	f3 = open(PROT)
	f4 = open(GFF)
	tss = [[e for e in l[:-1].split('\t')] for l in f1.readlines()[1:]]
	tts = [[e for e in l[:-1].split('\t')] for l in f2.readlines()[1:]]
	prot = [[e for e in l[:-1].split('\t')] for l in f3.readlines()[1:]]
	gff = f4.readlines()[4].split('\t')
	fin = int(gff[4])
	print(fin)
	for i in range(10) :
		num_gene.append(i)
		gene_pos.append([int(tss[i][2]),int(tts[i][2])])
		sens.append(tss[i][1])
		if i != 9:
			dom_pos.append([int(prot[i][1]), int(prot[i+1][1])-1])
		else:
			dom_pos.append([int(prot[i][1]), fin])
	return (np.array(num_gene), np.array(dom_pos), np.array(gene_pos), np.array(sens))


def writeData_init(TSS, TTS, GFF, PROT) :
	f1 = open('tousgenesidentiques/TSSevol_prev.dat', 'w')
	f2 = open('tousgenesidentiques/TTSevol_prev.dat', 'w')
	f3 = open('tousgenesidentiques/protevol_prev.dat', 'w')
	f4 = open('tousgenesidentiques/TSSevol.dat', 'w')
	f5 = open('tousgenesidentiques/TTSevol.dat', 'w')
	f6 = open('tousgenesidentiques/protevol.dat', 'w')
	f7 = open('tousgenesidentiques/tousgenesidentiques_evol_prev.gff', 'w')
	f8 = open('tousgenesidentiques/tousgenesidentiques_evol.gff', 'w')
	f1.close()
	f2.close()
	f3.close()
	f4.close()
	f5.close()
	f6.close()
	f7.close()
	f8.close()
	shutil.copy(TSS,'tousgenesidentiques/TSSevol.dat')
	shutil.copy(TTS,'tousgenesidentiques/TTSevol.dat')
	shutil.copy(PROT,'tousgenesidentiques/protevol.dat')
	shutil.copy(GFF,'tousgenesidentiques/tousgenesidentiques_evol.gff')

	
def writeData(gene_pos, sens, num_gene, dom_pos) :
	shutil.copy('tousgenesidentiques/TSSevol.dat', 'tousgenesidentiques/TSSevol_prev.dat')
	shutil.copy('tousgenesidentiques/TTSevol.dat', 'tousgenesidentiques/TTSevol_prev.dat')
	shutil.copy('tousgenesidentiques/protevol.dat', 'tousgenesidentiques/protevol_prev.dat')
	shutil.copy('tousgenesidentiques/tousgenesidentiques_evol.gff', 'tousgenesidentiques/tousgenesidentiques_evol_prev.gff')
	f1 = open('tousgenesidentiques/TSSevol.dat', 'w')
	f2 = open('tousgenesidentiques/TTSevol.dat', 'w')
	f3 = open('tousgenesidentiques/protevol.dat', 'w')
	'''
	Dans params.ini :
	tssevol = tousgenesidentiques/TSSevol.dat
	ttsevol = tousgenesidentiques/TTSevol.dat
	Il faut changer le format  de TSSevol et TTSevol (pd.dataframe) pour que la ligne 557 de TSC.py puisse s'exécuter et lire le fichier correctement
	'''
	f1.write("TUindex\tTUorient\tTSS_pos\tTSS_strength\n")
	f2.write("TUindex\tTUorient\tTTS_pos\tTTS_proba_off\n")
	f3.write("prot_name\tprot_pos\n")
	n = len(gene_pos)
	for i in range(n):
		f1.write(str(num_gene[i])+'\t')
		f2.write(str(num_gene[i])+'\t')
		f1.write(sens[i]+'\t')
		f2.write(sens[i]+'\t')
		f1.write(str(gene_pos[i,0])+'\t.2\n')
		f2.write(str(gene_pos[i,1])+'\t1.\n')
		f3.write("hns\t{}\n".format(dom_pos[i,0]))
	f1.close()
	f2.close()
	f3.close()
	
	f4 = open('tousgenesidentiques/tousgenesidentiques_evol.gff', 'r')
	contenu = [[e for e in l.split('\t')] for l in f4.readlines()]
	f4.close()
	contenu[3] = ['##sequence-region tousgenesidentiques' + str(dom_pos[0][0])+ ' ' + str(dom_pos[-1][1]) + '\n']
	contenu[4][3] = str(dom_pos[0,0])
	contenu[4][4] = str(dom_pos[-1,1])
	for i in range(n):
		contenu[i+5][3] = str(gene_pos[i,0])
		contenu[i+5][4] = str(gene_pos[i,1])
		contenu[i+5][6] = sens[i]
	
	f5 = open('tousgenesidentiques/tousgenesidentiques_evol.gff', 'w')
	sep='\t'
	for i in range(len(contenu)):
		f5.write(sep.join(contenu[i]))	
	f5.close()

		
def writeData_return(FILE_EVENTS):
	print('WRITE RETURN')
	shutil.copy('tousgenesidentiques/TSSevol_prev.dat', 'tousgenesidentiques/TSSevol.dat')
	shutil.copy('tousgenesidentiques/TTSevol_prev.dat', 'tousgenesidentiques/TTSevol.dat')
	shutil.copy('tousgenesidentiques/tousgenesidentiques_evol_prev.gff', 'tousgenesidentiques/tousgenesidentiques_evol.gff')
	shutil.copy('tousgenesidentiques/protevol_prev.dat', 'tousgenesidentiques/protevol.dat')
	with open(FILE_EVENTS, 'rb+') as filehandle:#remove last event (ex : '2,')
		filehandle.seek(-1, os.SEEK_END)
		filehandle.truncate()
		filehandle.seek(-1, os.SEEK_END)
		filehandle.truncate()
	num_gene, dom_pos, gene_pos, sens = loadData('tousgenesidentiques/TSSevol.dat', 'tousgenesidentiques/TTSevol.dat', 'tousgenesidentiques/protevol.dat', 'tousgenesidentiques/tousgenesidentiques_evol.gff')
	return  dom_pos, gene_pos, sens, num_gene


#########################
#EVENEMENTS DE MUTATIONS#
#########################


#Ajoute un codon à une position définie dans le génome
#Décale toutes les positions suivantes
def insertion(dom_pos, gene_pos, sens, num_gene) :
	pos = randomPos(dom_pos, gene_pos)
	for i in range(len(gene_pos)) :
		for j in range(len(gene_pos[i])) :
			if gene_pos[i,j] >= pos :
				gene_pos[i,j] += 1
	for i in range(len(dom_pos)) :
		for j in range(len(dom_pos[i])) :
			if dom_pos[i,j] >= pos :
				dom_pos[i,j] += 1
	print('\nINSERTION : {}\n'.format(pos))
	return (dom_pos, gene_pos, sens, num_gene)
				
				

#Méthode , delete une position aléatoire pos
#Décale toutes les positions suivantes
def deletion(dom_pos, gene_pos, sens, num_gene) :
	pos = randomPos(dom_pos, gene_pos)
	for i in range(len(gene_pos)) :
		for j in range(len(gene_pos[i])) :
			if gene_pos[i,j] >= pos :
				gene_pos[i,j] -= 1
	for i in range(len(dom_pos)) :
		for j in range(len(dom_pos[i])) :
			if dom_pos[i,j] >= pos :
				dom_pos[i,j] -= 1
	print('\nDELETION : {}\n'.format(pos))
	return (dom_pos, gene_pos, sens, num_gene)	
			
			
def inversion(dom_pos, gene_pos, sens, num_gene) :
	pos1 = randomPos(dom_pos, gene_pos)
	pos2 = randomPos(dom_pos, gene_pos)
	pos11 = min(pos1, pos2)
	pos22 = max(pos1, pos2)
	pos1 = pos11
	pos2 = pos22
	new_pos_gene = []
	new_pos_dom = []
	new_sens = sens
	###########################################
	#Verify that the genes are not cut in half# #Condition normalement vérifiée dans random_event
	###########################################
	for i in range(len(gene_pos)):
		"""print('i : ', i)
		#print('gene position : ', gene_pos[i,0],gene_pos[i,1])
		#print('positions of mutations : ', pos1, pos2, '\n')"""
		
		if pos1 >= min(gene_pos[i,0], gene_pos[i,1]) and pos1 <= max(gene_pos[i,0], gene_pos[i,1]) or pos2 >= min(gene_pos[i,0], gene_pos[i,1]) and pos2 <= max(gene_pos[i,0], gene_pos[i,1]):
			print('Gene {} : [{}-{}], positions : [{}-{}]'.format(i, gene_pos[i,0], gene_pos[i,1], pos1, pos2))
			sys.exit('impossible to cut the gene')
			
	#############################
	#Change positions of domains#
	#############################
	for i in range(len(dom_pos)) :
		for j in range (len(dom_pos[i])) :
			#Pour chaque position de début ou fin de domaine
			#Si elle se situe entre les 2 positions d'inversion
			#On change sa nouvelle position
			if dom_pos[i][j] > pos1 and dom_pos[i][j] < pos2 :
				new_pos_dom.append(pos1 + pos2 - dom_pos[i][j])
				"""print('previous dom_pos : ' + str(dom_pos[i][j]) + ' ; New dom_pos : ' + str(pos1 + pos2 - dom_pos[i][j]) + '\n')"""
			else :
				new_pos_dom.append(dom_pos[i][j])
				"""print('same dom_pos : ' + str(dom_pos[i][j])  + '\n')"""
	###########################
	#Change positions of genes#
	###########################
	affected_genes = []
	for i in range(len(gene_pos)) :
		for j in range (len(gene_pos[i])) :
			#Pour chaque position de début ou fin de gene
			#Si elle se situe entre les 2 positions d'inversion
			#On change sa nouvelle position
			if gene_pos[i][j] > pos1 and gene_pos[i][j] < pos2 :
				new_pos_gene.append(pos1 + pos2 - gene_pos[i][j])
				affected_genes.append(i)
				"""print('previous gene_pos : ' + str(gene_pos[i][j]) + ' ; New gene_pos : ' + str(pos1 + pos2 - gene_pos[i][j]) + '\n')"""
			else :
			#Sinon sa position reste la même
				new_pos_gene.append(gene_pos[i][j])
				"""print('same gene_pos : ' + str(gene_pos[i][j])  + '\n')"""
	#######################
	#Change order of genes#
	#######################
	affected_genes = np.unique(np.array(affected_genes))
	new_num_gene = num_gene #Initialisation du nouveau tableau d'index de genes
	inverted_real_affected_genes = np.flip(np.array([num_gene[i] for i in affected_genes])) 
	#affected_genes est la position des gènes affectés dans l'ordre où ils sont présentés
	#inverted_real_affected_genes est l'index des gènes affectés dans leur nouvel ordre
	#num_gene est le tableau de tous les index des genes
	for i in affected_genes :
		new_num_gene[i] = inverted_real_affected_genes[i - affected_genes[0]]
		'''print(affected_genes, inverted_real_affected_genes, new_num_gene)'''
	#############################
	#Change orientation of genes#
	#############################
	to_invert = []
	for i in affected_genes :
		to_invert.append(sens[i])
	inverted = np.flip(np.array(to_invert))
	for i in range(len(inverted)) :
		if inverted[i] == "+" :
			inverted[i] = "-"
		else :
			inverted[i] = "+"
	for i in (affected_genes) :
		new_sens[i] = inverted[i-affected_genes[0]]
	new_pos_dom = np.sort(np.array(new_pos_dom)).reshape(len(dom_pos), 2)
	new_pos_gene = np.sort(np.array(new_pos_gene)).reshape(len(gene_pos), 2)
	#On inverse TSS et TTS pour les genes en sens '-'
	for i in range(len(new_sens)) :
		if new_sens[i] == '-' :
			tss = new_pos_gene[i,1]#La position la plus élevée est le tss
			tts = new_pos_gene[i,0]#La position la plus basse est le tts
			new_pos_gene[i,0] = tss#On met dans la colonne tss la position élevée
			new_pos_gene[i,1] = tts#On met dans la colonne tts la position basse
			
	print('\nINVERSION : {}-{}\n'.format(pos1,pos2))
	return (new_pos_dom, new_pos_gene, new_sens, new_num_gene)
	
##############################################
#CHOIX D'UNE POSITION ALEATOIRE POUR MUTATION#
##############################################

#Les positions ne se trouvent pas dans les régions codantes
def randomPos(dom_pos, gene_pos) : 
	deb = dom_pos[0,0]
	fin = dom_pos[-1,1]
	count = 0
	cond = False
	while(not cond) : 
		pos = random.randint(deb,fin)
		for i in range(len(gene_pos)):
			if i == 0 :
				if (pos < min(gene_pos[i,0] - 60, gene_pos[i,1] - 60)) : 
					cond = True
			if (pos > max(gene_pos[i-1][1] + 60, gene_pos[i-1][0] + 60)  and pos < min(gene_pos[i][0] - 60, gene_pos[i][1] - 60)) :
				cond = True
			if i == len(gene_pos)-1 :
				if (pos > max(gene_pos[i,1] + 60, gene_pos[i,0] + 60)) :
					cond = True

		for i in range(len(dom_pos)) : #Refuse mutations at the exact positions of barriers
			for j in range(len(dom_pos[i])) :
				if pos == dom_pos[i, j] :
					cond = False
	return pos
	
	
#########
#FITNESS#
#########


def fitness(result, expected) : 
	"""
	obs = [] 
	cible = [] 
	f1 = open(result)
	f2 = open(expected)
	res = [[e for e in l[:-1].split('\t')] for l in f1.readlines()[0:]]
	'''print("\n\n\nEXPRESSION PROFILE \n")
	print(res)'''
	sum_transcripts = sum([int(line[7]) for line in res[1:]])
	
	exp = [[e for e in l[:-1].split()] for l in f2.readlines()[0:]]
	'''print("\nEXPECTED PROFILE \n")
	print(exp)'''
	for i in range(10) :
		cible.append(float(exp[i][1])*sum_transcripts)
		#cible.append(int(exp[i][4]))
		obs.append(int(res[i+1][7]))
	fitness = 0 
	for i in range(10) : 
		fitness += abs(math.log(obs[i]/cible[i]))
	fitness = math.exp(-fitness)
	return(fitness)
	""" 
	
	obs = pd.read_csv( 'output/all_tr_info.csv', sep = '	')
	cible = pd.read_csv('environment.dat', sep = '	')
	
	#keep in memory the order of the transcript unit
	transcripts_index = obs['TUindex'].tolist() 
	#sum of the number of observed transcripts
	total_nb_transcripts = obs.sum(axis=0)[7] 
	
	#calculate the rate of transcript of each gene
	obs['rate']= obs['number of transcripts generated']/total_nb_transcripts
	
	#join observed and expected dataset, according to the TUindex
	obs = obs.set_index('TUindex').join(cible.set_index('TUindex'), how= 'inner')
	
	#calculate the fitness
	obs['fitness'] = (obs['rate']/obs['expected_rate'])
	f = obs['fitness'].tolist()
	log = list(map(math.log, f))

	#return the fitness
	return(math.exp(-sum(log)))

#Write fitness in empty file
def first_fitness(FILE_FITNESS, event):
	f = open(FILE_FITNESS, 'a')
	newfitness = fitness('output/all_tr_info.csv',"environment.dat")
	f.write(event.split(',')[0] + ':' + str(newfitness))
	f.close()

#Compare and write fitness in not empty file
def majFitness(num_gene, dom_pos, gene_pos, sens, FILE_EVENTS, FILE_FITNESS, event, q) :
	new_dom_pos = dom_pos
	new_gene_pos = gene_pos
	new_sens = sens
	new_num_gene = num_gene
	#newfitness = fitness('output/all_tr_info.csv',"cible.dat")
	newfitness = fitness('output/all_tr_info.csv',"environment.dat")
	f = open(FILE_FITNESS, 'r') 
	t = [[e for e in l[:-1].split(':')] for l in f.readlines()[0:]] #event : fitness
	f3 = open(FILE_FITNESS, 'r')
	lines = f3.readlines()
	last_line = lines[len(lines)-1]
	f3.close()
	f2 = open(FILE_FITNESS, 'a')
	f = open(FILE_EVENTS, 'r')
	line = f.readline()
	f.close()
	if(newfitness > float(t[len(t)-1][1])) :
		f2.write('\n' + event.split(',')[0] + ':' + str(newfitness)) #Write superior fitness
	else :
		delta_fitness = float(t[len(t)-1][1]) - newfitness
		dice = random.random()
		print('\n\nProbability of accepting : ', math.exp(-delta_fitness/q))
		if dice < math.exp(-delta_fitness/q) :
		#if(math.exp(-delta_fitness/q) < 0.5)  :
			f2.write('\n' + event.split(',')[0] + ':' + str(newfitness))  #Write inferior fitness
		
		else : 
			#Return to previous step
			new_dom_pos, new_gene_pos, new_sens, new_num_gene = writeData_return(FILE_EVENTS)
			f2.write('\n'+last_line)
	f2.close()
	#return newfitness, num_gene, dom_pos, gene_pos, sens
	return new_dom_pos, new_gene_pos, new_sens, new_num_gene,


##############
#RANDOM EVENT#
##############
def random_event(dom_pos, gene_pos, sens, num_gene, q, FILE_EVENTS, FILE_FITNESS) :
	#pdb.set_trace()
	
	choice = random.random()
	if choice <= 1/3 :
		new_dom_pos, new_gene_pos, new_sens, new_num_gene = insertion(dom_pos, gene_pos, sens, num_gene)
		event = "0,"
	elif choice > 1/3 and choice <= 2/3 :
		new_dom_pos, new_gene_pos, new_sens, new_num_gene = deletion(dom_pos, gene_pos, sens, num_gene)
		event = "1,"
	else :
		new_dom_pos, new_gene_pos, new_sens, new_num_gene = inversion(dom_pos, gene_pos, sens, num_gene)
		event = "2,"
	f = open(FILE_EVENTS, 'a')
	f.write(event)
	f.close()
	f = open(FILE_EVENTS, 'r')
	line = f.readline()
	print("All events : ", line)
	print("Number of events : ", len(line.split(','))-1, '\n')
	writeData(new_gene_pos, new_sens, new_num_gene, new_dom_pos)
	#print('AVANT TRANSCRIPTION \n',new_gene_pos, '\n', new_dom_pos)
	if (len(line.split(',')) == 2 ): #Write in a new fitness file if this is the first event (len([event, '']) = 2)
		start_transcribing('params.ini')
		first_fitness(FILE_FITNESS, event)
		#majFitness(FILE_EVENTS, FILE_FITNESS, event ,q)
	else :
		start_transcribing('params.ini')
		new_dom_pos, new_gene_pos, new_sens, new_num_gene = majFitness(new_num_gene, new_dom_pos, new_gene_pos, new_sens, FILE_EVENTS, FILE_FITNESS, event ,q)
		#print('APRES MAJ FITNESS : \n ',new_gene_pos, '\n', new_dom_pos)
	f.close()
	#print("DOMAINES après\n\n", new_dom_pos, "\n\n")
	return(new_dom_pos, new_gene_pos, new_sens, new_num_gene)
	
#############
#EXPERIENCES#
#############

#Effet du q sur l'évolution de la fitness --> avec l'historique des fitness, on mesure le dfit/dt en fonction du q et la fitness maximale et finale atteinte en moyenne sur 9 simulation par q
def exp_1() :
	qs = [0.00001, 0.00005, 0.0001, 0.0005, 0.001, 0.005]
	for q in qs : #Le 1 des parametres signifie que c'est la première répétition
		PARAMS = "1_" + str(q) + "_" + str(1) + "_" + str(round(1/3, 2)) #1/3 = proba d'inversion
		main(PARAMS, q, 1000)

################
#TESTS METHODES#
################

def main(PARAMS, q, nbgeneration) :
	#Initiation of clock
	start_time = time.time()
		
	#PARAMS = [noExperience, noSimulation(défini par set de paramètres pour expériences taux d'expression) , q, taux_inv, taux_inser, taux_inver]
	FILE_EVENTS = "all_events_{}.txt".format(PARAMS)#Différent nom de fichier pour chaque set de paramètres
	FILE_FITNESS = "all_fitness_{}.txt".format(PARAMS)#Différent nom de fichier pour chaque set de paramètres

	writeData_init('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat', 'tousgenesidentiques/tousgenesidentiques.gff', 'tousgenesidentiques/prot.dat')
	num_gene, dom_pos, gene_pos, sens = loadData('tousgenesidentiques/TSSevol.dat', 'tousgenesidentiques/TTSevol.dat', 'tousgenesidentiques/protevol.dat', 'tousgenesidentiques/tousgenesidentiques_evol.gff')

	fitnesses = open(FILE_FITNESS, 'w')
	fitnesses.close()
	events = open(FILE_EVENTS, 'w')
	events.close()
	for i in range(nbgeneration) :
		print("\nIteration : ", i+1)
		dom_pos, gene_pos, sens, num_gene = random_event(dom_pos, gene_pos, sens, num_gene, q, FILE_EVENTS, FILE_FITNESS)
	end_time = time.time()
	t = end_time - start_time
	s = t%60
	r = t//60
	m = r%60
	r = r//60
	h = r%24
	print (t)
	print('{} hours, {} minutes, {} seconds'.format(h, m, s))


if __name__ == "__main__" :
	PARAMS = "abc"
	main(PARAMS, 0.0001, 100)
	#exp_1()
	#exp_2()
	#exp_3()
	#exp_4()
	#exp_5()
	#exp_6()
