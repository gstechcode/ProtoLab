class NSLXML:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		if(self.master.csv["NSL x ML"] == ""):
			self.master.fdict["NSL x ML"] = {
			"NSL x ML": "",
			"color": "white"
			}
		self.master.fdict["NSL x ML"] = {
			"NSL x ML": str(self.fdict["NSL x ML"][0]) + str(self.fdict["NSL x ML"][1]),
			"color": "white"
		}