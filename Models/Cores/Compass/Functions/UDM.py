class UDM:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("Upper Dental Midline","UDM","UDM")
	def load(self, fator, name, relacao):
		if(self.master.csv[fator] == ""):
			self.master.fdict[name]= {
			name: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		self.fdict[fator][0]= self.fdict[fator][0] * self.master.udm
		udm= self.fdict[fator][0] 
		if(udm > -1 and udm < 1):
			desv= 0
		else:
			if(udm >= -2 and udm <= -1):
				desv= 1
			else:
				if(udm <= 2 and udm >= 1):
					desv= 2
				else:
					if(udm < -2):
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
		if(self.master.fdict["UDM"]["formula"] == 0):
			return "Linha média superior sem desvio aparente."
		elif(self.master.fdict["UDM"]["formula"] == 1):
			return "Discreto desvio linha média superior à direita."
		elif(self.master.fdict["UDM"]["formula"] == 2):
			return "Discreto desvio linha média superior à esquerda."
		elif(self.master.fdict["UDM"]["formula"] == 3):
			return "Desvio linha média superior à direita."
		elif(self.master.fdict["UDM"]["formula"] == 4):
			return "Desvio linha média superior à esquerda."
		else:
			return ""

