
print('Ceci est notre code') 



def loadData(TSS, TTS) : 
	data = [] 
	f1 = open(TSS)
	f2 = open(TTS)
	tss = [[e for e in l[:-1].split('\t')] for l in f1.readlines()[1:]]
	tts = [[e for e in l[:-1].split('\t')] for l in f2.readlines()[1:]]
	for i in range(10) :
		data.append([int(tss[i][2]),int(tts[i][2]), (3000*i)+1, 3000*(i+1)]) 
	print(data)

#def writeData(TSS, TTS)  

loadData('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat')
