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

# the first script saved is start_num, and the last script saved is end_num - 1
# since range stops at the number before second in range(first, second)
def magic(start_num):
	for num in range(start_num, end_num+1):
		global counter
	 	counter = num

		if num in duplicates:
			continue
		else:
			webpage = open("Seinfeld " + str(num) + ".txt").read()
		
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
		find_script = webpage.find("=====<br>")
		
		# if "=====<br>" is not found, look for "=&nbsp;<br>", which is how two episodes are formatted instead
		if find_script == -1:
			find_script = webpage.find("=&nbsp;<br>")
		if find_script == -1:
			find_script = webpage.find("=</font></p>")	

		#go to the last character of find_script	
		begin_script = webpage.find(">", find_script)
		#start looking for the end of script after the index of begin_script. Episodes end when there's a </td>
		end_script = webpage.lower().find("</td>", begin_script+1)
		# the script starts at the character after ">" and ends at the character just befoer </td> This extracts
		# all the information between these two points
		output = webpage[begin_script+1:end_script]

		# tidying up the script contents
		replace_with_quote = ["&quot;", "&#148;", "&#147;"]

		for special_char in replace_with_quote:
			output = output.replace(special_char, '"')

		replace_with_empty_space = ["\t", "<br>", '<font size="-2">', '</font>', '<p>', '</p>']

		for special_char in replace_with_empty_space:
			output = output.replace(special_char, '')	
			
		output = output.replace("&nbsp;", "") # this might cause problems, but for now it gets rid of special code
		output = output.replace("&rsquo;", "'")
		output = output.replace("&#146;", "'")
		output = output.replace("&#145;", "'")
		output = output.replace("&#150;", "-")
		output = output.replace("&#133;", "...") 
		output = output.replace("&amp;", "&")
		output = output.replace("\n\n\n", "\n\n")
		output = output.replace("\n\n\n\n", "\n\n\n")

		season1 = range(1, 6)
		season2 = range(6, 18)
		season3 = range(18, 41)
		season4 = range(41, 65)
		season5 = range(65, 87)
		season6 = range(87, 111)
		season7 = range(111, 135)
		season8 = range(135, 157)
		season9 = range(157, 181)

		if num in season1:
			episode = "s1e" + str(season1.index(num)+1)
		elif num in season2:
			episode = "s2e" + str(season2.index(num)+1)
		elif num in season3:
			episode = "s3e" + str(season3.index(num)+1)
		elif num in season4:
			episode = "s4e" + str(season4.index(num)+1)
		elif num in season5:
			episode = "s5e" + str(season5.index(num)+1)
		elif num in season6:
			episode = "s6e" + str(season6.index(num)+1)
		elif num in season7:
			episode = "s7e" + str(season7.index(num)+1)
		elif num in season8:
			episode = "s8e" + str(season8.index(num)+1)
		else:
			episode = "s9e" + str(season9.index(num)+1)

		# open a file with the designated title in writing mode
		f = open("output\\Seinfeld " + episode + " " + str(num) + " - " + title + ".txt", 'w')
		# write the script to the file
		f.write(output)
		f.close()
		# need to open it according to the title. Maybe I should simply have the raw html saved without 
		# the title? Definitely has to be in a different order. How do I grab the title without going online? Need
		# to open the file to get it's title though. What if it didn't have a title? If it was just 1, 2, 3
		# could probably figure out how to do it without using urllib again. If i had a list of all the seinfeld episodes

magic(start_num)

if end_num == 180:
	try:
	 	fil = open("Seinfeld s9e23 179 - The Finale (1).txt", 'r') 

		if True:
			print "Ending..."

	except:
		print "Continuing..."
		magic(counter+1)	