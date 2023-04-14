class errorControl:
	def __init__(self):
		pass
	def Capture(self,fator1,fator2,name1,name2,fdict, relacao):
		if(fator1 == "" and fator2 == ""):
			fdict[relacao]= {
			name1: "",
			name2: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		elif(fator1 == ""):
			fdict[relacao]= {
			name1: str(fator2[0]) + fator2[1],
			name2: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		elif(fator2 == ""):
			fdict[relacao]= {
			name1: str(fator1[0]) + fator1[1],
			name2: "",
			"desvio": 404,
			"formula": 404,
			"color": "white"
			}
			return 0
		else:
			return 1