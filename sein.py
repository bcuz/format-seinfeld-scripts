import urllib

webpage = urllib.urlopen("http://www.seinology.com/scripts/script-08.shtml").read()

start = webpage.find("=====================<br>")
step2 = webpage.find(">", start)
step3 = webpage.lower().find("the end", step2+1)

output = webpage[step2+1:step3] + "The End"

output = output.replace("\t", "")

f = open("new_file.txt", 'w')
f.write(output)
f.close()