class CBA:
	def __init__(self, master):
		self.master= master
		self.master.fdict["CBA"]= { 
			"Cranial Base Angle": str(self.master.csv["2c Cranial Base Angle"][0]) + str(self.master.csv["2c Cranial Base Angle"][1])
			}
