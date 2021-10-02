# Define funcoes para verificar a logica de execucao de uma aplicacao produtor/consumidor

class PRODCONS:
	def __init__(self):
		self.fullBuffer = False
		self.valuesInserted = 0
		self.sizeBuffer = 5

	def insertInBuffer(self, id, value):
		'''Incrementa a quantidade de valores que estão no buffer'''
		self.valuesInserted += 1
		# print("Produtor " + str(id) + " inseriu o valor " + str(value))

	def readBuffer(self, id):
		if(self.valuesInserted != self.sizeBuffer):
			print("ERRO: consumidor " + str(id) + " consumiu sem que o buffer estivesse cheio")
		else:
			# print("Consumidor " + str(id) + " leu o buffer")
			self.valuesInserted = 0
			self.fullBuffer = False

	def sinalizeFullBuffer(self, id):
		'''Recebe o id do produtor que sinalizou. Verifica se a decisão de sinalização está correta'''
		if(self.valuesInserted != self.sizeBuffer):
			print("ERRO: produtor " + str(id) + " sinalizou que o buffer está cheio sem que ele estivesse")
		else:
			self.fullBuffer = True