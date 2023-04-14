class CORPUSLR:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("3e Corpus Length Left","3f Corpus Length Right","Corpus L","Corpus R", "CORPUSLR")
	def load(self, fator1, fator2, name1, name2, relacao):
		self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
		}
	def response(self):
		#A DEFINIR COM DR. MARCOS
		if(self.master.fdict["SNA"]["formula"] == 0):
			return "Ortognatismo Maxilar."
		elif(self.master.fdict["SNA"]["formula"] == 1):
			return "Retrognatismo Maxilar."
		elif(self.master.fdict["SNA"]["formula"] == 2):
			return "Prognatismo Maxilar."
