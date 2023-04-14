class COMMENTS:
	def __init__(self, master):
		self.master= master
		self.__process__()
	def __process__(self):
		response= ""
		db= self.master.fdict
		csv= self.master.csv
		if(db["NOME"] == "" or db["IDADE"] == "" or self.master.denticao == "" or csv["2, A - Np"][0] == "" or csv["2, Pog - Np"][0] == "" or csv["Gn MSP"][0] == "" or csv["Lower Dental Midline"][0] == "" or csv["Upper Dental Midline"][0] == ""):
			response= ""
			print("Aqui")
		else:
			response= "Face com características de " + db["response"]["ANP"] + ", " + db["response"]["POGNP"] + ", " + db["response"]["CONDLRGN"] + ", " +  db["response"]["GNMSP"] + ", " + db["response"]["HC"] + ", " + db["response"]["XMSP131416"] + ", " + db["response"]["RIGHTLFH"] + "."
		self.master.fdict["COMMENTS"] = response.replace(".","") + "."	