# -*- coding: utf-8 -*-

"""
Module projectparallelprogrammeren.atomen 
=================================================================

Deze module bevat alle atomen die nodig zijn in de simulatie.

"""

import numpy as np

class Atomen:
	"""Deze klasse bevat enkel de coördinaten van de atomen, omdat er enkel de Lennard Jones potentiaal berekend zal worden."""
	
	def __init__(self, aantal):
		print("Er worden", aantal, "atomen gesimuleerd.") #dient voorlopig als test
		
		
#test code
test = Atomen(3)
