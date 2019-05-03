x= 0
for a in range(1,1000000,2):
	palindrome = True
	for b in range((len(str(a))/2)):
		if str(a)[b] != str(a)[-b-1]:
			palindrome = False
			break
	if palindrome:
		for c in range((len(bin(a))-2)/2):
			if str(bin(a))[c+2] != str(bin(a))[-c-1]:
				palindrome = False
	if palindrome:
		x += a
print x		
		
