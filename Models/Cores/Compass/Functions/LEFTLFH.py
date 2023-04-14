class LEFTLFH:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2bB2 Left Lower Facial Height","Left LFH")
	def load(self, fator1, relacao):
		if(self.master.csv[fator1] == ""):
			self.master.fdict[name]= {
			name: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		if(self.fdict[fator1][0] < 37):
			desvio= 1
		else:
			if(self.fdict[fator1][0] > 45):
				desvio= 2
			else:
				desvio= 0
		if(desvio >= 2):
			color= "red"
		elif(desvio < 2 and desvio >= 1):
			color= "yellow"
		elif(desvio < 1):
			color= "green"
		else:
			color= ""

		self.master.fdict[relacao]= {
			 relacao: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			"desvio": desvio,
			"formula": desvio,
			"color": color
		}
	def response(self):
		if(self.master.fdict["Left LFH"]["formula"] == 0):
			return "LFH é mediano"
		elif(self.master.fdict["Left LFH"]["formula"] == 1):
			return "Ângulo da AFAI diminuído"
		elif(self.master.fdict["Left LFH"]["formula"] == 2):
			return "Ângulo da AFAI aumentado"
		else:
			return ""