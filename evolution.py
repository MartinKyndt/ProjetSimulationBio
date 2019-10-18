
print('Ceci est notre code') 



def loadData(TSS, TTS) : 
	data = [] 
	f1 = open(TSS)
	f2 = open(TTS)
	tss = [[e for e in l[:-1].split('\t')] for l in f1.readlines()[1:]]
	tts = [[e for e in l[:-1].split('\t')] for l in f2.readlines()[1:]]
	for i in range(10) :
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
 

data = loadData('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat')
print(data)
#insertion(data, 3500)




