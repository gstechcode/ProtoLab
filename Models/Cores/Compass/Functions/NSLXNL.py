class NSLXNL:
	def __init__(self, master):
		self.fdict= master.csv
		self.master= master
		if(self.master.csv["NSL x NL"] == ""):
			self.master.fdict["NSL x NL"] = {
			"NSL x ML": "",
			"color": "white"
			}
		self.master.fdict["NSL x NL"] = {
			"NSL x NL": str(self.fdict["NSL x NL"][0]) + str(self.fdict["NSL x NL"][1]),
			"color": "white"
		}