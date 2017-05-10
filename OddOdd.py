def OddOdd(value):
	Toogle = True
	SumtoReturn = 0
	for Values in value:
		if (Toogle == True):
			if(value.index(Values)%2 == 1):
				SumtoReturn = SumtoReturn + Values
	Toogle = not Toogle
	return SumtoReturn

print(OddOdd([1,3,6,9]))