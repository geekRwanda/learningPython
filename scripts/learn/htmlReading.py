print('***************************************************************************************')
print('This is a Simple Python Script Written by Yves Dominique GATONI to work on a predefined text file')
print('***************************************************************************************')
def HTML_Analysis():
	count =0 #Creating a count variabe for holding line numbers
#an adequate way into openning a file without the need to close if at the end
	with open('amakuru.txt') as workFile: 
		lines = workFile.readlines() #Reading the lines of the file for counting
#Line number counting logic.
	for line in lines :
		if '<title>' in line :
			print('\n')
			print('##################################')
			print('WELCOME TO MY FIRST SCRIPT G33K :))')
			print('##################################')
			print('The news title is : ')
			title = line[20:88]
			print (title)
		elif 'Yanditswe' in line :
			print ('The news Author is :')
			author = line[63:85]
			print (author)
		elif line != '' :
			count += 1
	print ('The number of lines in the given file is :' + str(count))
	print('##################################')
	print('\n')
	def outputWritting():
		with open ('results.txt','a+') as output :
			output.write('The Headline title is: '+title)
			output.write('\n')
			output.write('The Headline Author is :'+author)
			output.write('\n')
			output.write('The number of lines in the file is:' +str(count))
			print ('\n')
		output.close()
	outputWritting()
HTML_Analysis()
