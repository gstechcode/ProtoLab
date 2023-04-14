from Models.Cores.Compass.Functions.desvio import desvio

class UPPERLOWERHEIGHT(desvio):
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2a Upper Facial Height","2b Lower Facial Height", "Upper Facial Height","Lower Facial Height", "ULH")
	def load(self,fator1,fator2, name1, name2, relacao):
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

		if(self.master.idade <= 6):
			if(desv >= -2 and desv <= 2):
				res= 0
			else:
				if(self.fdict[fator2][0] > self.fdict[fator1][0]):
					res= 1
				else:
					res= 2
		else:
			if(self.master.idade > 12):
				if(desv >= 8 and desv <= 12):
					res= 0
				else:
					if(self.fdict[fator2][0] > self.fdict[fator1][0]):
						res= 1
					else:
						res= 2
			else:
				if(desv >= 3 and desv <= 7):
					res= 0
				else:
					if(self.fdict[fator2][0] > self.fdict[fator1][0]):
						res= 1
					else:
						res= 2

		if(res >= 2):
			color= "red"
		elif(res < 2 and res >= 1):
			color= "yellow"
		else:
			color= "green"

		self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
			"desvio": desv,
			"formula": res,
			"color": color
		}
	def response(self):
		if(self.master.fdict["ULH"]["formula"] == 0):
			return "AFAI semelhante à AFAS."
		elif(self.master.fdict["ULH"]["formula"] == 1):
			return "AFAI maior do que AFAS."
		elif(self.master.fdict["ULH"]["formula"] == 2):
			return "AFAI menor do que AFAS."
