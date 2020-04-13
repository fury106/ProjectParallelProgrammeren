#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ProjectParallelProgrammeren` package."""

import os
import sys
import pytest
import math

from click.testing import CliRunner
from click import echo

#import projectparallelprogrammeren as ppp
from projectparallelprogrammeren import atomen

#def test_greet():
 #   expected = "Hello John!"
  #  greeting = greet("John")
   # assert greeting==expected

def test_afstand():
	test = atomen.Atomen(5)
	atoom1 = test.getCoordinate(1)
	atoom2 = test.getCoordinate(2)
	expected = math.sqrt(math.pow((atoom1[0] - atoom2[0]) , 2) + math.pow((atoom1[1] - atoom2[1]) , 2) + math.pow((atoom1[2] - atoom2[2]) , 2))
	afstand = test.afstandTweeAtomen(1, 2)
	assert afstand == expected

def test_afstand_zelfde_atoom():
	test = atomen.Atomen(2)
	atoom = test.getCoordinate(1)
	expected = 0
	afstand = test.afstandTweeAtomen(0,0)
	assert afstand == expected
	
def test_bereken_LJ_Pot():
	test = atomen.Atomen(4)
	atoom1 = test.getCoordinate(0)
	atoom2 = test.getCoordinate(1)
	atoom3 = test.getCoordinate(2)
	atoom4 = test.getCoordinate(3)
	r12 = test.afstandTweeAtomen(0,1)
	r13 = test.afstandTweeAtomen(0,2)
	r14 = test.afstandTweeAtomen(0,3)
	r23 = test.afstandTweeAtomen(1,2)
	r24 = test.afstandTweeAtomen(1,3)
	r34 = test.afstandTweeAtomen(2,3)
	pot12 = 1/math.pow(r12,12) - 1/math.pow(r12,6)
	pot13 = 1/math.pow(r13,12) - 1/math.pow(r13,6)
	pot14 = 1/math.pow(r14,12) - 1/math.pow(r14,6)
	pot23 = 1/math.pow(r23,12) - 1/math.pow(r23,6)
	pot24 = 1/math.pow(r24,12) - 1/math.pow(r24,6)
	pot34 = 1/math.pow(r34,12) - 1/math.pow(r34,6)
	expected = round(pot12 + pot13 + pot14 + pot23 + pot24 + pot34, 5)
	pot = round(test.berekenLJPot(), 5)
	assert pot == expected

	

# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_

    the_test_you_want_to_debug()
    print("-*# finished #*-")
# ==============================================================================
