# -*- coding: utf-8 -*-
"""
Package projectparallelprogrammeren
=======================================

A 'hello world' example.
"""
__version__ = "0.0.2"



def hello(who='world'):
    """'Hello world' method.

    :param str who: whom to say hello to (default = 'world')
    :returns: a string
    """
    result = "Hello " + who
    return result
    
if __name__=="__main__":
	assert hello() == "Hello world"
	assert hello("user of this code") == "Hello user of this code"
	print("-*# success #*-")

# eof
