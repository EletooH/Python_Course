class EvensRange:
	def __init__(self,**kw):
		self.number = kw['start'] - 1
		self.max_count = kw['max_count'] -1

	def __next__(self):
		if self.number <= self.max_count:
			self.number+=1
			return  self.number
		else:
			raise StopIteration

	def __iter__(self):
		return self

evens_range = EvensRange(max_count=10, start=1)

for i in evens_range:
    if i %2 == 0:
	    print(i)
