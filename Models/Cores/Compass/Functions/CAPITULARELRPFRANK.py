from Models.Cores.Compass.Functions.desvio import desvio

class CAPITULARELRPFRANK(desvio):
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("3DC CAPITULARE L PL, FRANKFURT","3DD CAPITULARE R PL, FRANKFURT","CAPITULARE L P. FRANKFURT","CAPITULARE R P. FRANKFURT","CAPITULARELRPFRANK")
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
			response= 0
		else:
			if(self.fdict[fator2][0] < self.fdict[fator1][0]):
				if(desv > 2):
					response= 3
				else:
					response= 1
			else:
				if(desv > 2):
					response= 4
				else:
					response= 2

		if(response >= 3):
			color= "red"
		elif(response < 3 and response >= 1):
			color= "yellow"
		elif(response < 1):
			color= "green"
		else:
			color= ""


		self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
			"desvio": desv,
			"formula": response,
			"color": color
		}

	def response(self):
		if(self.master.fdict["CAPITULARELRPFRANK"]["formula"] == 0):
			return "Cabeças de mandíbula equidistantes ao Plano de Frankfurt."
		elif(self.master.fdict["CAPITULARELRPFRANK"]["formula"] == 1):
			return "Cabeça de mandíbula direita ligeiramente mais superior."
		elif(self.master.fdict["CAPITULARELRPFRANK"]["formula"] == 2):
			return "Cabeça de mandíbula esquerda ligeiramente mais superior."
		elif(self.master.fdict["CAPITULARELRPFRANK"]["formula"] == 3):
			return "Cabeça de mandíbula direita mais superior."
		elif(self.master.fdict["CAPITULARELRPFRANK"]["formula"] == 4):
			return "Cabeça de mandíbula esquerda mais superior."