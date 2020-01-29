from hw1 import conversion_func
import pytest


def test_func1():
	assert conversion_func(4) == "IV"
def test_func2():
	assert conversion_func(5) == "V"
def test_func3():
	assert conversion_func(310) == "CCCX"
def test_func4():
	assert conversion_func(17) == "XVII"
def test_func5():
	assert conversion_func(500) == "D"
def test_func6():
	assert conversion_func(137) == "CXXXVII"
def test_func7():
	assert conversion_func(1998) == "MCMXCVIII"
def test_func8():
	assert conversion_func(270) == "CCLXX"
def test_func9():
	assert conversion_func(46) == "XLVI"
