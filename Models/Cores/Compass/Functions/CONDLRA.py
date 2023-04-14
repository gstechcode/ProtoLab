from Models.Cores.Compass.Functions.desvio import desvio

class CONDLRA(desvio):
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2j CondL - A","2k CondR - A","CondL - A","CondR - A","CondLRA")
	def load(self, fator1, fator2, name1, name2, relacao):
		response= 0
		if(self.master.csv[fator1] == "" and self.master.csv[fator2] == ""):
			self.master.fdict[relacao]= {
			name1: "",
			name2: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		elif(self.master.csv[fator1] == ""):
			self.master.fdict[relacao]= {
			name1: "",
			name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		elif(self.master.csv[fator2] == ""):
			self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			name2: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		desv= super().__init__(fator1,fator2, self.master)
		desv= abs(float("%.2f" % desv))
		if(desv <= 1):
			res= 0
		else:
			if(self.fdict[fator2][0] > self.fdict[fator1][0]):
				if(desv >= 2):
					res= 3
				else:
					res= 1
			else:
				if(desv >= 2):
					res= 4
				else:
					res= 2

		if(res >= 4):
			color= "red"
		elif(res < 4 and res >= 1):
			color= "yellow"
		elif(res < 1):
			color= "green"

		self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
			"desvio": desv,
			"formula": res,
			"color": color
		}
	def response(self):
		if(self.master.fdict["CondLRA"]["formula"] == 0):
			return "Comprimentos efetivos da face média simétricos."
		elif(self.master.fdict["CondLRA"]["formula"] == 1):
			return "Comprimentos efetivos da face média ligeiramente assimétricos."
		elif(self.master.fdict["CondLRA"]["formula"] == 2):
			return "Comprimentos efetivos da face média ligeiramente assimétricos."
		elif(self.master.fdict["CondLRA"]["formula"] == 3):
			return "Comprimentos efetivos da face média assimétricos; Direito é maior."
		elif(self.master.fdict["CondLRA"]["formula"] == 4):
			return "Comprimentos efetivos da face média assimétricos; Esquerdo é maior."
		else:
			return ""
