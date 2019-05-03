import csv
count = 0
alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet.index('a')
with open('/Users/joshuajacob/Desktop/Project Euler/42_words.txt') as names:
	for row in csv.reader(names):
		for word in row:
			word_count = 0
			for letter in word:
				word_count += alphabet.index(letter.lower())+1
			if 0.5*(-1+(1+8*float(word_count))**0.5)%1 == 0:
				count += 1
				print word, word_count, 0.5*(-1+(1+8*float(word_count))**0.5)
print count