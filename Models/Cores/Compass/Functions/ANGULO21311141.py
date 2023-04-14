class ANGULO21311141:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("Ângulo 21/31","Ângulo 11/41","ANG2131","ANG1141","ANG21311141")
	def load(self, fator1, fator2, name1, name2, relacao):
		try:
			self.master.fdict[relacao]= {
				name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
				name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
			}
		except Exception:
			self.master.fdict[relacao]= {
				name1: "",
				name2: "",
			}
