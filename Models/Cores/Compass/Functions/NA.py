class NA:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("11 / NA","21/ NA","11/ NA mm","21/ NA mm","ANG11","ANG21","MM11","MM21","NA")
	def load(self, fator1, fator2, fator3, fator4, name1, name2, name3, name4, relacao):
		try:
			self.master.fdict[relacao]= {
				name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
				name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
				name3: str(self.fdict[fator3][0]) + self.fdict[fator3][1],
				name4: str(self.fdict[fator4][0]) + self.fdict[fator4][1],
			}
		except Exception:
			self.master.fdict[relacao]= {
				name1: "",
				name2: "",
				name3: "",
				name4: "",
			}		
