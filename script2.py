
class LCG:
	"""
	Linear congruential generator (LCG), gebaseerd op ET-rng.
	
	:param seed: Gebruikt standaard de huidige tijd om verschillende sequenties te berekenen.
	:param a: Parameter voor de LCG.
	:param b: Parameter voor de LCG.
	:param m: Parameter voor de LCG.
	"""
	#De parameters zijn grote getallen. Dit zorgt ervoor dat ze als het juiste type opgeslagen worden.
	import numpy as np
	from time import time_ns
	UINT = np.uint64
	
	def __init__(self, seed=None, a=2147483629, b=2147483629, m=2**31-1):
		#seed instellen
		if seed is None:
			self.seed = LCG.UINT(time_ns())
		else:
			self.seed = LCG.UINT(seed)
		
		#parameters opslaan
		self.a = LCG.UINT(a)
		self.b = LCG.UINT(b)
		self.m = LCG.UINT(m)
		
		#sequentie initialiseren
		self.x = self.seed
	
	def __call__(self):
		"""
		:return: een willekeurig getal
		"""
		self.x = (self.a * self.x + self.b) % self.m
		return self.x


if __name__ == "__main__":
	"""Dit script vergelijkt enkele rng met elkaar."""
	import numpy as np
	from time import time_ns
	from et_stopwatch import Stopwatch
	import projectparallelprogrammeren as ppp
	f90 = ppp.rng.my_f90_module
	
	print("1000000 getallen met numpy generator:")
	array1 = np.empty(1000000)
	with Stopwatch(message="np.random.randint(), 1000000x oproepen"):
		for i in range(1000000):
			array1[i] = np.random.randint(2147483629)
	gem = np.average(array1)
	std = np.std(array1)
	print("Het gemiddelde is:", gem, "en de standaardafwijking is:", std)
	
	print(" ")
	
	array2 = np.empty(1000000)
	with Stopwatch(message="np.random.randint(), 1x oproepen"):
		array2 = np.random.randint(1,2147483629,1000000)
	gem = np.average(array2)
	std = np.std(array2)
	print("Het gemiddelde is:", gem, "en de standaardafwijking is:", std)
	
	"""print(" ")
	print("1000000 getallen met zelfgeschreven python generator:")
	
	array3 = np.empty(1000000)
	with Stopwatch(message="zelf geschreven, 1000000x"):
		for i in range(1000000):
			array3[i] = float(LCG())
	gem = np.average(array3)
	std = np.std(array3)
	print("Het gemiddelde is:", gem, "en de standaardafwijking is:", std)"""
	
	print(" ")
	print("1000000 getallen met zelfgeschreven Fortran rng")
	array4 = np.empty(1000000)
	with Stopwatch(message="1000000x, Fortran rng"):
		array4 = f90.coordinaten(1000000)
	array4 = array4 * 500000 #omdat getallen worden gedeeld door 500000 in rng
	gem = np.average(array4)
	std = np.std(array4)
	print("Het gemiddelde is:", gem, "en de standaardafwijking is:", std)
	

