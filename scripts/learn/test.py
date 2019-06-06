with open('news1.txt') as workFile :
	count =0
	lines = workFile.readlines()
	for line in lines :
		if '<title>' in line :
#			print(line)
			title_start=len(line)
			title_end=title_start-20
			title = line[8:title_end]
			print(title)
		elif 'Yanditswe' in line :
			print (line)
			print(author)
	#		author = line[122:143]
	#		print (author)
#		elif line != '' :
#			count +=1
#	print('Number of lines is :'+str(count))
workFile.close()
