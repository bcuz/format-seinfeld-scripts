import urllib
from sys import argv

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

for num in range(start_num, end_num+1):
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
	
	# uses the find_nth function to find the second instance of " - ", which is nearby the title of the script
	find_title = find_nth(webpage, " - ") 
	# finds the "-" character in the webpage, but it starts looking at the point where find_title is found. 
	# So we're really only moving the cursor from the first character of " - " to the "-" character itself
	# this can probably be deleted actually, and more added to begin_title (which would become find_title) below
	begin_title = webpage.lower().find("-", find_title)
	# find where the title grabbing will stop. Starts searching after the index given by begin_title
	end_title = webpage.find("<", begin_title+1)

	# the title starts to be grabbed at the character right after "- " and ends being extracted at the character
	# right before "<"
	title = webpage[begin_title+2:end_title]

	#find the index where the scripts begin
	find_script = webpage.find("=====================<br>")
	#go to the last character of find_script
	begin_script = webpage.find(">", find_script)
	#start looking for the end of script after the index of begin_script. Episodes end when there's a </td>
	end_script = webpage.lower().find("</td>", begin_script+1)
	# the script starts at the character after ">" and ends at the character just befoer </td> This extracts
	# all the information between these two points
	output = webpage[begin_script+1:end_script]

	# tidying up the script contents
	output = output.replace("\t", "")
	output = output.replace("&#146;", "'")
	output = output.replace("&#145;", "'")
	output = output.replace("&#148;", "\"")
	output = output.replace("&#147;", "\"")
	output = output.replace("&#150;", "-")
	output = output.replace("<br>", "")
	output = output.replace("\n\n\n", "\n\n")
	output = output.replace("\n\n\n\n", "\n\n\n")

	# open a file with the designated title in writing mode
	f = open("Seinfeld ep" + str(num) + " " + title + ".txt", 'w')
	# write the script to the file
	f.write(output)
	f.close()