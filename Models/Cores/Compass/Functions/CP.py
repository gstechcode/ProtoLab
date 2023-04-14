from Models.Cores.Compass.Functions.desvio import desvio

class CP(desvio):
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("1q 16 Coronal Plane","1r 26  Coronal Plane","16 Coronal Plane","26 Coronal Plane","CP1626")
		self.load("1s 36 Coronal Plane","1t 46 Coronal Plane","36 Coronal Plane","46 Coronal Plane","CP3646")	
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
			if(self.fdict[fator1][0] > self.fdict[fator2][0]):
				if(desv > 3):
					response= 3
				else:
					response= 1
			else:
				if(self.fdict[fator1][0] < self.fdict[fator2][0]):
					if(desv > 3):
						response= 4
					else:
						response= 2
		if(response >= 3):
			color= "red"
		elif(response < 3 and response >= 1):
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
	def response1626(self):
		average= round(self.master.fdict["CP1626"]["formula"])

		if(average == 0):
			return "Molares superiores equidistantes do Plano Coronal."
		elif(average == 1):
			return "Elemento 16 ligeiramente mais mesial."
		elif(average == 2):
			return "Elemento 26 ligeiramente mais mesial."
		elif(average == 3):
			return "Elemento 16 mais mesial."
		elif(average == 4):
			return "Elemento 26 mais mesial."
		else:
			return ""
	def response3646(self):
		average = round(self.master.fdict["CP3646"]["formula"])

		if(average == 0):
			return "Molares inferiores equidistantes do Plano Coronal."
		elif(average == 1):
			return "Elemento 36 ligeiramente mais mesial."
		elif(average == 2):
			return "Elemento 46 ligeiramente mais mesial."
		elif(average == 3):
			return "Elemento 36 mais mesial."
		elif(average == 4):
			return "Elemento 46 mais mesial."
		else:
			return ""