# -*- coding: utf-8 -*-

"""
Module projectparallelprogrammeren.atomen 
=================================================================

Deze module bevat alle atomen die nodig zijn in de simulatie.

"""

import numpy as np
import math
from et_stopwatch import Stopwatch
import projectparallelprogrammeren as ppp
f90 = ppp.rng.my_f90_module

class Atomen:
	"""Deze klasse bevat enkel de coördinaten van de atomen, omdat er enkel de Lennard Jones potentiaal berekend zal worden."""
	
	def __init__(self, aantal):
		#print("Er worden", aantal, "atomen gesimuleerd.") #dient voorlopig als test
		#self.Atomen = np.random.rand(3,aantal) #coordinaten genereren van de atomen
		self.Atomen = np.zeros((3, aantal))
		#for i in range(aantal):
		#	x  = f90.lcg1()
		#	self.Atomen[0, i] = x
		#for i in range(aantal):
		#	y  = f90.lcg1()
		#	self.Atomen[1, i] = y
		#for i in range(aantal):
		#	z  = f90.lcg1()
		#	self.Atomen[2, i] = z
		self.Atomen = f90.coordinaten(aantal)
		#print(self.Atomen)
		
		
	def getCoordinate(self, nummerAtoom):
		
		""" Deze functie retourneert een lijst met het x, y en z coordinaat van het opgegeven atoom.
		
		:param int nummerAtoom: is het nummer (min = 0, max = #atomen - 1) van het atoom waar je de coordinaten van wil weten
		"""
		
		x = self.Atomen[0, nummerAtoom]
		y = self.Atomen[1, nummerAtoom]
		z = self.Atomen[2, nummerAtoom]
		return [x, y, z]
		
		
	def afstandTweeAtomen(self, nummerAtoom1, nummerAtoom2):
		
		""" Deze functie berekent de afstand tussen de twee opgegeven atomen.
		
		:param int nummerAtoom1: is het nummer van het eerste atoom.
		:param int nummerAtoom2: is het nummer van het tweede atoom.
		"""
		
		atoom1 = self.getCoordinate(nummerAtoom1)
		atoom2 = self.getCoordinate(nummerAtoom2)
		afstand = math.sqrt(math.pow((atoom1[0] - atoom2[0]) , 2) + math.pow((atoom1[1] - atoom2[1]) , 2) + math.pow((atoom1[2] - atoom2[2]) , 2))
		return afstand
		
	def berekenLJPot(self):
		""" Deze (test)functie berekent de totale LJ potentiaal van alle atomen. Van deze functie dient een Fortran of C++ variant gemaakt te worden, aangezien lussen traag zijn in Python.
		"""
		totalePot = 0
		#for atoom1 in range(len(self.Atomen[0])):
		#	for atoom2 in range(len(self.Atomen[0])):
		#omdat pot12 = pot21, moet elk paar maar 1x berekend worden, dus zo:
		for atoom1 in range(len(self.Atomen[0])-1):
			for atoom2 in range(atoom1 + 1, len(self.Atomen[0])):
				if atoom1 != atoom2:
					r = self.afstandTweeAtomen(atoom1, atoom2)
					pot = 4*(1/math.pow(r,12) - 1/math.pow(r,6))
					totalePot = totalePot + pot
					#print(atoom1, '-', atoom2, ': ', pot)
		#totalePot = totalePot / 2 # elke potentiaal wordt 2x berekend (pot1-2 = pot2-1)
		#print('totale potentiaal = ', totalePot)
		return totalePot
		
	def getCoordinaten(self):
		"Deze functie retourneert de coordinaten van alle atomen."""
		x = self.Atomen[0].tolist()
		y = self.Atomen[1].tolist()
		z = self.Atomen[2].tolist()
		return [x, y, z]
		
#test code
if __name__ == '__main__':
	test = Atomen(8)
	with Stopwatch(message="getCoordinate"):
		print(test.getCoordinate(2))
		print(test)
	with Stopwatch(message="afstandTweeAtomen"):
		print(test.afstandTweeAtomen(1,2))
	with Stopwatch(message="berekenLJPot"):
		pot = test.berekenLJPot()
	print(test.getCoordinaten)
