def OddOdd(value):
	Toogle = True
	SumtoReturn = 0
	for Values in value:
		if (Toogle == True):
			if(Values%2 == 0):
				SumtoReturn = SumtoReturn + Values
	Toogle = False
	return SumtoReturn

OddOdd([1,3,5,6,7,9])