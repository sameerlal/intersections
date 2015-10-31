import random
from sys import argv
import csv
script, out = argv
# change to 'wr' to fail if file does not exist
outfile = open(out, 'w')
filewriter = csv.writer(outfile)
#	A = 0, B = 1, C = 2, D = 3
filewriter.writerow( ('iteration', 'A' , 'B' , 'C'))
iterations = raw_input("Enter iterations: " + "\n" + ">> ")
for i in range(int(iterations)):
	A = random.randint(1,3)
	B = random.randint(1,3)
	if(B == 1):
		B = 0
	C = random.randint(0,2)
	if(C==2):
		C = 3
	D = random.randint(0,2)
	filewriter.writerow( (i+1,str(A),str(B),str(C),str(D)))
outfile.close()