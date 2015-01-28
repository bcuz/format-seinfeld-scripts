import urllib
from sys import argv

# This file saves the raw html of each episode in it's own file formatted "Seinfeld *episode number*"
# There's no need to really run this file ever again, unless something happens to my current library
# of saved raw html files

# after "py filename.py" you put the first script you want up to and including the last script
# It'll download all scripts in between. If you just want one script, you enter the same number twice
script, start_num, end_num = argv
# converts the number from a string to a num, so it can be used in a range
start_num = int(start_num)
end_num = int(end_num)

# episodes that are just duplicates of the previous one
duplicates = [83, 101, 178, 180]

# if the episode is a duplicate of the previous one, treat it as the previous one
if start_num in duplicates:
	start_num -= 1

# if 0 is entered then all the scripts from the start_num to episode 180 (inclusive) are extracted
if end_num == 0:
	end_num	= 180

# custom function to find the second instance of " - ", which helps in locating the pages title
def find_nth(str1, substr1):
  return str1.find(substr1,str1.find(substr1)+1)

# episodes that have the same link and are wierdly conjoined like "82and83"
conjoined = [82, 100, 177, 179]
# the first script saved is start_num, and the last script saved is end_num - 1
# since range stops at the number before second in range(first, second)
def magic(start_num):
	for num in range(start_num, end_num+1):
		global counter
	 	counter = num
		# deals with the conjoined scripts
		if num in conjoined:
			webpage = urllib.urlopen("http://www.seinology.com/scripts/script-" + str(num) + "and" + str(num+1) + ".shtml").read()
		# if the episode number is a duplicate, go on to the next episode number
		elif num in duplicates:
			continue
		# deals with scripts 1-9, which are formatted like script-01		
		elif num in range(1, 10):
			webpage = urllib.urlopen("http://www.seinology.com/scripts/script-0" + str(num) + ".shtml").read()		
		# deals with the rest of the episodes
		else:
			webpage = urllib.urlopen("http://www.seinology.com/scripts/script-" + str(num) + ".shtml").read()

		# open a file with the designated title in writing mode
		f = open("Seinfeld " + str(num) + ".txt", 'w')
		# write the script to the file
		f.write(webpage)
		f.close()


magic(start_num)

# Test to see if all the files have been downloaded, if a request to go all the way to the last
# episode has been made. 
if end_num == 180:
	try:
		# attempts to open the last episode that should've been created
	 	fil = open("Seinfeld 179.txt", 'r') 

	 	# if the file is found, the program ends
		if True:
			print "Ending..."

	# if the file isn't found, we run the function again, starting from the episode after 
	# the process stopped		
	except:
		print "Continuing..."
		magic(counter+1)	