#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for f2py module `projectparallelprogrammeren.atomenf`."""

import projectparallelprogrammeren as ppp
import math
# create an alias for the binary extension cpp module
f90 = ppp.atomenf.f90_module

def test_lj2atomen():
	"""Test om de potentiaal tussen 2 atomen te berekenen"""
	afstand = 1.5
	pot = 4*((1/afstand)**12 - (1/afstand)**6)
	potf = f90.ljpot2atomen(afstand)
	assert round(pot, 7) == round(potf, 7)

def test_lj2atomen_afstand0():
	"""Test om na te gaan dat er geen errors verschijnen wanneer de afstand 0 is"""
	afstand = 0
	pot = f90.ljpot2atomen(afstand)
	assert pot == 0
	
def test_alle_jlpot():
	"""test om alle potentialen te berekenen"""
	atomen = [[1,2,3],[4,5,6],[7,8,9]]
	r12 = math.sqrt(math.pow(2-1,2)+math.pow(5-4,2)+math.pow(8-7,2))
	r13 = math.sqrt(math.pow(3-1,2)+math.pow(6-4,2)+math.pow(9-7,2))
	r23 = math.sqrt(math.pow(3-2,2)+math.pow(6-5,2)+math.pow(9-8,2))
	pot12 = 4*(math.pow(1/r12,12)-math.pow(1/r12,6))
	pot13 = 4*(math.pow(1/r13,12)-math.pow(1/r13,6))
	pot23 = 4*(math.pow(1/r23,12)-math.pow(1/r23,6))
	pot = f90.ljpotalleatomen(atomen,3)
	assert round(pot12+pot13+pot23,7) == round(pot,7)


#===============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
#===============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_f90_add

    print(f"__main__ running {the_test_you_want_to_debug} ...")
    the_test_you_want_to_debug()
    print('-*# finished #*-')
#===============================================================================
