class desvio(object):
	def __init__(self, v1,v2, pai):
		self.fdict= pai.csv
		print(f"\n{self.fdict[v1]} -> {self.fdict[v2]}\n")
		return self.fdict[v1][0] - self.fdict[v2][0]