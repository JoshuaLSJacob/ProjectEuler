max_num = 0
for a in range(1,9876):
	if len(set(str(a))) == len(str(a)) and '0' not in str(a):
		success = False
		num = a
		b = 2
		while not success:
			num = int(str(num)+str(b*a))
			if len(str(num)) == 9 and len(set(str(num))) == len(str(num)) and '0' not in str(num):
				print num

				success = True
			elif (len(str(num)) == 9 and len(set(str(num))) != len(str(num))) or len(str(num)) > 9 :
				break
			b += 1
	if success == True and num > max_num :
		max_num = num
print max_num