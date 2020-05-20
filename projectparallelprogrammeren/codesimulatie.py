# -*- coding: utf-8 -*-

"""
Module projectparallelprogrammeren.codesimulatie 
=================================================================

Deze module simuleert alles.

"""

import projectparallelprogrammeren

def simulatie():
	"""
	Deze functie voert alle versies uit zodat deze vergeleken kunnen worden qua timing.
	"""
	from importlib import import_module
	for i in range(4):
		#alle versies van de simulatie importeren en achtereenvolgens uitvoeren.
		version = f"montecarlo_v{i}"
		montecarlo = import_module(version)
		montecarlo.simulatie(100,50) #Deze waarden dienen enkel als test

if __name__ == "__main__":
	simulatie()
	
#eof
