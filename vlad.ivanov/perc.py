from random import randint



class Perceptron(object):
	def __init__(self, s_len, a_len, sToA = None, aToR = None, trainA = None):
		if sToA == None:
			self.sToA = []
		if aToR == None:	
			self.aToR = []
		if trainA == None:
			self.trainA = []
		self.s_len = s_len
		self.a_len = a_len

	def findA(self, vector):
		temp = [0] * self.a_len
		
#		for t in range(len(self.aToR)):
#			temp.append(0)
		for t in range(self.s_len):
			if vector[t] != 0:
				for g in range(self.a_len):
					temp[g] += vector[t] * self.sToA[t][g]
		for t in range(self.a_len):
			if temp[t] > 0:
				temp[t] = 1
			else:
				temp[t] = 0
		return temp

	def findR(self, vector):
		sum = 0

		for t in range(self.a_len):
			sum += vector[t] * self.aToR[t]
		if sum > 0:
			return 1
		elif sum <= 0:
			return -1

	def changeAtor(self, vector, res):
		if res == 1:
			for t in range(self.a_len):
				self.aToR[t] += vector[t]
		else:
			for t in range(self.a_len):
				self.aToR[t] -= vector[t]
	def createStoa(self):
		self.sToA = []
		for i in range(self.s_len):
			self.sToA.append([])		
			for g in range(self.a_len):
				self.sToA[i].append(randint(0, 1) * 2 - 1)
	
	def createTrainA(self, tData):
		self.trainA = []
		w = 0
		for t in tData:
			print(w)
			w += 1
			self.trainA.append(self.findA(t[0]))
			

	def train(self, tData):
		self.createStoa()
		print("create ATOR")
		self.aToR = [0] * self.a_len
		
		self.createTrainA(tData)
#		self.checkTrainA()
		print('ok')
		flag = True
		poi = 0
		while flag:
			poi += 1
			flag = False
			u = 0
			w2 = 0
			w1 = 0
			for vector, res in tData:
				v = self.trainA[u]
				
				u += 1
				#print(u)
				ans = self.findR(v)
			
				if ans != res:
					self.changeAtor(v, res)
					flag = True
				#print(self.aToR, ans, res, v)
			if poi % 5 == 0:
				u = 0
				for vector, res in tData:
					v = self.trainA[u]
				
					u += 1
					#print(u)
					ans = self.findR(v)
			
					if ans != res:
						if res == 1:
							w2 += 1
						else:
							w1 += 1
				print(w1, w2)
			
			
	def check(self, vector):
		return(self.findR(self.findA(vector)))

	def extract(self, path):
		f = open(path, 'w')
		for t in range(len(self.sToA)):
			f.write((' ').join("{0}".format(n) for n in self.sToA[t]))
			f.write('\n')
		f.write('\n')
		f.write((' ').join("{0}".format(n) for n in self.aToR))
		
	def insert(self, path):
		lst = open(path).readlines()
		self.sToA = []
		self.aToR = []
		for t in lst[:-2]:
			self.sToA.append(list(map(int, t[:-1].split())))
		self.aToR = list(map(int, lst[len(lst) - 1].split()))

	def checkTrainA(self):
		for t in range(5000):
			for g in range(5000):
				if t != g and self.trainA[t] == self.trainA[g] and tData[t][1] != tData[g][1]:
					print(t, g)


def createTData():
	ans = list(map(int, open("train_labels").read().split()))
	for i in range(NUM_TRAIN):
		print(i)
		x = list(map(int, open("train/" + str(i + 1) + ".txt").read().split()))
		if ans[i] != cur_d:
			tData.append((x, -1))
		else:
			tData.append((x, 1))

	for i in range(NUM_TRAIN, NUM_TRAIN + 20000):
		if ans[i] == cur_d:
			x = list(map(int, open("train/" + str(i + 1) + ".txt").read().split()))
			tData.append((x, 1))
NUM_TRAIN = 20000
cur_d = 2

#tData = []
#createTData()
#tData = tData[::-1]
#print(len(tData))
#print('training')

p = Perceptron(784, 3500)
#p.train(tData)
#p.extract('stoaandator2')

p.insert('stoaandator2')
print('yep')


fw = open("perc_1", 'w')
for t in range(1000):
	if p.check(list(map(int, open("test/" + str(t + 1) + ".txt").read().split()))) == 1:
		fw.write(str(t + 1) + ':2\n')	
	if t % 500 == 0:
		print(t)




