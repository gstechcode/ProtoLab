from Models.Cores.Compass.Functions.desvio import desvio

class MEFLRCAMPER(desvio):
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2r MeFL X Camper","2s MeFR X Camper", "MeFL X Camper", "MeFR X Camper","MeFLRCamper")
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
			if(self.fdict[fator2][0] < self.fdict[fator1][0]):
				res= 1
			else:
				res= 2

		if(res >= 2):
			color= "red"
		elif(res < 2 and res >= 1):
			color= "yellow"
		elif(res < 1):
			color= "green"
		else:
			color= ""

		self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
			"desvio": desv,
			"formula": res,
			"color": color
		}
	def response(self):
		if(self.master.fdict["MeFLRCamper"]["formula"] == 0):
			return "Dimensões verticais simétricas entre os corpos mandibulares"
		elif(self.master.fdict["MeFLRCamper"]["formula"] == 1):
			return "Mínima dimensão vertical à direita entre os corpos mandibulares"
		elif(self.master.fdict["MeFLRCamper"]["formula"] == 2):
			return "Mínima dimensão vertical à esquerda entre os corpos mandibulares"
		else:
			return ""