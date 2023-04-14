from Models.Cores.Compass.Functions.desvio import desvio

class MEFLRMSP(desvio):
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2t MeFL X MSP","2u MeFR X MSP","MeFL X MSP","MeFR X MSP","MEFLRMSP")
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
				response= 1
			else:
				response= 2

		if(response >= 2):
			color= "red"
		elif(response < 2 and response >= 1):
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
		if(self.master.fdict["MEFLRMSP"]["formula"] == 0):
			return "Corpos mandibulares equidistantes ao plano sagital mediano."
		elif(self.master.fdict["MEFLRMSP"]["formula"] == 1):
			return "Desvio mandibular à esquerda na região de Forames Mentonianos."
		elif(self.master.fdict["MEFLRMSP"]["formula"] == 2):
			return "Desvio mandibular à direita na região de Forames Mentonianos."