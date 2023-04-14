from Models.Cores.Compass.Functions.desvio import desvio

class CARL(desvio):
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2z Condylar Axis Right","2z Condylar Axis Left","Condylar Axis Right","Condylar Axis Left","CARL")
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
		if(desv <= 2):
			response= 0
		else:
			if(desv > 5):
				response= 2
			else:
				response= 1

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
		if(self.master.fdict["CARL"]["formula"] == 0):
			return "Eixos condilares simétricos."
		elif(self.master.fdict["CARL"]["formula"] == 1):
			return "Eixos condilares ligeiramente assimétricos."
		elif(self.master.fdict["CARL"]["formula"] == 2):
			return "Eixos Condilares assimétricos."