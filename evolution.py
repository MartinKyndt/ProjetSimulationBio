
print('Ceci est notre code') 



def loadData(TSS, TTS) : 
	data = [] 
	f1 = open(TSS)
	f2 = open(TTS)
	tss = [[e for e in l[:-1].split('\\')] for l in f1.readlines()]
	tts = f2.readlines() 
	print(tss)

#def writeData(TSS, TTS)  

loadData('tousgenesidentiques/TSS.dat', 'tousgenesidentiques/TTS.dat')
