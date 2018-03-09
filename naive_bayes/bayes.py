# 2018.03.09
# @auther: pkusp
# description: machine learning in action

def loadDataSet():
	postingList = [['my','dog','has','flea',\
					'problems','help','please'],
					['maybe','not','take','him',\
					'stupid']]
	classVec = [0,1]
	return postingList,classVec

def createVocabList(dataSet):
	vocalbSet = set([])
	for doc in dataSet:
		vocalSet = vocalbSet | set(doc)
	return list(vocalbSet)

def setWord2Vec(vocabList,inputSet):
	returnVec = [0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else:
			print("the word:%s is not in !")%word
	return returnVec
