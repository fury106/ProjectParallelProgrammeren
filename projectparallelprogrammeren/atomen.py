# -*- coding: utf-8 -*-

"""
Module projectparallelprogrammeren.atomen 
=================================================================

Deze module bevat alle atomen die nodig zijn in de simulatie.

"""

import numpy as np
import math

class Atomen:
	"""Deze klasse bevat enkel de coördinaten van de atomen, omdat er enkel de Lennard Jones potentiaal berekend zal worden."""
	
	def __init__(self, aantal):
		print("Er worden", aantal, "atomen gesimuleerd.") #dient voorlopig als test
		self.Atomen = np.random.rand(3,aantal) #coordinaten genereren van de atomen
		print(self.Atomen)
		
		
	def getCoordinate(self, nummerAtoom):
		""" Deze functie retourneert een lijst met het x, y en z coordinaat van het opgegeven atoom.
		:param int nummerAtoom: is het nummer (min = 0, max = #atomen - 1) van het atoom waar je de coordinaten van wil weten"""
		x = self.Atomen[0, nummerAtoom]
		y = self.Atomen[1, nummerAtoom]
		z = self.Atomen[2, nummerAtoom]
		return [x, y, z]
		
		
	def afstandTweeAtomen(self, nummerAtoom1, nummerAtoom2):
		""" Deze functie berekent de afstand tussen de twee opgegeven atomen.
		:param int nummerAtoom1: is het nummer van het eerste atoom.
		:param int nummerAtoom2: is het nummer van het tweede atoom."""
		atoom1 = self.getCoordinate(nummerAtoom1)
		atoom2 = self.getCoordinate(nummerAtoom2)
		afstand = math.sqrt(math.pow((atoom1[0] - atoom2[0]) , 2) + math.pow((atoom1[1] - atoom2[1]) , 2) + math.pow((atoom1[2] - atoom2[2]) , 2))
		return afstand
		
#test code
test = Atomen(8)
print(test.getCoordinate(2))
print(test)
print(test.afstandTweeAtomen(1,2))
