import urllib

def find_nth(str1, substr1):
  return str1.find(substr1,str1.find(substr1)+1)

other = [82, 83, 100, 101, 177, 178, 179, 180]

for num in range(1, 181):
	if num in other:
		webpage = urllib.urlopen("http://www.seinology.com/scripts/script-" + str(num) + "and" + str(num+1) + ".shtml").read()
	elif num in range(1, 10):
		webpage = urllib.urlopen("http://www.seinology.com/scripts/script-0" + str(num) + ".shtml").read()		
	else:
		webpage = urllib.urlopen("http://www.seinology.com/scripts/script-" + str(num) + ".shtml").read()
	
	find_title = find_nth(webpage, " - ") 
	begin_title = webpage.lower().find("-", find_title)
	end_title = webpage.find("<", begin_title+1)

	title = webpage[begin_title+2:end_title]

	find_script = webpage.find("=====================<br>")
	begin_script = webpage.find(">", find_script)
	end_script = webpage.lower().find("the end", begin_script+1)

	output = webpage[begin_script+1:end_script] + "\n\nThe End"

	output = output.replace("\t", "")
	output = output.replace("&#146;", "'")
	output = output.replace("&#145;", "'")
	output = output.replace("&#148;", "\"")
	output = output.replace("&#147;", "\"")
	output = output.replace("&#150;", "-")
	output = output.replace("<br>", "")
	output = output.replace("\n\n\n", "\n\n")
	output = output.replace("\n\n\n\n", "\n\n\n")

	f = open("Seinfeld ep" + str(num) + " " + title + ".txt", 'w')
	f.write(output)
	f.close()