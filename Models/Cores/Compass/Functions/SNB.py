class SNB:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		self.load("2i SNB","SNB")
	def load(self, fator1, name1):
		if(self.master.csv[fator1] == ""):
			self.master.fdict[name]= {
			name: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		relacao= name1
		if(self.fdict[fator1][0] >= 77 and self.fdict[fator1][0] <= 83):
			desv= 0
		else:
			if(self.fdict[fator1][0] < 77):
				desv= 1
			else:
				desv= 2
		res= desv

		if(res >= 3):
			color= "red"
		elif(res < 3 and res >= 1):
			color= "yellow"
		elif(res < 1):
			color= "green"

		self.master.fdict[relacao]= {
			name1: str(self.fdict[fator1][0]) + self.fdict[fator1][1],
			"desvio": desv,
			"formula": res,
			"color": color
		}
	def response(self):
		if(self.master.fdict["SNB"]["formula"] == 0):
			return "Ortognatismo Mandibular."
		elif(self.master.fdict["SNB"]["formula"] == 1):
			return "Retrognatismo Mandibular."
		elif(self.master.fdict["SNB"]["formula"] == 2):
			return "Prognatismo Mandibular."
