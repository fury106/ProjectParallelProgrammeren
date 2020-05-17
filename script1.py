if __name__ == "__main__":
	"""
	Dit script bestudeert de invloed van het aantal simulaties op de tijd die nodig is.
	"""
	import projectparallelprogrammeren as ppp
	v0 = ppp.montecarlo_v0
	v1 = ppp.montecarlo_v1
	v2 = ppp.montecarlo_v2
	v3 = ppp.montecarlo_v3
	
	print("100 atomen, 10 simulaties")
	v0.simulatie(100, 10)
	v1.simulatie(100, 10)
	v2.simulatie(100, 10)
	v3.simulatie(100, 10)
	
	print("100 atomen, 20 simulaties")
	v0.simulatie(100, 20)
	v1.simulatie(100, 20)
	v2.simulatie(100, 20)
	v3.simulatie(100, 20)
	
	print("100 atomen, 35 simulaties")
	v0.simulatie(100, 35)
	v1.simulatie(100, 35)
	v2.simulatie(100, 35)
	v3.simulatie(100, 35)
	
	print("100 atomen, 50 simulaties")
	v0.simulatie(100, 50)
	v1.simulatie(100, 50)
	v2.simulatie(100, 50)
	v3.simulatie(100, 50)
	
	print("100 atomen, 100 simulaties")
	v0.simulatie(100, 100)
	v1.simulatie(100, 100)
	v2.simulatie(100, 100)
	v3.simulatie(100, 100)
	
	print("100 atomen, 250 simulaties")
	v0.simulatie(100, 250)
	v1.simulatie(100, 250)
	v2.simulatie(100, 250)
	v3.simulatie(100, 250)
	
	print("100 atomen, 500 simulaties")
	v0.simulatie(100, 500)
	v1.simulatie(100, 500)
	v2.simulatie(100, 500)
	v3.simulatie(100, 500)
	
	print("100 atomen, 1000 simulaties")
	v0.simulatie(100, 1000)
	v1.simulatie(100, 1000)
	v2.simulatie(100, 1000)
	v3.simulatie(100, 1000)
