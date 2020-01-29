from hw1 import conversion_func
import pytest


def test_func1():
	assert conversion_func(4) == "IV"
def test_func2():
	assert conversion_func(5) == "V"
