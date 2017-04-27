def getsome(word, num):
	Rword = ""
	for letter in word:
		for count in range(num):
			Rword = Rword+letter
	return Rword


hi = getsome("That's Not Guud", 2)
print(hi)