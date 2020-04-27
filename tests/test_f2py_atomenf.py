#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for f2py module `projectparallelprogrammeren.atomenf`."""

import projectparallelprogrammeren as ppp
# create an alias for the binary extension cpp module
f90 = ppp.atomenf.f90_module

def test_lj2atomen():
	"""Test om de potentiaal tussen 2 atomen te berekenen"""
	afstand = 1.5
	pot = 4*((1/afstand)**12 - (1/afstand)**6)
	potf = f90.ljpot2atomen(afstand)
	assert round(pot, 7) == round(potf, 7)


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
