#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ProjectParallelProgrammeren` package."""

import os
import sys
import pytest
import math

from click.testing import CliRunner
from click import echo

import projectparallelprogrammeren

#def test_greet():
 #   expected = "Hello John!"
  #  greeting = greet("John")
   # assert greeting==expected

def test_afstand():
	test = Atomen(5)
	atoom1 = test.getCoordinate(1)
	atoom2 = test.getCoordinate(2)
	expected = math.sqrt(math.pow((atoom1[0] - atoom2[0]) , 2) + math.pow((atoom1[1] - atoom2[1]) , 2) + math.pow((atoom1[2] - atoom2[2]) , 2))
	afstand = test.afstandTweeAtomen(1, 2)
	assert afstand == expected
	

# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_

    the_test_you_want_to_debug()
    print("-*# finished #*-")
# ==============================================================================
