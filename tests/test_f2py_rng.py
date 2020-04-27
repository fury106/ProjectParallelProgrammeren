#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for f2py module `projectparallelprogrammeren.rng`."""

import projectparallelprogrammeren as ppp
# create an alias for the binary extension cpp module
f90 = ppp.rng.my_f90_module

def test_f90_seed():
	"""Test standaars 'seed' en zijn bijhorende initiele stauts"""
	f90.set_seed(1)
	assert f90.seed == 1
	assert f90.x == 1
	
def test_f90_set_seed():
	"""Test voor het toewijzen van een waarde aan 'seed'"""
	f90.set_seed(1)
	assert f90.seed == 1
	assert f90.x == 1

def test_f90_lcg1():
	""" Deze test vergelijkt the fortran variant met de python variant"""
	# 'seed' instellen
	seed = 1
	lcg1 = ppp.LCG(seed=seed)
	f90.set_seed(seed)
	# test voor 10 cijfers
	for i in range(10):
		r = lcg1()
		fr = f90.lcg1()
		assert r == fr
		
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
