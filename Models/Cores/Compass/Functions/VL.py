from Models.Cores.Compass.Functions.desvio import desvio

class VL(desvio):
	def __init__(self,master):
		self.fdict= master.fdict
		self.master= master
		self.load("1ta 16 VL Inclination","1tb 26 VL Inclination","16 VL Inclination","26 VL Inclination","VL1626")
		self.load("1tc 13 VL Inclination","1td 23 VL Inclination","13 VL Inclination","23 VL Inclination","VL1323")
		self.load("1te 46 VL Inclination","1tf  36 VL Inclination","46 VL Inclination","36 VL Inclination","VL4636")
		self.load("1tg 43 VL Inclination","1th 33 VL Inclination","43 VL Inclination","33 VL Inclination","VL4333")
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
		if(desv <= 3):
			response= 0
		else:
			if(desv > 5):
				response= 2
			else:
				response= 1
		if(response >= 2):
			color= "red"
		elif(response >= 1 and response < 2):
			color= "yellow"
		elif(response < 1):
			color= "green"

		self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			name2: str(self.fdict[fator2][0]) + self.fdict[fator2][1],
			"desvio": desv,
			"formula": response,
			"color": color
		}
	def response(self):
		average= round((self.master.fdict["VL1626"]["formula"] + self.master.fdict["VL1323"]["formula"] + self.master.fdict["VL4636"]["formula"] + self.master.fdict["VL4333"]["formula"])/2)
		if(average == 0):
			return "Inclinações vestibulolinguais simétricas."
		elif(average == 1):
			return "Inclinações vestibulolinguais ligeiramente assimétricas."
		elif(average == 2):
			return "Inclinações vestibulolinguais assimétricas."
		else:
			return ""