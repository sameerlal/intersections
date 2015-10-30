import random
from sys import argv
import csv
script, out = argv
# change to 'wr' to fail if file does not exist
outfile = open(out, 'w')
filewriter = csv.writer(outfile)
filewriter.writerow( ('iteration', 'A' , 'B' , 'C'))
iterations = raw_input("Inter iterations: " + "\n" + ">> ")
for i in range(int(iterations)):
	filewriter.writerow( (i+1, str(random.randint(0,3)), str(random.randint(0,3)), str(random.randint(0,3)) ) )
outfile.close()