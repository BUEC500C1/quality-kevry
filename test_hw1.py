from hw1 import conversion_func


def test_func():
	assert conversion_func(4) == "IV"
  
	assert conversion_func(5) == "V"
  
	assert conversion_func(9) == "IX"
