class GNMSP:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("Gn MSP","Gn MSP","GNMSP")
	def load(self, fator, name, relacao):
		if(self.master.csv[fator] == ""):
			self.master.fdict[name]= {
			name: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		self.fdict[fator][0]= self.fdict[fator][0] * self.master.gnmsp
		gnmsp= self.fdict[fator][0]
		if(gnmsp > -1 and gnmsp < 1):
			desv= 0
		else:
			if(gnmsp >= -2 and gnmsp <= -1):
				desv= 1
			else:
				if(gnmsp <= 2 and gnmsp >= 1):
					desv= 2
				else:
					if(gnmsp < -2):
						desv= 3
					else:
						desv= 4

		response= desv

		if(response >= 3):
			color= "red"
		elif(response < 3 and response >= 1):
			color= "yellow"
		elif(response < 1):
			color= "green"
		else:
			color= ""


		self.master.fdict[relacao]= {
			name: str(self.fdict[fator][0]) + self.fdict[fator][1],
			"desvio": desv,
			"formula": response,
			"color": color
		}

	def response(self):
		if(self.master.fdict["GNMSP"]["formula"] == 0):
			return "Mandíbula sem desvio aparente."
		elif(self.master.fdict["GNMSP"]["formula"] == 1):
			return "Discreto desvio mandibular à direita."
		elif(self.master.fdict["GNMSP"]["formula"] == 2):
			return "Discreto desvio mandibular à esquerda."
		elif(self.master.fdict["GNMSP"]["formula"] == 3):
			return "Desvio mandibular à direita."
		elif(self.master.fdict["GNMSP"]["formula"] == 4):
			return "Desvio mandibular à esquerda."
		else:
			return ""

