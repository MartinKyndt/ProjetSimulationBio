import random
print('Ceci est notre code') 



def loadData(TSS, TTS) : 
	data = [] 
	f1 = open(TSS)
	f2 = open(TTS)
	tss = [[e for e in l[:-1].split('\t')] for l in f1.readlines()[1:]]
	tts = [[e for e in l[:-1].split('\t')] for l in f2.readlines()[1:]]
	for i in range(10) :
		data.append([int(tss[i][2]),int(tts[i][2]), (3000*i)+1, 3000*(i+1)]) 
<<<<<<< HEAD
	return(data)
=======
	return data
	

#def writeData(TSS, TTS) 

#Ajoute un codon à une position définie dans le génome
#Décale toutes les positions suivantes
def insertion(data, pos) :
	for i in range(len(data)) :
		for j in range(len(data[0])) :
			if data[i][j] >= pos :
				data[i][j] += 1
 

data = loadData('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat')
print(data)
#insertion(data, 3500)


>>>>>>> def89a69ae6438674fc58df722f301dfafe3efa8


<<<<<<< HEAD
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
=======
>>>>>>> def89a69ae6438674fc58df722f301dfafe3efa8
