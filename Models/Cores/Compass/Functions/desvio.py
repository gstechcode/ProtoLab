class desvio(object):
	def __init__(self, v1,v2, pai):
		self.fdict= pai.csv
		return self.fdict[v1][0] - self.fdict[v2][0]