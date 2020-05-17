if __name__ == "__main__":
	"""
	Dit script bestudeert de invloed van de hoeveelheid atomen op de tijd die nodig is.
	"""
	import projectparallelprogrammeren as ppp
	v0 = ppp.montecarlo_v0
	v1 = ppp.montecarlo_v1
	v2 = ppp.montecarlo_v2
	v3 = ppp.montecarlo_v3
	
	print("100 atomen, 100 simulaties")
	v0.simulatie(100, 100)
	v1.simulatie(100, 100)
	v2.simulatie(100, 100)
	v3.simulatie(100, 100)
	
	print("500 atomen, 100 simulaties")
	v0.simulatie(500, 100)
	v1.simulatie(500, 100)
	v2.simulatie(500, 100)
	v3.simulatie(500, 100)
	
	print("1000 atomen, 100 simulaties")
	v0.simulatie(1000, 100)
	v1.simulatie(1000, 100)
	v2.simulatie(1000, 100)
	v3.simulatie(1000, 100)
	
	print("2000 atomen, 100 simulaties")
	v0.simulatie(2000, 100)
	v1.simulatie(2000, 100)
	v2.simulatie(2000, 100)
	v3.simulatie(2000, 100)
	
	print("5000 atomen, 100 simulaties")
	v0.simulatie(5000, 100)
	v1.simulatie(5000, 100)
	v2.simulatie(5000, 100)
	v3.simulatie(5000, 100)
	
	print("10000 atomen, 100 simulaties")
	v0.simulatie(10000, 100)
	v1.simulatie(10000, 100)
	v2.simulatie(10000, 100)
	v3.simulatie(10000, 100)
	
	print("50000 atomen, 100 simulaties")
	v1.simulatie(50000, 100)
	v2.simulatie(50000, 100)
	v3.simulatie(50000, 100)
	
	print("100000 atomen, 100 simulaties")
	v1.simulatie(100000, 100)
	v2.simulatie(100000, 100)
	v3.simulatie(100000, 100)
