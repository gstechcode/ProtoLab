class POGPHOLDAWAY:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("Pog P, Holdaway","Pog P, Holdaway","Pog P, Holdaway")
	def load(self, fator1, name1, relacao):
		try:
			self.master.fdict[relacao]= {
				name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			}
		except Exception:
			self.master.fdict[relacao]= {
				name1: "",
			}
