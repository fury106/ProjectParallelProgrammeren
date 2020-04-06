#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ProjectParallelProgrammeren` package."""

import os
import sys
import pytest

from click.testing import CliRunner
from click import echo

import projectparallelprogrammeren 


def test_greet():
    expected = "Hello John!"
    greeting = greet("John")
    assert greeting==expected


# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_

    the_test_you_want_to_debug()
    print("-*# finished #*-")
# ==============================================================================
