import urllib

webpage = urllib.urlopen("http://www.seinology.com/scripts/script-08.shtml").read()

find_script = webpage.find("=====================<br>")
begin_script = webpage.find(">", find_script)
end_script = webpage.lower().find("the end", begin_script+1)

output = webpage[begin_script+1:end_script] + "The End"

output = output.replace("\t", "")
output = output.replace("&#146;", "'")
output = output.replace("&#145;", "'")
output = output.replace("&#148;", "\"")
output = output.replace("&#147;", "\"")
output = output.replace("&#150;", "-")
output = output.replace("<br>", "")
output = output.replace("\n\n\n", "\n\n")
output = output.replace("\n\n\n\n", "\n\n\n")

f = open("new_file.txt", 'w')
f.write(output)
f.close()